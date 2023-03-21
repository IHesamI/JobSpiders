from pathlib import Path
import scrapy
import re
# TODO thie site try to defend itself from Spider 
# ! Need to fix this 

class IranTalent(scrapy.Spider):
    name='IranTalent'
    def start_requests(self):
        baseUrl='https://www.irantalent.com/jobs/it-software-web-development-jobs?language=persian'
        urls=[baseUrl+'&page=%s'%(i) for i in range(1,2)]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def  parse(self, response):
        print(response.status)
        # titles=response.css('p.position-title.text-ellipsis::text').getall()
        # print(titles)
        # # JobInfo=response.xpath('//li [@class="c-jobListView__metaItem"]/span/span/text()').getall() # TODO for more information need this field 
        # for title in titles:
        #     title=title.replace('\n','')
        #     title=re.sub(r'\s{2,}','',title)
        #     title=title+'\n'
        #     print(title)
        #     with open(self.name+'.csv','a',encoding="utf-8") as jobinjaFile:
        #         jobinjaFile.write(title)
        self.log(self.name+' Crawled')

        
