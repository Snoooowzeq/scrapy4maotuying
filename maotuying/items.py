# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaotuyingCityItem(scrapy.Item):
    # define the fields for your item here like:
    #name = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    province = scrapy.Field()
    hotel_num = scrapy.Field()
    comment_num = scrapy.Field()

class MaotuyingHotelItem(scrapy.Item):
    hotel_id = scrapy.Field()
    hotel_ch_name = scrapy.Field()
    hotel_en_name = scrapy.Field()
    price = scrapy.Field()
    price_website = scrapy.Field()
    ranking = scrapy.Field()
    comment_num = scrapy.Field()
    rating = scrapy.Field()
    address = scrapy.Field()
    photo_num = scrapy.Field()
    hotel_character = scrapy.Field()
    stars = scrapy.Field()
    award = scrapy.Field()
    info = scrapy.Field()

class MaotuyingItem(scrapy.Item):
    hotel_name = scrapy.Field()
    comment = scrapy.Field()
    comment_num = scrapy.Field()
    introduce = scrapy.Field()