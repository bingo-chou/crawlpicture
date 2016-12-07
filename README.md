# crawlpicture
---------

## 功能：

利用scrapy框架抓取某站所有图片，全站图片共20012张（大约3.1G）。下载的图片将保存在项目根目录的imgs文件夹下

--------

## 三方库：
1. scrapy:用于爬取图片链接，标题等信息
2. requests:用于最后请求图片链接

--------

## 用法:

1. 安装scrapy框架：pip -i https://pypi.tuna.tsinghua.edu.cn/simple install scrapy

2. 安装requests库: pip -i https://pypi.tuna.tsinghua.edu.cn/simple install requests

3. cd到项目根目录，然后:scrapy crawl crawlpicture

