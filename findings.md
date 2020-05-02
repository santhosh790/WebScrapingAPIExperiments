Webscraping
==========

*Scraping is rendering the HTML content through code and retrieve the required information*.

Scraping the static HTML page is straightforward. Just hit the url and read the content. When it comes to reading
the dynamic or pages with form elements that requires filling and submitting, it becomes tricky. There are set of
modules to do this task.

1. Mechanize
2. MechanicalSoup
3. Scrapy
4. Selenium, etc.,

I've implemented mechanize, mechanicalsoup and scrapy in this repository for dynamic content retrieval from the
websites.

Mechanize uses urllib2 to connect and retrieve the data. It is one of the old webscrapping tool available in python

MechanicalSoup is new API which is similar to Mechanize API. It has new features like Stateful Browser. It is using
requests, BeautifulSoup internally. Understanding beautifulsoup makes
work simpler. There is a minimal documentation from the team itself:
https://mechanicalsoup.readthedocs.io/en/stable/index.html
**Mechanize and MechanicalSoup** don't support javascript. 

Scrapy is one of the powerful crawling tool. It can crawl the dynamic website through Scrapy's Spider.
This is basically for large scale web scrapping. Basically, it's a command line tool.

We define a crawler in python that uses scrapy.Spider and use scrapy commnadline tool to run tat crawler.

It is also not supporting the javascript by default. But, we can use 
scrapy for javascript enabled sites by utilizing Splash with scrapyjs.
Look at answer (here) [https://stackoverflow.com/questions/16391677/how-to-send-javascript-and-cookies-enabled-in-scrapy]

But Scrapy is an heavier module than Mechanize and MechanicalSoup. Many number of dependencies are required for this.
When I try to install Scrapy, these were the dependent packages needed along with it.
w3lib, cssselect, lxml, parsel, pyOpenSSL, PyHamc
rest, attrs, zope.interface, hyperlink, Automat, constantly, incremental, Twiste
d, PyDispatcher, protego, pyasn1, pyasn1-modules, service-identity, queuelib, pyopenssl,
cryptography.

Conclusion:
    Based on the requirements we can decide on the tool we need.
    
1. If you wish to crawl static pages, requests and beautifulsoup are excellent tools to use.
2. If the requirement is to use and follow form elements, we can go with MechanicalSoup or mechanize even.
3. If the requirement is to use form elements along with extensive parsings, we can go with Scrapy.
4. If we need Javascript also enabled, we can go with Scrapy+Splash or selenium (Unexplored in this experiment)


Different important tools: https://analyticsindiamag.com/top-7-python-web-scraping-tools-for-data-scientists/
https://analyticsindiamag.com/top-resources-to-learn-web-scraping/