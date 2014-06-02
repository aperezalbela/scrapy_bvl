from scrapy.spider import Spider
from scrapy.selector import Selector
from bvl.items import Company



class BVLSpider(Spider):
	name			=	"bvl"
	allowed_domains	=	['www.bvl.com.pe']
	start_urls		=	[
			'http://www.bvl.com.pe/includes/empresas_todas.dat',
	]

	def parse(self, response):
		sel 		=	Selector(response)
		companies	=	sel.xpath('//tr/td')

		items		=	[]

		for company in companies:
			item				=	Company()
			item['name']		=	company.xpath('a/text()').extract()
			item['link']		=	company.xpath('a/@href').extract()
			item['code']		=	company.xpath('a/@href').re('inf_corporativa(\w+)_')
			item['mnemonic']	=	company.xpath('a/@href').re('inf_corporativa\w+_(\w+)\.html')
			items.append(item)
		return items