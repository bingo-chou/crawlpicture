#!/usr/bin/env python
# -*- coding:utf-8 -*-

from scrapy.spiders import CrawlSpider,Rule
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader,Identity
from scrapy.linkextractors import LinkExtractor
from crawlpicture.items import CrawlpictureItem

class CrawlpictureSpider(CrawlSpider):
	name='crawlpicture'
	
	start_urls=[
		'http://www.meizitu.com/a/list_1_1.html',
	]
	
	
	rules=(
		Rule(LinkExtractor(allow=('http://www.meizitu.com/a/list_\d+_\d+\.html',)),callback='parse_list',follow=True),
		Rule(LinkExtractor(allow=('http://www.meizitu.com/a/\d+\.html',)),callback='parse_item',follow=True),
	)
	
	#处理图片列表页面，获取图片详细页面的url和列表页面的下一页
	def parse_list(self,response):
		image_urls=response.css('li.wp-item')
		for image_url in image_urls:
			url=image_url.xpath('div/div/a/@href').extract_first()
			yield Request(response.urljoin(url),callback=self.parse_item)
		numli=response.css('div#wp_page_numbers ul li')[-2]
		tag=True if numli.xpath('a/text()').extract_first()==u'\u4e0b\u4e00\u9875' else False
		
		if tag:
			next_page=response.urljoin(numli.xpath('a/@href').extract_first())
			yield Request(next_page,callback=self.parse_list)

	#处理图片详细页面
	def parse_item(self,response):
		l=ItemLoader(item=CrawlpictureItem(),response=response)
		l.add_xpath('name','//h2/a/text()')
		l.add_css('tags','div.metaRight p::text')
		#l.add_xpath('image_urls','//div[@id="picture"]/p/img/@src' or '//img[@class="scrollLoading"]/@src',Identity())
		l.add_css('image_urls','div.postContent img::attr(src)',Identity())
		l.add_value('url',response.url)
		return l.load_item()		
		
	
	
