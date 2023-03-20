import scrapy
class Eeshtekhdam(scrapy.Spider):
    name='Eeshtekhdam'
    def start_requests(self):
        baseUrl='https://www.e-estekhdam.com/search/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D9%85%D8%B4%D8%A7%D8%BA%D9%84-%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1-%D9%86%D8%B1%D9%85%E2%80%8C%D8%A7%D9%81%D8%B2%D8%A7%D8%B1-IT'
        urls=[baseUrl+'?page=%s'%(i) for i in range(1,6)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def  parse(self, response):
        titles=response.css('a.title.vertical-top.display-inline::text').getall()
        # JobInfo=response.xpath('//li [@class="c-jobListView__metaItem"]/span/span/text()').getall() # TODO for more information need this field 
        print(titles)
        for title in titles:
        #     title=title.replace('\n','')
        #     title=re.sub(r'\s{2,}','',title)
            title=title+'\n'
        #     print(title)
            with open(self.name+'.csv','a',encoding="utf-8") as jobinjaFile:
                jobinjaFile.write(title)
        self.log('JobInjaCrawled')

        
