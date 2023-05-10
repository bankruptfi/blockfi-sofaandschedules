# blockfi-sofaandschedules

Collection of files and scripts to process data from various BlockFi related documents.

| File/Direcotry                    | Purpose                                       |
| --------------------------------- | --------------------------------------------- |
| output-stage1/                    | Output from extract-pdf-tables.py (camelot)   |
| output-stage2/                    | Output from invoke*.ps1 scripts               |
| pdf/                              | PDF/Court Docket files to process             |
| extract-pdf-tables.py             | Extract tables from PDF documents             |
| invoke-convertPropertyHeld.ps1    | Combine output from camelot into one csv file |
| invoke-convertUnsecuredClaims.ps1 | Combine output from camelot into one csv file |
| invoke-convert90daypayments.ps1   | Combine output from camelot into one csv file |
