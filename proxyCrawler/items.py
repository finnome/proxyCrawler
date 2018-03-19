# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxycrawlerItem(scrapy.Item):
    origin_ip = scrapy.Field()
    type = scrapy.Field()
    port = scrapy.Field()
    ip = scrapy.Field()
