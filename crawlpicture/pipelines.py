# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import requests
from crawlpicture import settings
import os
import csv
from crawlpicture.csvwriter import UnicodeWriter
headers={
	'Host': 'mm.howkuai.com',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    	'Accept-Language': 'en-US,en;q=0.5',
    	'Accept-Encoding': 'gzip,deflate',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
}

#记录没能正确请求的图片信息
def writeCSV(data):
	
	if not os.path.exists('error.csv'):
		csvfile=file('error.csv','ab')
		writer=UnicodeWriter(csvfile,delimiter=',')
		writer.writerow([u'图片名称',u'地址'])
		writer.writerow(data)
	else:
		csvfile=file('error.csv','ab')
		writer=UnicodeWriter(csvfile,delimiter=',')
		writer.writerow(data)
	csvfile.close()
	
class CrawlpicturePipeline(object):
    def process_item(self, item, spider):
        
	if 'image_urls' in item:
		images=[]
		dir_path='%s/%s'%(settings.IMAGES_STORE,spider.name)

		if not os.path.exists(dir_path):
			os.makedirs(dir_path)
		for image_url in item['image_urls']:
			suffix=image_url.split('/')[-1]
			image_file_name=item['name'][0]+suffix
			file_path='%s/%s'%(dir_path,image_file_name)
			images.append(file_path)
			if os.path.exists(file_path):
				continue
			response=requests.get(image_url,headers=headers,stream=True)
			#正确请求则保存图片
			if response.status_code==200:
				with open(file_path,'wb') as f:
					for block in response.iter_content(1024):
						if not block:
							break
						f.write(block)
			else:
				data=[image_file_name,image_url]
				writeCSV(data)	
					
		item['images']=images
	return item

