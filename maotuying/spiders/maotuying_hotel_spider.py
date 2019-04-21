# -*- coding: utf-8 -*-
import scrapy
from maotuying.items import MaotuyingHotelItem


class MaotuyingSpiderSpider(scrapy.Spider):
    name = 'maotuying_hotel_spider'
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
        hotels_url = response.xpath("//li[@class='hotels twoLines']/a/@href").extract_first()
        yield scrapy.Request("https://www.tripadvisor.cn" + hotels_url, callback=self.parse_hotel_list)


    def parse_hotel_list(self, response):
        hotel_list = response.xpath("//div[@class='listing_title']")
        for hotel_list_item in hotel_list:
            hotel_url = hotel_list_item.xpath(".//a//@href").extract_first()
            yield scrapy.Request("https://www.tripadvisor.cn" + hotel_url, callback=self.parse_hotel_detail)
        next_link = response.xpath(
            "//div[@class='unified ui_pagination standard_pagination ui_section listFooter']/a[@class='nav next taLnk ui_button primary']/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://www.tripadvisor.cn" + next_link, callback=self.parse_hotel_list)


    def parse_hotel_detail(self, response):
        hotel_item = MaotuyingHotelItem()
        hotel_item['hotel_id'] = response.xpath("//div[@class='blRow']/@data-locid").extract_first()
        hotel_item['hotel_ch_name'] = response.xpath("//h1[@id='HEADING']/text()").extract_first()
        hotel_item['hotel_en_name'] = response.xpath("//div[@class='is-hidden-mobile']/text()").extract_first()
        hotel_item['price'] = response.xpath("//div[@class='price __resizeWatch']/text()").extract_first()
        hotel_item['price_website'] = response.xpath("//img[@class='providerImg']/@alt").extract_first()
        hotel_item['ranking'] = response.xpath("//b[@class='rank']/text()").extract_first()
        hotel_item['comment_num'] = response.xpath("//span[@class='reviewCount']/text()").extract_first()
        hotel_item['rating'] = response.xpath("//span[@class='ui_bubble_rating bubble_40']/@alt").extract_first()
        hotel_item['address'] = response.xpath("//span[@class='street-address']/text()").extract_first()
        hotel_item['photo_num'] = response.xpath("//span[@class='is-hidden-tablet hotels-media-album-parts-PhotoCount__text--3OXuH']/text()").extract_first()
        hotel_item['hotel_character'] = response.xpath("//div[@class='sub_content ui_columns is-multiline is-gapless is-mobile']//text()").extract()
        hotel_item['stars'] = response.xpath("//div[@class='hotels-hotel-review-overview-HighlightedAmenities__amenityItem--3E_Yg']/div/text()").extract_first()
        hotel_item['award'] = response.xpath("//div[@class='badgeWrapper']/span/span/text()").extract_first()
        hotel_item['info'] = response.xpath("//div[@class='section_content']/div[@class='sub_content']/div[@class='textitem']/text()").extract()
        yield hotel_item