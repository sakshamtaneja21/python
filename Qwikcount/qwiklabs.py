import requests
from bs4 import BeautifulSoup
import html5lib
import sys
import csv
import validators

_cache = {}
failed = []
def _read(url):
	text = _cache.get(url)
	if text is None:
		text = requests.get(url).text
		if not text:
			raise Exception('Empty response. Check connectivity.')
		_cache[url] = text
	return text

def qwikcount(url):

	r = requests.get(url)
	soup = BeautifulSoup(r.content,'html5lib')
	count = 0
	body = soup.body

	divTag = soup.find("div", {'class': 'public-profile__badges'})

	classes = []
	children = divTag.find_all("div",recursive = False)
	nameTag = soup.find("h1", {'class': 'l-mbm'}, text=True)
	value = nameTag.text.lstrip("\n").rstrip("\n")
	for child in children:
		count = count+1
	return count,value

if sys.version_info[0] ==2:
	input = raw_input
n=0
name=""
value=""
input_file = input('Enter input file name (csv file): ')
# input_file = 'file.csv'
output_file = input('Enter output file name (Default output.csv): ')

if not output_file.replace(' ', ''):
	output_file = 'output.csv'

with open(input_file, 'r') as fin:
	with open(output_file, 'w') as fout:
		fout.write('Name' + ',' + 'Name on Qwiklabs' + ',' + 'Qwiklabs Profile' + ',' + 'Number of Quest Completed' + ',' + 'Status' + '\n')
		reader = csv.reader(fin)
		for line in reader:
			if(n==1):
				name=line[0]
				n=0
			if(line[0].isdigit()):
				n=n+1
			url = line[0]
			if(validators.url(str(url))):
				print('Fetching Quest Count :',name)
				try:
					count,value =qwikcount(url)
					statuss="Incomplete"
					if(count >= 5):
						statuss = "Completed"
				except Exception as e:
					print("Failed :",name)
					print(e)
					value =""
					count = 'N/A'
					statuss= "Error"
					failed.append(name)
				fout.write( name + ',' + str(value) + ',' + url+ ',' + str(count) + ',' + statuss + '\n')
					
print("Export Complete")

