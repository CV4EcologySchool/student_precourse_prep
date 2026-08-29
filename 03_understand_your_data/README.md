# Session 3: exploratory data analysis of your dataset

## What you should learn

- the difference between media, metadata, and annotations;
- how to read a CSV table with Pandas;
- how to inspect rows, columns, data types, and missing values;
- how to count targets and natural data groups;
- how one simple table or plot can reveal a data question;
- how metadata rows connect back to media files and later dataset code.

## Before the session

If possible, prepare a small metadata extract from your own project as a CSV.
It should contain enough rows to show the structure of your data but does not
need to describe the full dataset. Do not add research data to this repository.

Know the local path to the CSV and, if available, the directory containing a
small corresponding media sample. Ask an instructor for help creating a safe
extract if the data are large, remote, restricted, or stored in another format.

## Guided exploratory data analysis (EDA)

Open `explore_your_data.ipynb` in VS Code. The first part uses
`example_metadata.csv`, a small fictional camera-trap table with an
iWildCam-like structure. It demonstrates the Pandas operations without the
large downloads and custom helper code required by the old iWildCam assignment.

The main part asks you to apply the same checks to your own metadata:

1. define what one row represents;
2. inspect its shape, columns, data types, and missing values;
3. identify sample ID, media filename, target, and natural-group columns;
4. count a meaningful target and group;
5. compare the target across groups;
6. make and interpret one plot;
7. check unique IDs and, when possible, links to media files; and
8. record one concrete data question for the instructors.

If your metadata are not ready, use the supplied example for the entire
notebook and record what must happen before your own data can be explored.

## Extra reading and source:

This exercise uses the same core concepts as Data Carpentry's [Starting With Data](https://datacarpentry.github.io/python-ecology-lesson/02-starting-with-data.html). The most relevant sections are:

- importing Pandas;
- reading CSV data;
- inspecting a DataFrame;
- grouping and counting;
- quick plotting.

The original lesson uses the Portal Project Teaching Database and is CC-BY 4.0. Completing its other chapters is not required.

