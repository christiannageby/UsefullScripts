import argparse
import urllib2
import sys

"""
This program will search a website with pagination after a specified term like a
Hyperlink or a Username(E.g @Christiannageby)
"""

#check if the url is valid and contain the index variable

def checkUrl(url):
    return True if url.find("*i*") > -1 else False

def urlBuilder(url, index):
    url = args.base_url

    # check if the index is located at the end of the url
    if url.find("*i*") == len(url) - 3:
        return url[:-3] + str(index)
    elif url.find("*i*") != -1:
       breakpoint = url.find("*i*")
       return url[:breakpoint] + str(index) + url[breakpoint+3:]
    else:
        return 0


#add all arguments required for the program to function correct
parser = argparse.ArgumentParser()
parser.add_argument("-base-url", help="The url where the index(for pagination) is replaced with *i*")
parser.add_argument("-min-index", help="the minimum value the index will be", type=int)
parser.add_argument("-max-index", help="the max value the index-variable can be", type=int)
parser.add_argument("-search-term", help="what to search for")

args = parser.parse_args()

if checkUrl(args.base_url) != True:
    sys.exit("The Specified url did not contain a escape character for index")

#dataset with results
urls = []
#search though all indexes specified by user
for i in range(args.min_index, args.max_index):

    data = str(urllib2.urlopen(urlBuilder(args.base_url, i)).read())
    if data.find(str(args.search_term)) != -1:
        urls.append(urlBuilder(args.base_url, i))

sys.stdout.write("Found {} pages containing {}\n".format(len(urls), args.search_term))
for url in urls:
    print url