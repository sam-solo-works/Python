from scrapy.selector import Selector 
from scrapy.http import HtmlResponse

response = HtmlResponse(url = 'https://www.foodiecrush.com/hummus-veggie-wrap-plus-10-heavenly-hummus-recipes-to-make-at-home/') 
res = Selector(response)
res.xpath("//h2").extract() 
#Selector(response = response).xpath('//span/text()').extract()

print(res.xpath("//h2").extract())