# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from proxyCrawler.db import MongoDB

class ProxycrawlerPipeline(object):
    collection_name = 'ip_proxies'

    def open_spider(self, spider):
        self.db = MongoDB()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        self.db.db[self.collection_name].update_one({'ip': item.get('ip')}, {'$setOnInsert': dict(item)}, upsert=True)
        return item

