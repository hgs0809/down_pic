# -*- coding: utf-8 -*-
import scrapy
from down_pic.items import DownPicItem


class PicSpider(scrapy.Spider):
    name = "pic"
    allowed_domains = ["dbmeinv.com"]
    start_urls = (
        'http://www.dbmeinv.com/',
    )

    def parse(self, response):
	item = DownPicItem()
	item['image_url'] = response.xpath("//img/@src").extract()
	return item
	#for link in response.xpath("//img/@src"):
	#	item['image_url'] = link.extract()
	#	yield item
	

#response.xpath("//img/@src").extract()
