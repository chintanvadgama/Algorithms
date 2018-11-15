import sys,os,requests,urllib2
from bs4 import BeautifulSoup,SoupStrainer
from pprint import pprint
# try:
#     file_path = sys.argv[1]
# except:
#     print("Usage: python download_links.py <file_path>")
#     sys.exit(1)


def get_links(link):
    links = []
    response = urllib2.urlopen(link)
    html = BeautifulSoup(response,'html.parser',parse_only=SoupStrainer('a'))
    for link in html:
        if link.has_attr('href') and link.has_attr('target'):
            if link['target'] == '_blank':
                links.append(link['href'])
    return links


if __name__ == '__main__':
    web_links = get_links("https://www.geeksforgeeks.org/operating-systems/")
    for wl in web_links:
        fname = wl.split('/')[-2] + '.html'
        try:
            wl_content = requests.get(wl).content
        except: continue
        with open(fname,'w') as fp:
            fp.write(wl_content)
