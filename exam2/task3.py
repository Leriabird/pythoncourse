__author__ = 'Leria'

import xml.etree.ElementTree as ET
import urllib2
import requests
import lxml

url = "http://string-db.org/api/psi-mi/interactions?identifier=APP&required_score=800&limit=5"
s = urllib2.urlopen(url)
contents = s.read()

contents = contents.split("\n")
contents[1] = "<entrySet level=\"2\" version=\"5\">"
contents = "\n".join(contents)

file = open("first_hundred_string_app1.xml", 'w')
file.write(contents)
file.close()
tree = ET.parse('first_hundred_string_app1.xml')
root = tree.getroot()
print(root)