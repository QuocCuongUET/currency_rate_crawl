import scrapy

class BankIndonesiaSpider(scrapy.Spider):
	name = 'bank_indonesia'

	def start_requests(self):
		url = 'https://www.bi.go.id/en/moneter/informasi-kurs/transaksi-bi/Default.aspx'
		yield scrapy.Request(url, self.parse)

	def parse(self, response):

		# Get date of crawl
		date = response.css('span#ctl00_PlaceHolderMain_biWebKursTransaksiBI_lblUpdate::text').extract_first()
		
		# Get table contain data
		table = response.css('table#ctl00_PlaceHolderMain_biWebKursTransaksiBI_GridView2')

		for tr in table.css('tr'):

			td = tr.css('td::text')

			if td:
		
				data = {
					'Currencies' : td[0].extract(),
					'Value'      : td[1].extract(),
					'Sell'		 : td[2].extract(),
					'Buy'		 : td[3].extract(),
				}

				yield data


