# Lawrence Sullivan Ross personal research project
A personal passion project researching the history of Lawrence Sullivan Ross. The research document is meant to provide a historical framework for discussions on Lawrence Sullivan Ross' place in Texas A&M University's culture. These discussions were prompted by the 2020 United States cultural reckoning in the wake of George Floyd's death at the hands of Minnesota police officers. 

This project attempts to answer common questions about Lawrence Ross' behaviors, beliefs, and actions concerning African Americans before, during, and after the Civil War. This document does not discuss Lawrence Ross' history with Native Americans, his years as president of the Agricultural and Mechanical College of Texas, or what role he should play in Texas A&M's current and future culture. 

# Sources
Research material generated in the creation of this document, and the items cited throughout, are available online via Google Drive:
https://drive.google.com/drive/folders/1h493Edj-1fKCnI8hRfd1kw8nYTTstslM

The Google Drive directory includes .png and .pdf newspaper clippings, undergraduate and graduate research papers, library research output, and important email correspondence. 

# Using pdflatex
This repository uses pdflatex to generate documents. Pdflatex is a TeX modification which allows TeX to output to PDF directly. Check the LateX webpage (https://www.latex-project.org/get/) for installation instructions. 

The report uses several tex packages. My latex distribution required me to download the following packages before I could successfully create documents with a bibliography and a way to references sources in the document. 
```console
sudo apt-get install texlive-bibtex-extra
sudo apt-get install texlive-latex-extra
```

The report uses the bibtex package to manage citations and bibliographies. Bibtex relies on several files that can be autogenerated with an intermediate step after `pdflatex texfile.tex` is first run. The following command sequence is required if any changes to the report's citations or bibliography are made:
```console
pdflatex texfile.tex
bibtex texfile
pdflatex texfile.tex
```
