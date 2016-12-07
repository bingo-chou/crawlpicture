# crawlpicture
---------

## 功能：

利用ｓｃｒａｐｙ框架抓取某站所有图片，全站图片共２００１２张（大约３.1G）。下载的图片将保存在项目根目录的ｉｍｇｓ文件夹下

--------

## 三方库：
1. ｓｃｒａｐｙ:用于爬取图片链接，标题等信息
2. ｒｅｑｕｅｓｔｓ:用于最后请求图片链接

--------

## 用法:

1. 安装ｓｃｒａｐｙ框架：pip -i https://pypi.tuna.tsinghua.edu.cn/simple scrapy

2. 安装ｒｅｑｕｅｓｔｓ库: pip -i https://pypi.tuna.tsinghua.edu.cn/simple requests

3. cd到项目根目录，然后:scrapy crawl crawlpicture

