import datetime
import scrapy

class CoinExSpider(scrapy.Spider):
    name = "coinex"
    start_urls = [
        'https://www.coinex.com/mining'
    ]

    def parse(self, response):
        span_content_list = response.xpath('//span/text()').extract()
        # get data fields that we need
        mined_yesterday = span_content_list[-5].split(' ')[0]
        qualified_dividend = span_content_list[-3].split(' ')[0]
        total_locked = span_content_list[-1].split(' ')[0]

        #print(mined_yesterday)
        #print(qualified_dividend)
        #print(total_locked)

        # get data and time
        now = datetime.datetime.now()
        self.appendToFile(str(now),
                     mined_yesterday,
                     qualified_dividend,
                     total_locked)

    def appendToFile(self, now, mined, dividend, locked):
        with open('coinexdata.txt', 'a') as f:
            f.write(now + '\t' + mined + '\t' + dividend + '\t' + locked + '\n')
            f.close()

    
