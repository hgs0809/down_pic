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
	for url in response.xpath("//li[@class='next next_page']/a/@href").extract():
		all_url = "http://www.dbmeinv.com" + url
		yield scrapy.Request(all_url)
	item = DownPicItem()
	item['image_url'] = response.xpath("//img/@src").extract()
	yield item
	#for link in response.xpath("//img/@src"):
	#	item['image_url'] = link.extract()
	#	yield item
	

#response.xpath("//img/@src").extract()
#<li class="next next_page"><a href="/?pager_offset=3" title="下一页">下一页 &#8594;</a></li>

