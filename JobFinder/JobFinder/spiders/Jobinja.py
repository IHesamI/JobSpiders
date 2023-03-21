from pathlib import Path
import scrapy
import re
class Jobinja(scrapy.Spider):
    name='Jobinja'
    def start_requests(self):
        baseUrl='https://jobinja.ir/jobs/category/it-software-web-development-jobs/%D8%A7%D8%B3%D8%AA%D8%AE%D8%AF%D8%A7%D9%85-%D9%88%D8%A8-%D8%A8%D8%B1%D9%86%D8%A7%D9%85%D9%87-%D9%86%D9%88%DB%8C%D8%B3-%D9%86%D8%B1%D9%85-%D8%A7%D9%81%D8%B2%D8%A7%D8%B1'
        urls=[baseUrl+'?page=%s'%(i) for i in range(1,82)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def  parse(self, response):
        titles=response.css('a.c-jobListView__titleLink::text').getall()
        # JobInfo=response.xpath('//li [@class="c-jobListView__metaItem"]/span/span/text()').getall() # TODO for more information need this field 
        for title in titles:
            title=title.replace('\n','')
            title=re.sub(r'\s{2,}','',title)
            title=title+'\n'
            with open(self.name+'.csv','a',encoding="utf-8") as jobinjaFile:
                jobinjaFile.write(title)
        self.log(self.name+' Crawled')

        
