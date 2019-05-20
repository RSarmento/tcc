# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    processo = scrapy.Field()
    orgao = scrapy.Field()
    publicacao = scrapy.Field()
    julgador = scrapy.Field()
    relator = scrapy.Field()
    elementos = scrapy.Field()
