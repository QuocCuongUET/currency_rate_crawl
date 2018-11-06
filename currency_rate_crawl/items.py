# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CurrencyRateItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    transfer_date              = scrapy.Field()
    based_currency_id          = scrapy.Field()
    transfer_currency_id       = scrapy.Field()
    rate_currency_transfer     = scrapy.Field()
    rate_tax_currency_transfer = scrapy.Field()
    update_user_id             = scrapy.Field()
