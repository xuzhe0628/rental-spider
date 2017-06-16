import scrapy


class KongjianjiaSpider(scrapy.Spider):
    name = "Kongjianjia"
    start_urls = [
        'http://gz.kongjianjia.com/xiezilou',
    ]

    def parse(self, response):
        for quote in response.css('div.xiangmu-top'):
            yield {
                'url': ('http://gz.kongjianjia.com' + 
                    quote.css('a::attr("href")').extract_first()),
                'building': quote.css('a::text').extract_first(),
                'price': quote.css('span.xiangmu-span1 b::text').extract_first(),
                # 'price_unit': # quote.css('span.xiangmu-span1::text').extract_first(),
            }

        next_page = response.css('a.page-next::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)