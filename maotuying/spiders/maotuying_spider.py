# -*- coding: utf-8 -*-
import scrapy
#from maotuying.items import MaotuyingItem


class MaotuyingSpiderSpider(scrapy.Spider):
    name = 'maotuying_spider'
    allowed_domains = ['www.tripadvisor.cn']
    start_urls = ['https://www.tripadvisor.cn/Hotels-g294212-Beijing-Hotels.html']

    def parse(self, response):
        pass
        #print(response.text)
        hotel_list = response.xpath("//div[@class='prw_rup prw_meta_hsx_responsive_listing ui_section listItem']")
        for i_item in hotel_list:
            maotuying_item = MaotuyingItem()
            maotuying_item['hotel_name'] = i_item.xpath(".//div[@class='listing_title']/a/text()").extract_first()
            maotuying_item['comment_number'] = i_item.xpath(".//div[@class='prw_rup prw_common_bubble_clickable_responsive_rating_and_review_count linespace is-shown-at-mobile']/a[2]/text()").extract_first()
            maotuying_item['comment'] = i_item.xpath(".//div[@class='reviews']//a/@title").extract_first()
            maotuying_item['introduce'] = i_item.xpath(".//div[@class='label']//text()").extract()
            print(maotuying_item)
            yield maotuying_item
        next_link = response.xpath("//div[@class='unified ui_pagination standard_pagination ui_section listFooter']/a[@class='nav next taLnk ui_button primary']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://www.tripadvisor.cn"+next_link, callback=self.parse)