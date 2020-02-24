import scrapy


class CatalogueSpider(scrapy.Spider):
    name = 'catalogue'
    start_urls = ['https://www.urparts.com/index.cfm/page/catalogue']
    url_level = len(start_urls[0].split('/'))
    url_set = set()
    urlRepeat = 0

    def check_if_unique(self, url):
        if url in self.url_set:
            self.urlRepeat += 1
            return False
        else:
            self.url_set.add(url)
            return True

    def parse(self, response):
        split_url = response.url.split('/')
        if len(split_url) == self.url_level:
            for manufacturer in response.css('.allmakes>ul>li>a'):
                yield response.follow(manufacturer, callback=self.parse)
        elif len(split_url) == self.url_level + 1:
            print('allcategories ' + split_url[-1])
            for model in response.css('.allcategories>ul>li>a'):
                yield response.follow(model, callback=self.parse)
        elif len(split_url) == self.url_level + 2:
            print('allcategories ' + split_url[-1])
            for model in response.css('.allmodels>ul>li>a'):
                yield response.follow(model, callback=self.parse)
        elif len(split_url) == self.url_level + 3:
            print('allparts ' + split_url[-1] + ' len: ' + str(len(split_url)))
            if self.check_if_unique(response.url):
                for part in response.css('.allparts>ul>li'):
                    split_url = [s.replace('%20', ' ') for s in split_url]
                    item = {
                        'manufacturer': split_url[6],
                        'category': split_url[7],
                        'model': split_url[8],
                        'part': part.css('a::text').get().strip(' -'),
                        'part_category': part.css('span::text').get().strip()
                    }
                    yield item
            else:

                print(str(self.urlRepeat) + ' Already been here ' + response.url)
