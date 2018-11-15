import sys, urllib2, threading, time
from Queue import Queue
from bs4 import BeautifulSoup,SoupStrainer


BASE_URL = 'https://www.glassdoor.com/Reviews/san-jose-reviews-SRCH_IL.0,8_IM761'
SF_URL = 'https://www.glassdoor.com/Reviews/san-francisco-reviews-SRCH_IL.0,13_IM759'
global_links = []


def get_links(link):
    links = []
    hdr = {'User-Agent': 'Mozilla/5.0'}
    r = urllib2.Request(link,headers=hdr)
    response = urllib2.urlopen(r)
    soup = BeautifulSoup(response,'html.parser',parse_only=SoupStrainer('span'))
    for link in soup:
        wl = link.findAll('span',{"class":"url"})
        if wl:
            links.append(wl[0].string)
    return links


class URLBuilder(threading.Thread):
    def __init__(self, url=BASE_URL, pages=10):
        threading.Thread.__init__(self)
        self.urls = []
        self.url = url
        self.pages = pages

    def build_urls(self):
        for page in range(1,self.pages):
            burl = self.url + '_IP%s.htm' % page
            self.urls.append(burl)

    def run(self):
        self.build_urls()


class GetLinks(threading.Thread):
    def __init__(self,page_url):
        threading.Thread.__init__(self)
        self.page_url = page_url

    def get_links(self):
        links = []
        hdr = {
            'User-Agent': 'Mozilla/5.0'
            }
        r = urllib2.Request(self.page_url, headers=hdr)
        response = urllib2.urlopen(r)
        soup = BeautifulSoup(response, 'html.parser', parse_only=SoupStrainer('span'))
        for link in soup:
            wl = link.findAll('span', {
                "class": "url"
                })
            if wl:
                links.append(wl[0].string)
        return links

    def run(self):
        self.get_links()


def write_links_to_file(links):
    with open('companies_list.txt','a') as fp:
        fp.write(str(links) + '\n')


class DownloadWorker(threading.Thread):
    def __init__(self, queue,file_name='glassdoor_sj_companies.txt'):
        threading.Thread.__init__(self)
        self.queue = queue
        self.file_name = file_name

    def run(self):
        while True:
            link = self.queue.get()
            try:
                print("Getting Links of webpage : (%s) " % link)
                links = get_links(link)
                with open(self.file_name, 'a') as fp:
                    for l in links:
                        fp.write("%s\n" % l)
            finally:
                self.queue.task_done()


if __name__ == '__main__':
    start = time.time()
    # 1. Initialize URL Builder and get all urls
    urlb = URLBuilder(SF_URL, pages=1962)
    urlb.build_urls()
    # 2. Create a queue to put all the urls in queue
    queue = Queue()
    for x in range(10):
        worker = DownloadWorker(queue, file_name='sf_companies.txt')
        worker.Daemon = True
        worker.start()

    # 3. Update queue
    for url in urlb.urls:
        # logging.INFO("Queueing url : (%s)" % url)
        print("Queueing URL: (%s) " % url)
        queue.put(url)
    queue.join()
    print("Time Taken:", time.time() - start)
    sys.exit(0)