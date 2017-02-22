import urllib2
from urllib2 import urlopen
from bs4 import BeautifulSoup
from pymongo import MongoClient
import time
from tqdm import tqdm
import pymongo

# DB
client = MongoClient()
db = client['memes']
popular = db.popular


count = 0
##check every page of popular memes on knowyourmeme
for x in tqdm(range(258)):
	time.sleep(0.2)
	# Create http request
	request = urllib2.Request('http://knowyourmeme.com/memes/popular/page/'+ str(x) )
	request.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
	html = urllib2.urlopen(request)
	soup = BeautifulSoup(html ,  "html.parser")

	##get only the image section
	imagesection = soup.find(id="entries_list")

	for img in imagesection.find_all('img'):
		count += 1
		data = {}
		data["title"] = img['title']
		data["imgsrc"] = img['data-src']
		data["memeid"] = count
		popular.insert(data)



	
