import csv
open ('hola file.csv') as csvfile:
report = csv.reader(csvfile, delimiter=';')
print report
