import threading
from queue import Queue
from general import *
from domain import *
from spider import Spider


HOMEPAGE = input('Enter the homepage of the website you want to crawl\n')
DOMAIN_NAME = get_domain(HOMEPAGE)
PROJECT_NAME = DOMAIN_NAME.replace('.', '_')
print(PROJECT_NAME)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWALED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(project_name=PROJECT_NAME, base_url=HOMEPAGE, domain_name=DOMAIN_NAME)


# Worker thread, die when the main thread exist.
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Performs the nex job in the queue.


def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.currentThread().name, url)
        queue.task_done()


def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()

# Check if there are items in the queue, if so crawl them


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links are in the queue')
        create_jobs()


create_workers()
crawl()
