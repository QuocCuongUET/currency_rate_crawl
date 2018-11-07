# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging

# from spiders.bank_indonesia_spider import BankIndonesiaSpider

# TO_CRAWL = [BankIndonesiaSpider]

# configure_logging()
# runner = CrawlerRunner()

# @defer.inlineCallbacks

# def crawl():
#     for spider in TO_CRAWL:
#         yield runner.crawl(spider)

#     reactor.stop()

# crawl()
# reactor.run() # the script will block here until the last crawl call is finished




import scrapy
from scrapy.crawler import CrawlerProcess
from spiders.bank_indonesia_spider import BankIndonesiaSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(BankIndonesiaSpider)
process.start() # the script will block here until the crawling is finished