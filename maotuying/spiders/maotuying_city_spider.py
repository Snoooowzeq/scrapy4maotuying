# -*- coding: utf-8 -*-
import scrapy
from maotuying.items import MaotuyingCityItem


class MaotuyingSpiderSpider(scrapy.Spider):
    name = 'maotuying_city_spider'
    allowed_domains = ['www.tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/TourismChildrenAjax?geo=294211&offset=0&desktop=true']
    count = 0

    def parse(self, response):
        self.count += 1
        city_list = response.xpath("//a[@class='popularCity hoverHighlight']")
        for i_item in city_list:
            city_url = i_item.xpath(".//@href").extract_first()
            yield scrapy.Request("https://www.tripadvisor.cn" + city_url, callback=self.parse_city_detail)
        if self.count <= 211:
            yield scrapy.Request(
                "https://www.tripadvisor.cn/TourismChildrenAjax?geo=294211&offset=" + str(self.count) + "&desktop=true",
                callback=self.parse)

    def parse_city_detail(self, response):
        maotuying_city_item = MaotuyingCityItem()
        maotuying_city_item['city_name'] = response.xpath("//div[@class='pageHeading']/h1/text()").extract_first()
        maotuying_city_item['city_id'] = response.xpath("//li[@class='hotels twoLines']/a/@href").extract_first().split('-')[1]
        maotuying_city_item['province'] = response.xpath("//ul[@class='breadcrumbs']//li[3]//text()").extract_first()
        maotuying_city_item['hotel_num'] = response.xpath("//a[@data-trk='hotels_nav']//span[@class='typeQty']/text()").extract_first()
        maotuying_city_item['comment_num'] = response.xpath("//a[@data-trk='hotels_nav']//span[@class='contentCount']/text()").extract_first()
        yield maotuying_city_item