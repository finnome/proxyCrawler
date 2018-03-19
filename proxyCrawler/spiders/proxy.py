# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from proxyCrawler.items import ProxycrawlerItem
import telnetlib


class ProxySpider(scrapy.Spider):
    name = 'proxy'
    allowed_domains = ['http://www.xicidaili.com/']
    start_urls = ['http://www.xicidaili.com/']

    def parse(self, response):
        sel = Selector(response)
        tr_list = sel.xpath('//table[@id="ip_list"]/tr')
        for i in range(2, len(tr_list)):
            cells = tr_list[i].xpath('td')
            if len(cells) <= 0: continue
            origin_ip = cells[1].xpath('text()').extract()[0]
            port = cells[2].xpath('text()').extract()[0]
            type = cells[5].xpath('text()').extract()[0].lower()
            ip = type + '://' + origin_ip + ':' + port
            # 只爬取http、https代理
            if type == 'http' or type == 'https':
                item = ProxycrawlerItem()
                item['ip'] = ip
                item['port'] = port
                item['type'] = type
                item['origin_ip'] = origin_ip
                # 验证ip是否可用
                if self.telnet(item):
                    yield item

    def telnet(self, item):
        try:
            telnetlib.Telnet(item['origin_ip'], port=item['port'], timeout=10.0)
        except:
            print('connect failure')
            return False
        else:
            print('conncet success')
            return True
