# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
# 这个网页是用来筛选想要的数据的
import scrapy


class FirstDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    teacher_name = scrapy.Field()
    introduction = scrapy.Field()
    maxim = scrapy.Field()


if __name__ == '__main__':
    item = FirstDemoItem()
    # item = dict()
    item['teacher_name'] = 6666
    print(item)
