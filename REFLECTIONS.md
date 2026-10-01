# Assignment reflections

## Which metadata standard did you choose and why?

I selected the Data Documentation Initiative (DDI), specifically the DDI-Codebook documentation model. It provides a useful structure for documenting a research study, its files and its variables. This dataset combines repeated student observations, AI interaction metrics and assignment grades, so readers need both study-level context and detailed variable definitions. The README and data dictionary follow this structure in human-readable form; they are not a validated DDI XML file.

## Which template/software did you use?

The project uses a custom GitHub-compatible Markdown README organized around the assignment's five rubric categories. Python, pandas and openpyxl were used for read-only workbook inspection, descriptive profiling and consistency checks. The variable dictionary and audit results are stored as CSV files. AI assistance supported the code and documentation, with definitions checked against the workbook, Zenodo metadata and the authors' publicly available scripts.

## What was the most challenging part, and how was it addressed?

The most challenging part was distinguishing what the spreadsheet directly shows from what requires external documentation. In particular, blank values and zeros had different patterns depending on attendance and AI access. The audit also found 20 records with positive query counts despite no recorded AI access, including four absent records. In addition, the current public export code did not fully match the workbook's missing-value conventions. These issues were addressed by preserving the source, recording the discrepancies, linking the inspected code, and separating verified observations from unresolved definitions. This avoids presenting assumptions as facts or making undocumented corrections.
