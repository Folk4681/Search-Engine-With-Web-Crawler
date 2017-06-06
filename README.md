# Search-Engine-With-Web-Crawler
Python web crawler with a C++ search engine - Vighnesh Souda.

Be sure to install BeautifulSoup4 for Python 2.7.
1. First, you need to specify the number of input pages. This is denoted by the variable
“NUMPAGES” in webCrawler.py. This variable MUST be the same value as
“NUM_INPUT_PAGES” located at the top of the “test.cpp” file.
2. Next, you need to choose a topic to initially query the webCrawler. This must be a valid
page in the Wikipedia database, like “Math” or “United_States” or “Cuisine”.
3. Next, in the project workspace, run “python webCrawler.py” in a terminal. There should
not be any issues.
4. Next, in the project workspace, in a terminal, run “g++ test.cpp -o out -std=c++11”. Note:
this will most likely not work on Windows. It is very important that you include the flag
“std=c++11”. After doing so, you should see a file called “out” in the project directory.
5. In the same terminal, run ./out. The program should run with no problem, and you should
see a request to query the trie.

## Ubuntu
```
$ git clone https://github.com/vsouda/Search-Engine-With-Web-Crawler.git
$ cd Search-Engine-With-Web-Crawler/src/
$ python webCrawler.py
$ g++ test.cpp -o out -std=c++11
$ ./out
```


## Sample Outputs
![alt_text](https://puu.sh/wcgar/9e89fe4313.png)
![alt text](https://puu.sh/wcgbo/e4eaac8be2.png)
![alt text](https://puu.sh/wcfZ5/f51801a162.png)
