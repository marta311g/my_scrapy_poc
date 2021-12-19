import scrapy


class PoCSpider(scrapy.Spider):
    name = 'poc'
    start_urls = [
        'https://github.com/wRAR?tab=repositories',
    ]

    def parse(self, response):
        for prog_lang in response.xpath('//span[@itemprop=$val]/text()', val="programmingLanguage").getall():
            yield {
                "lang": prog_lang
            }
        
        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)