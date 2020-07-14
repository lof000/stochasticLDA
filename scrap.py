import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://arxiv.org/search/?query=database&searchtype=all&abstracts=show&order=-announced_date_first&size=50']

    def parse(self, response):
        for title in response.css('.abstract-short'):
            yield {'title': title.css('::text').get()}

        #for next_page in response.css('a.next-posts-link'):
        #    yield response.follow(next_page, self.parse)