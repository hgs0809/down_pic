# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class DownPicPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
	for image_url in item['image_url']:
		print image_url
		yield scrapy.Request(image_url)
    def item_completed(self, results, item, info):
	print results
	print item 
	print info

