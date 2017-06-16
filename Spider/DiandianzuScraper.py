import scrapy


class DiandianzuSpider(scrapy.Spider):
    name = "Diandianzu"
    start_urls = [
        'http://gz.diandianzu.com/listing/',
    ]

    def parse(self, response):
        for quote in response.css('div.part1.clearfix'):
            yield {
                'url': ('http://gz.diandianzu.com' + 
                    quote.css('a::attr("href")').extract_first()),
                'building': quote.css('a::text').extract_first(),
                'price': quote.css('span.price-num::text').extract_first(),
                'price_unit': quote.css('span.price-unit::text').extract_first(),
                'price_text': quote.css ('span.price-txt::text').extract_first(),
            }

        next_page = response.css('a.next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)