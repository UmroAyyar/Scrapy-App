# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Bookscraper2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def serialize_price(value):
    return f'£ {str(value)}'

class BookItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    product_type = scrapy.Field()
    price_exc_tax = scrapy.Field()
    Price_inc_tax = scrapy.Field()
    Tax = scrapy.Field()
    availability = scrapy.Field()
    reviews = scrapy.Field()
    stars = scrapy.Field()
    catagory = scrapy.Field()
    Description = scrapy.Field()
    price = scrapy.Field()
