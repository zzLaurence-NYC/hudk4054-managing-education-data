"""Read-only workbook audit. Usage: python audit.py '/absolute/path/data.xlsx'
Requires pandas and openpyxl. Reports go in audit_results beside this script, never to source.
"""
from pathlib import Path
import sys, hashlib, json
import pandas as pd
import openpyxl

source = Path(sys.argv[1]).expanduser().resolve()
out = Path(__file__).resolve().parent / "audit_results"
out.mkdir(exist_ok=True)
before = hashlib.sha256(source.read_bytes()).hexdigest()
wb = openpyxl.load_workbook(source, data_only=False)
inventory = []
for ws in wb:
    inventory.append(dict(sheet=ws.title, rows_including_header=ws.max_row,
        columns=ws.max_column, state=ws.sheet_state,
        merged_ranges=[str(x) for x in ws.merged_cells.ranges],
        formula_count=sum(c.data_type == 'f' for row in ws for c in row),
        hidden_rows=[k for k,v in ws.row_dimensions.items() if v.hidden],
        hidden_columns=[k for k,v in ws.column_dimensions.items() if v.hidden]))
print('1. WORKBOOK', inventory)

# Inspect raw cells BEFORE pandas converts blanks into NaN.
ws = wb['Sheet1']
raw = list(ws.values)
headers = list(raw[0])
assert len(set(headers)) == len(headers), 'Duplicate column names: inspect first.'
d = pd.read_excel(source, sheet_name='Sheet1')
profile = []
for j, col in enumerate(headers):
    s = d[col]
    numeric = pd.api.types.is_numeric_dtype(s)
    profile.append(dict(variable=col, dtype=str(s.dtype),
        physical_blanks=sum(row[j] is None for row in raw[1:]),
        pandas_missing=int(s.isna().sum()), missing_pct=round(s.isna().mean()*100,2),
        unique_nonmissing=int(s.nunique()),
        observed_min=s.min() if numeric else '',
        observed_max=s.max() if numeric else '',
        noninteger_count=int((s.dropna()%1 != 0).sum()) if numeric else '',
        whitespace_only=sum(isinstance(row[j],str) and not row[j].strip() for row in raw[1:]),
        categories='; '.join(map(str,s.dropna().unique())) if not numeric and col!='Student ID' else ''))
pd.DataFrame(profile).to_csv(out/'variable_profile.csv',index=False,encoding='utf-8-sig')
print('2. VARIABLES\n',pd.DataFrame(profile).to_string(index=False))

checks = []
def check(name, count, interpretation):
    checks.append(dict(check=name,count=int(count),interpretation=interpretation))
check('Rows',len(d),'Student-week records, including absent weeks')
check('Students',d['Student ID'].nunique(),'Distinct identifiers')
check('Exact duplicate excess rows',d.duplicated().sum(),'Do not delete automatically')
check('Student-week duplicate excess rows',d.duplicated(['Student ID','Week']).sum(),'Candidate key test')
check('Students without all 16 weeks',sum(set(g.Week)!=set(range(1,17)) for _,g in d.groupby('Student ID')),'Coverage test')
check('Students mapped to multiple courses',(d.groupby('Student ID').Course.nunique()>1).sum(),'Identifier consistency')
for col in ['Attendance','AI Access']:
    check(col+' invalid codes',(~d[col].isin([0,1])).sum(),'Documented binary coding')
check('Week invalid',(~d.Week.isin(range(1,17))).sum(),'Documented semester weeks')
check('Assignment outside 0-100',(d['Assignment Score'].notna() & ~d['Assignment Score'].between(0,100)).sum(),'Documented grade scale')
for col in ['Assignment Score','Structural Complexity Score','Content Richness Score']:
    check(col+' missingness differs from absence',(d[col].isna() != d.Attendance.eq(0)).sum(),'Association, not proof of missingness mechanism')
for col in ['AI Response Reliance Score','Prompt Refinement Depth Score','AI Response Complexity Score']:
    check(col+' missingness differs from no access',(d[col].isna() != d['AI Access'].eq(0)).sum(),'Structural missingness candidate; confirm with documentation')
for col in ['AI Query Depth & Structure Score','AI Query Efficiency Score','AI Response Utility Score','AI-Driven Problem-Solving Score']:
    check(col+' nonzero without access',((d['AI Access']==0)&(d[col]!=0)).sum(),'Zero may be export placeholder')
flags = (d['AI Access']==0)&(d['AI Query Count']>0)
check('Queries without AI access',flags.sum(),'Needs source/log verification, not automatic correction')
check('Queries while absent',((d.Attendance==0)&(d['AI Query Count']>0)).sum(),'Subset of access inconsistencies')
anomalies=d.loc[flags].copy()
anomalies.insert(0,'excel_row',anomalies.index+2)
anomalies.to_csv(out/'flagged_records.csv',index=False,encoding='utf-8-sig')
pd.DataFrame(checks).to_csv(out/'audit_checklist.csv',index=False,encoding='utf-8-sig')
print('3. CHECKS\n',pd.DataFrame(checks).to_string(index=False))
print('4. ATTENDANCE / ACCESS\n',pd.crosstab(d.Attendance,d['AI Access']))
print('5. MISSING BY ACCESS\n',d.groupby('AI Access').agg(lambda s:s.isna().sum()).to_string())
print('6. WEEK / ACTIVITY\n',pd.crosstab(d.Week,d['Activity Type']).to_string())
access = d['AI Access'].eq(1)
expected = (d.loc[access,'AI Query Depth & Structure Score'] / d.loc[access,'AI Query Count']).clip(upper=100).round(2)
delta = (d.loc[access,'AI Query Efficiency Score'] - expected).abs()
check('QE exact matches using exported inputs',delta.lt(1e-9).sum(),'Formula diagnostic among AI-access records; not full pipeline reproduction')
check('QE differences greater than 0.5',delta.gt(0.5+1e-9).sum(),'Diagnostic threshold; raw-input precision and code version unresolved')
pd.DataFrame(checks).to_csv(out/'audit_checklist.csv',index=False,encoding='utf-8-sig')
print('QE diagnostic:', int(delta.lt(1e-9).sum()), 'exact;', int(delta.gt(0.5+1e-9).sum()), 'over 0.5')
after = hashlib.sha256(source.read_bytes()).hexdigest()
assert before == after, 'Source hash changed.'
manifest=dict(source=str(source),md5=hashlib.md5(source.read_bytes()).hexdigest(),
    sha256_before=before,sha256_after=after,source_unchanged=before==after,
    pandas_version=pd.__version__,openpyxl_version=openpyxl.__version__,sheets=inventory)
(out/'audit_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print('7. SOURCE UNCHANGED',before==after)
