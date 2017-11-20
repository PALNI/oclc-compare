import csv

with open("library2/oclc_pln.txt", "r") as f:
  reader = csv.reader(f, delimiter = '\t')
  mydict = {rows[0] for rows in reader}
  length = len(mydict)
  print(length)
  
csv_out = csv.writer(open('nd_not_in_palni.txt', 'w'), delimiter = '\t')

with open("library1/library1_oclc.txt", "r") as g:
  reader2 = csv.reader(g, delimiter = '\t')
  for row in reader2:
    if row[0] in mydict:
      pass
    else:
      csv_out.writerow([row[0],row[1],row[2],row[3]])