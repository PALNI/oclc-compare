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

Run `python3 oclc_compare.py`.  This script creates two output files of OCLC numbers.  The output file 
from library 1 will include title, author, and publication date as well as OCLC number.

When the script finishes, you will see 'finished library2' output in your Terminal. 

Run `python3 compare_lookup.py`.  This script will look up all of the OCLC numbers from 
library1 in the library2 set of OCLC numbers.  If a match is *not* found, the OCLC number,
title, author, publication date from the library1 set will be written to a final output file.


