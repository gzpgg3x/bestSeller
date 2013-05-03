from urllib2 import urlopen
from json import loads
import codecs, sys
import os 

sys.stdout = codecs.getwriter('UTF-8')(sys.stdout)

try:
    os.remove("output.txt")
except OSError:
    pass

def call_the_articles():
    
    url = "http://api.nytimes.com/svc/books/v2/lists/2010-10-01/trade-fiction-paperback?&offset=&sortby=&sortorder=&api-key=1ddfd825a1084dbe50334ad25dd5ddfa:2:67632807"
    # url = "http://api.nytimes.com/svc/books/v2/lists/best-sellers/history.json?title=pioneer&api-key=1ddfd825a1084dbe50334ad25dd5ddfa:2:67632807"
    # url = "http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/30.json?&offset=%s&api-key=a1f2de9c74a24d2cf3f72d910ff68018:14:61296924"
    return loads(urlopen(url).read())

articles = call_the_articles()
g = ""

f = codecs.open('output.txt', 'w', encoding='utf-8')
for story in articles["results"]:
    # f.write(story["title"] + "\n")
    for book in story["book_details"]: 
        try:
            # g = g + story["title"] + "\n"
            g = g + book["title"] + "\n"
        except:
            g = g + " \n"
f.close()
print g



	# try:
	# 	p = Page.objects.get(pk=page_id)
	# except:
	# 	raise Http404