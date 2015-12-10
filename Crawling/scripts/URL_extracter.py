from bs4 import BeautifulSoup
import urllib2

"""
@author Nils Bouchardon
"""


url = "http://www.tvsubtitles.net/setlang.php?page=/tvshows.html&setlang1=en"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
file = open('list_of_URLs.txt', 'w')



table = soup.table
links = table.find_all('a', )

for link in links:
	file.write(link.get('href')+'\n')
	
file.close()	



