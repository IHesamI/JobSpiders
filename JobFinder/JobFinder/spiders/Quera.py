import scrapy
class Quera(scrapy.Spider):
    name='Quera'
    def start_requests(self):
        baseUrl='https://quera.org/magnet/jobs'
        urls=[baseUrl+'?page=%s'%(i) for i in range(1,13)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def  parse(self, response):
        titles=response.xpath('//a[has-class("chakra-link","css-spn4bz")]/span/text()').getall()
        for title in titles:
            title=title+'\n'
            with open(self.name+'.csv','a',encoding="utf-8") as File:
                File.write(title)
        self.log(self.name+' Crawled')

        
