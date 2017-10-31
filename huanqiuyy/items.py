# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HuanqiuyyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    product_tag = scrapy.Field()
    product_point = scrapy.Field()
    product_category = scrapy.Field()
    investment_area = scrapy.Field()
    manufacture_factory = scrapy.Field()
    approval_number = scrapy.Field()
    product_specifications = scrapy.Field()
    product_ingredients = scrapy.Field()
    product_usage = scrapy.Field()
    product_pack = scrapy.Field()
    product_function = scrapy.Field()
    contact_name = scrapy.Field()
    telphone = scrapy.Field()
    fax = scrapy.Field()
    mobilephone = scrapy.Field()
    address = scrapy.Field()
    qq = scrapy.Field()
    wechat = scrapy.Field()
    mail = scrapy.Field()
