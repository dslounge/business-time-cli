#!/usr/bin/python

import json
import urllib2
import sys
import yaml

#for checking if a row of data belongs to men's or women's bathroom
menIdent = "Men's Room"
womenIdent = "Women's Room"	

#for printing stuff out
class line:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

	@staticmethod
	def ok (txt):
		line.printColor(txt, line.OKGREEN)

	@staticmethod
	def fail (txt):
		line.printColor(txt, line.FAIL)

	@staticmethod
	def warn (txt):
		line.printColor(txt, line.WARNING)

	@staticmethod
	def printColor (txt, color):
		#convert txt to string if it's not
		safeTxt = txt if isinstance(txt, str) else str(txt)
		print color + safeTxt + line.ENDC


printByStatus = {"open": line.ok, "closed": line.fail}

#print using an appropriate color based on bathroom status
def printBathroom(b):
	name = b['name']
	status = b['value']
	printByStatus.get(status, line.warn)(name + ": " + status)	

try: 
	# load url endpoint	
	with open("config.yml", 'r') as ymlfile:
		cfg = yaml.load(ymlfile)
		endpoint = cfg['business-time']['api-url']

	# load data
	allData = json.load(urllib2.urlopen(endpoint))	
	bathrooms = {'men':[], 'women':[]}
	bathrooms['all'] = allData

	# generate dictionary. I wonder if this could be done with one line of python magic
	for item in allData:		
		if menIdent in item['name']:
			bathrooms['men'].append(item)
		else:
			bathrooms['women'].append(item)	

	# check arguments
	arg = "all"
	if len(sys.argv) > 1:
		arg = sys.argv[1]

	# some parameter safety	
	if arg not in ["men", "women", "all"]:
		line.warn("did not understand your parameter, printing all")
		arg = "all"

	#print the bathrooms
	map(printBathroom, bathrooms[arg])


except urllib2.HTTPError, e:
    line.fail('We failed with error code - %s.' % e.code)
except urllib2.URLError, e:
    line.fail("failed to load url: " + endpoint)
except ValueError:  # includes simplejson.decoder.JSONDecodeError
    line.fail('Decoding JSON has failed :(')    	