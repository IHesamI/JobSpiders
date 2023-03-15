from pathlib import Path
import scrapy

class Jobvision(scrapy.Spider):
    name='Jobvision'
    def start_requests(self):
        urls=['https://jobvision.ir/jobs/category/developer']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def  parse(self, response):
        Path(F'JOBVISION.html').write_bytes(response.body)
        self.log('Jobvision saved')
        # return super().parse(response)
        
