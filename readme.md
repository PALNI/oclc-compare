# Compare two sets of MARC records by OCLC number
This scripts enables the comparison of two sets of MARC records by OCLC number, as would
be needed in a project that compared the holdings of two libraries.  The instructions
below presume you want to see how many of library 1's holdings are in library 2's holdings.

* Presumes Python3
* Requires PyMARC
* Presumes the OCLC number is in the 035 $a field
* 035 $z fields are not checked

## Instructions
Download this repository and unzip it.  Within the folder created by the repository, create
two directories: library1 and library2.

Place MARC records for library 1 in the library1 folder, and the MARC records for library 2
in the library2 folder.  You can place multiple MARC files in each folder, the script will
process every .mrc file found in each folder.

Run oclc_compare.py.  The output will count the number of of OCLC numbers from the library1
folder that are not found in the library2 folder.


