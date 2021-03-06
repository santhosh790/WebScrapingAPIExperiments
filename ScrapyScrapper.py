import scrapy


class w3SchoolSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.w3schools.com/css/default.asp']

    def parse(self, response):
        next_page = response.css('.w3-btn w3-blue').extract()

        yield response.follow(next_page, self.parse)


'''
Notes:
https://scrapy.org/
https://stackoverflow.com/questions/16391677/how-to-send-javascript-and-cookies-enabled-in-scrapy
https://docs.scrapy.org/en/latest/index.html
'''