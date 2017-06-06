import requests #this is used for the internet to find a page
import random #used to find a random link on a wikipedia page to use for input
import math
import re #this is regex, and it is used to find strings not involved in our search engine, like special characters
import os #used to save files and open/create new ones
import glob #used to find, recursively, every file in a certain folder
from bs4 import BeautifulSoup #used to prettify the input pages

NUMPAGES = 9 #number of input pages
urlEnding = "/wiki/Leather"  #THIS IS OUR STARTING WIKIPEDIA QUERY. YOU CAN CHANGE THIS TO ANY WIKIPEDIA LINK TO SEARCH FOR PARTICULAR TOPICS

stop_words = ["a","about","above","across","after","against","along","among","and", "around", 
	"at","before","behind","between","beyond","but","by","concerning","despite","down","during","including",
	"except","few","following","for","from","he","he","her","him","i","in","into","it","like","me","near","of",
	"off","on","one","out","over","plus","she","since","some","them","the","they",
	"through","throughout","to","towards","under","until","up","upon","us","we","with","within","without","you"]

files = glob.glob('inputs/*') #we recurse through every file in the folder "inputs"
for f in files:
	os.remove(f) #we delete any preexisting files in the folder "inputs"


valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_/") #we need to format the input pages, so we clean the HTML files by only allowing alphanumerical characters along with underscores and slashes
string1 = 'a href' #we know that links are contained after the words "a href"
string2 = '"' #we look for the ending index of the next link
previousURLs = [] #we make sure not to crawl pages we have already crawled
previousURLs.append(urlEnding)
url = "https://en.wikipedia.org" + urlEnding #we scavenge this file
print(urlEnding)
page = requests.get(url)
contents = page.content
soup = BeautifulSoup(contents, 'html.parser')
soup = soup.prettify("utf-8")
new_string = re.sub('[^a-zA-Z0-9\n]', ' ', soup).split()
resultwords = [word for word in new_string if word.lower() not in stop_words] #this makes sure we are using valid inputs for our C++ search program
resultwords = ' '.join(resultwords)
file = open("inputs/input1.txt","w") #we write the string to an input page
file.write(resultwords) 
file.close()
for integer in range(2,NUMPAGES+1): #we then continue this process over the next n-1 pages
	urlString = "#"
	while (not (set(urlString) <= valid_chars)):
		randomDecimal = random.uniform(0,0.8) #this random number is used to find a random link between the start of the page and 80% through the page
		index = int(math.floor(randomDecimal*len(contents)))
		x = contents.find(string1, index)
		y = contents.find(string2, x+len(string1)+3) #this allows us to find a random link in our current wikipedia page
		urlString = contents[x+len(string1)+2:y]
		urlString = urlString.replace(" ", "_")
		if (set(urlString) <= valid_chars and (urlString not in previousURLs)):
			print(urlString)

	url = "https://en.wikipedia.org" + urlString #this block is the same as the one before the loop; we simply scavenge through the link and ready it for parsing into the input pages used for our C++ search engine
	previousURLs.append(urlString);
	page2 = requests.get(url)
	contents = page2.content
	soup = BeautifulSoup(contents, 'html.parser')
	soup = soup.prettify("utf-8")
	new_string = re.sub('[^a-zA-Z0-9\n]', ' ', soup).split()
	resultwords = [word for word in new_string if word.lower() not in stop_words]
	resultwords = ' '.join(resultwords)
	file = open("inputs/input" + str(integer) + ".txt","w") 
	file.write(resultwords) 
	file.close()

