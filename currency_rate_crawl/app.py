from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from spiders.bank_indonesia_spider import BankIndonesiaSpider

TO_CRAWL = [BankIndonesiaSpider]

settings = get_project_settings()
configure_logging()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks

def crawl():
    for spider in TO_CRAWL:
        yield runner.crawl(spider)

    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
