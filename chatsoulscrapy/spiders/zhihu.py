import scrapy


class ZhihuSpider(scrapy.Spider):
    name = "zhihu"
    allowed_domains = ["www.zhihu.com"]
    # start_urls = ["http://www.zhihu.com/"]
    start_urls = ["https://www.zhihu.com/column/c_1272930684131704832"]

    def parse(self, response):
        pass
