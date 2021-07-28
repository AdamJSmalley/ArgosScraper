import scrapy
from scrapy.spiders import SitemapSpider

class sitemap(SitemapSpider):
    name = 'sitemap' #the name that you need to run the spider from the command line.
    table = 'prices_v1' #the MySQL table to insert the data into
    primary_key = 'URL'
    sitemap_urls = ['https://www.argos.co.uk/product.xml', 'https://www.argos.co.uk/product2.xml'] #the urls of the two sitemaps that contain links to all of argos's products

    def parse(self, response):
        PRICE_SELECTOR = ".price ::attr(content)" #the css selector to find price on the product page
        CATEGORY_SELECTOR = "//li[contains(@class,'breadcrumb__item')]/a/span/text()" #the xpath selector to find all the categories of the product
        NAME_SELECTOR = "//li[contains(@class,'breadcrumb__item')]/span/span/text()" #the xpath selector to find the name of the product

        categories = response.xpath(CATEGORY_SELECTOR).getall()

        yield { #scrape the data from the product page
            'URL' : response.url, #scrape the product url from the response object
            'Price' : response.css(PRICE_SELECTOR).get(),
            'Name' : response.xpath(NAME_SELECTOR).get(),
            'Category1' : categories[0],
            'Category2' : categories[1],
            'Category3' : categories[2]
        }