import csv

def convert_to_html(dictionary, indent=0):
	p=[]
	p.append('<ul>\n')
	for k,v in dictionary.iteritems():
 		if isinstance(v, dict):
 	  		p.append('<li>'+ str(k) + ':')
 	        p.append(convert_to_html(v))
 	        p.append('</li>')
     	else:
 	        p.append('<li>'+ str(k) + ':'+ str(v) + '</li>')
 		    p.append('</ul>\n')
 	return '\n'.join(p)

products = {}
file_name= raw_input('Please enter file name: ')
print 'the file name you entered is ', file_name

with open (file_name, 'rb') as csvfile:
	report = csv.reader(csvfile, delimiter=',')
	for row in report:
		print row
		products[row[0]]={'qty':qty,'revenue':revenue}

