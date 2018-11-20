# -*- coding: utf-8 -*-
import scrapy
from first_demo.items import FirstDemoItem


class TeacherSpider(scrapy.Spider):
    name = 'teacher'
    allowed_domains = ['itsource.cn']
    start_urls = ['http://itsource.cn/']

    def parse(self, response):
        # file_name = 'teacher.html'
        # open(file_name, 'w', encoding='utf-8').write(response.text)
        for teacher in response.xpath('//ul[@id="list_detail"]/li'):
            teacher_name = teacher.xpath('.//span[2]/text()').extract()
            introduction = teacher.xpath('.//p[2]/text()').extract()
            maxim = teacher.xpath('.//p[5]/text()').extract()
            item = FirstDemoItem()
            item['teacher_name'] = teacher_name[0]
            item['introduction'] = introduction[0]
            item['maxim'] = maxim[0]
            print(item)
            yield item
