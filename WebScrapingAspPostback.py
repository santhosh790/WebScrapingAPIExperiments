import mechanicalsoup as ms


def select_form_method():
    br = ms.StatefulBrowser()

    br.open('http://quotes.toscrape.com/search.aspx')

    br.select_form('form[action ="/filter.aspx"]')

    br['author'] = 'Albert Einstein'

    res = br.submit_selected()

    print(br.get_url())
    print(res.status_code)
    br.select_form('form[action ="/filter.aspx"]')
    br['tag'] = 'deep-thoughts'

    res2 = br.submit_selected()

    print(br.get_url())
    print(res2.status_code)

    #print(res2.text)

    page = br.get_current_page()
    vals = page.find("div", class_="quote")
    print(vals)
    print(vals.find('span', class_='content').text)


def new_form_method():

    br = ms.StatefulBrowser()
    page = br.get('http://quotes.toscrape.com/search.aspx')

    form1 = ms.Form(page.soup.form)
    form1.set_select({'author':'Albert Einstein'})

    resp = br.submit(form=form1, url='http://quotes.toscrape.com/filterings.aspx')
    print(resp.status_code)

    ## Here browser will not have any form element

    form2 = ms.Form(resp.soup.form)
    form2.set_select({'tag':'deep-thoughts'})
    resp = br.submit(form=form2, url='http://quotes.toscrape.com/filter.aspx')

    print(resp.status_code)
    print(resp.text)

new_form_method()

'''

Another easier scrapper for aspx pages::
https://medium.com/@simranpandey97/web-scraper-for-aspx-form-based-webpages-b8828085e4a2
http://toddhayton.com/2014/12/08/form-handling-with-mechanize-and-beautifulsoup/

To try- https://stackoverflow.com/questions/28974838/crawling-through-pages-with-postback-data-javascript-python-scrapy


https://blog.scrapinghub.com/2016/04/20/scrapy-tips-from-the-pros-april-2016-edition
import scrapy
class SpidyQuotesViewStateSpider(scrapy.Spider):
    name = 'spidyquotes-viewstate'
    start_urls = ['http://quotes.toscrape.com/search.aspx']
    download_delay = 1.5

    def parse(self, response):
        for author in response.css('select#author > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': author,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_tags
            )

    def parse_tags(self, response):
        for tag in response.css('select#tag > option ::attr(value)').extract():
            yield scrapy.FormRequest(
                'http://quotes.toscrape.com/filter.aspx',
                formdata={
                    'author': response.css(
                        'select#author > option[selected] ::attr(value)'
                    ).extract_first(),
                    'tag': tag,
                    '__VIEWSTATE': response.css('input#__VIEWSTATE::attr(value)').extract_first()
                },
                callback=self.parse_results,
            )

    def parse_results(self, response):
        for quote in response.css("div.quote"):
            yield {
                'quote': quote.css('span.content ::text').extract_first(),
                'author': quote.css('span.author ::text').extract_first(),
                'tag': quote.css('span.tag ::text').extract_first(),
            }

'''