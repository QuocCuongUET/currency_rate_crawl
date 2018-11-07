import scrapy
from items import CurrencyRateItem
from currency_id import detectCurrencyId
from datetime import datetime, timedelta

class BankIndonesiaSpider(scrapy.Spider):
    name = 'bank_indonesia'

    BASED_CURRENCY_ID_IND = 3
    WEB_DATE_FORMAT = '%d %B %Y'
    DB_DATE_FORMAT  = '%Y%m%d'


    def start_requests(self):
		url = 'https://www.bi.go.id/en/moneter/informasi-kurs/transaksi-bi/Default.aspx'
		yield scrapy.Request(url, self.parse)


    def parse(self, response):

        # Get date of crawl
        transfer_date = response.css('span#ctl00_PlaceHolderMain_biWebKursTransaksiBI_lblUpdate::text').extract_first()

        # Get table contain data
        table = response.css('table#ctl00_PlaceHolderMain_biWebKursTransaksiBI_GridView2')

        for tr in table.css('tr'):

            td = tr.css('td::text')

            if td:

                item = self.createCurrencyRateItem(td, transfer_date)

                yield item



    def createCurrencyRateItem(self, data, transfer_date):

        transfer_currency_symbol = data[0].extract().strip()

        number_of_item = float(data[1].extract())

        price_of_sell  = self.formatPriceToFloat(data[2].extract())

        price_of_buy   = self.formatPriceToFloat(data[3].extract())


        item = CurrencyRateItem()

        item['transfer_date']               = self.formatTransferDate(transfer_date)

        item['based_currency_id']           = self.BASED_CURRENCY_ID_IND

        item['transfer_currency_id']        = detectCurrencyId(transfer_currency_symbol)

        item['rate_currency_transfer']      = self.calculateRateTransfer(price_of_sell, price_of_buy, number_of_item)

        item['rate_tax_currency_transfer']  = 0

        item['update_user_id']              = 0

        item['created_at']                  = datetime.now()


        return item


    def formatTransferDate(self, date):
        date = datetime.strptime(date, self.WEB_DATE_FORMAT)
        return datetime.strftime(date, self.DB_DATE_FORMAT)


    def calculateRateTransfer(self, price_of_sell, price_of_buy, number_of_item):
        rate_currency_transfer =  (price_of_sell + price_of_buy) / (2 * number_of_item)

        return round(rate_currency_transfer, 6)


    def formatPriceToFloat(self, str):

        # Format string is same 932,485,392.983
        rate_currency_transfer = str.replace(',', '')

        return float(rate_currency_transfer)

