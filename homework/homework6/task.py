__author__ = 'Leria'

import re
import requests
from lxml import etree

def link_finder(url):
    tree = etree.fromstring(requests.get(url).text, etree.HTMLParser())
    linky_links = [elt.attrib.get('href') for elt in tree.iter('a') if elt.attrib.get('href')]
    reg = re.compile('/wiki/')
    template = "https://en.wikipedia.org"
    start = [(template + linky_links[index[0]]) for index in enumerate(linky_links) if reg.match(linky_links[index[0]])]
    return start

def clicker(start, end, click_amount):
    if click_amount == 0:
        return None
    else:
        final_links = []
        begin = link_finder(start)
        if end in begin:
            final_links = [start, end]
        else:
            for b in begin:
                res = clicker(b, end, click_amount - 1)
                if res:
                    final_links = [start] + [res]
                    break
        return '\n'.join(final_links)


print(clicker('https://en.wikipedia.org/wiki/Gone_Maggie_Gone', 'https://en.wikipedia.org/wiki/Theia_(planet)', 2))