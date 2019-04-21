from scrapy import cmdline
cmdline.execute('scrapy crawl maotuying_spider -o maotuying_comment.csv'.split())
cmdline.execute('scrapy crawl maotuying_city_spider -o maotuying_city.csv'.split())
cmdline.execute('scrapy crawl maotuying_hotel_spider -o maotuying_hotels.csv'.split())