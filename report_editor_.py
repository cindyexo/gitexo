import CSV

products = {}

with open ('test.csv') as csvfile:
	report = csv.reader(csvfile, delimiter=',')
	for row in report:
		print row
