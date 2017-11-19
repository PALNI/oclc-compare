from pymarc import MARCReader
import csv, re
from os import listdir
from re import search

#process library1's holdings

SRC_DIR = 'library1'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('library1/library1_oclc.txt', 'w'), delimiter = '\t')

oclc_number = ''

#print all OCLC numbers (035|a)
for item in file_list:
  fd = open(SRC_DIR + '/' + item, 'rb')
  reader = MARCReader(fd)
  for record in reader:
    for f in record.get_fields('035'):
      if f['a'] is not None:
        oclc_number = (f['a'])
        oclc_number = re.sub("[^0-9]", "", oclc_number)
      csv_out.writerow([oclc_number])
  print('end of library 1 records')
print('finished library1')


#process library2's holdings

SRC_DIR = 'library2'

# get a list of all .mrc files in source directory
file_list = filter(lambda x: search('.mrc', x), listdir(SRC_DIR))

csv_out = csv.writer(open('library2/library2_oclc.txt', 'w'), delimiter = '\t')

oclc_number = ''

#print all OCLC numbers (035|a)
for item in file_list:
  fd = open(SRC_DIR + '/' + item, 'rb')
  reader = MARCReader(fd)
  for record in reader:
    for f in record.get_fields('035'):
      if f['a'] is not None:
        oclc_number = (f['a'])
        oclc_number = re.sub("[^0-9]", "", oclc_number)
      csv_out.writerow([oclc_number])
  print('end of library2 records')
print ('finished library2')
      

#compare the two outfiles
outfile = open("complete_analysis.txt", "w")
lines_to_check_for = [ line for line in open("library2/library2_oclc.txt", "r") ]
for line in open("library1/library1_oclc.txt", "r"):
    print('checking ' + str(line))
    if not line in lines_to_check_for:
        outfile.write(line)
outfile.close 
with open(outfile) as f:
  for i, l in enumerate(f):
    pass
    diffcount =  i + 1
print('analysis complete, # of different numbers found = ' diffcount)