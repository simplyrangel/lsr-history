"""Create the timeline table."""
import numpy as np
import pandas as pd

# autogenerated message:
def autogen_message():
    return "% This file was autogenerated by timeline.py.\n%\n"

# read the spreadsheet:
df = pd.read_excel("timeline.xlsx", dtype=str)
df.columns = [0,1,2,3,4]
df = df.fillna(" ")

# set up table:
table_format = "\\begin{longtable}{|p{0.06\\linewidth}|p{0.4\\linewidth}|p{0.4\\linewidth}|p{0.1\\linewidth}|}"
row_template = "{} & {} & {} & {} \\\ \n"
caption = "\\caption{High level timeline of Lawrence Ross' family and personal life.}"

headers = [
    "Year",
    "State or national history",
    "LSR personal or family history",
    "Source"]
headers = ["\\textbf{%s}" %x for x in headers]
headers_str = ""
for hede in headers[:-1]:
    headers_str += "%s & " %hede
headers_str += "%s" %headers[-1]

# create latex table:
with open("timeline.tex", "w") as of:
    of.write(autogen_message())
    of.write("%s \n" %table_format)
    of.write("%s \\\ \n" %caption) #two dashes are needed for the caption at the top of longtable
    
    # column headers:
    of.write("\\hline \n")
    of.write("%s \\\ \n" %headers_str)
    of.write("\\hline \n")

    # write rows:
    for ii in df.index:
        row = row_template.format(
            "%s" %df.loc[ii, 0],
            "%s" %df.loc[ii, 1],
            "%s" %df.loc[ii, 2],
            "%s" %df.loc[ii, 3])
        of.write(row)
        of.write("\\hline \n")
    
    # end longtable:
    of.write("\\end{longtable}")






