__author__ = 'Leria'

import re
import urllib
import requests
from lxml import etree
import _elementtree

url = 'https://twitter.com/googlefacts'
d = requests.get(url).text
root = etree.fromstring(d)
it = root.iter(<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">Sizzl, Oscar Mayer’s new dating app, pairs up singles based on their love of bacon.</p>)







# url = "http://string-db.org/api/psi-mi/interactions?identifier=APP&required_score=800&limit=5"
# s = urllib2.urlopen(url)
# contents = s.read()
#
# contents = contents.split("\n")
# contents[1] = "<entrySet level=\"2\" version=\"5\">"
# contents = "\n".join(contents)
#
# file = open("first_hundred_string_app1.xml", 'w')
# file.write(contents)
# file.close()
# tree = ET.parse('first_hundred_string_app1.xml')
# root = tree.getroot()
# print(root)