from bs4 import BeautifulSoup
import mechanize
import re


"""
@author Nils Bouchardon
"""

url_prefix = 'http://www.tvsubtitles.net/'
f = open('list_of_URLs_end.txt', 'r')
br = mechanize.Browser()

while 1:

	line = f.readline()
	if not line:
		break
	splitedLine = line.split('.')[0].split('-')
	numb_of_season = int(splitedLine[2])
	
	for i in range(numb_of_season):
	
		root = '-'+splitedLine[1]+'-'+str(i+1)+'-en.html'
	
		#----------------------------------------------------------------------------
		# Zip name retrieval :
		
		page = br.open(url_prefix+'subtitle'+root)
		zName = BeautifulSoup(page.read()).find(text=re.compile('.zip'))
		
		#----------------------------------------------------------------------------
		# Download :
		
		if zName is not None:
			dwldLink = url_prefix+'download'+root
			try:
				r = br.retrieve(dwldLink, zName)
				print 'Downloaded :'+zName
			except:
				print "Error"
					
		#----------------------------------------------------------------------------

