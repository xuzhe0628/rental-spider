import scrapy


class HaozuSpider(scrapy.Spider):
    name = "Haozu"
    start_urls = [
        'http://www.haozu.com/gz/zuxiezilou/',
    ]

    def parse(self, response):
        for quote in response.css('div.list-content'):
            yield {
                'url': ('http://www.haozu.com' +
                    quote.css('h1.h1-title a::attr("href")').extract_first()),
                'building': quote.css('h1.h1-title a::text').extract_first(),
                'price': quote.css('span.s1 i.i2::text').extract_first(),
                'price_unit': quote.css('span.s1::text').extract_first(),
            }

        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)