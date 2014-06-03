#coding:utf-8
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from bvl.items import Company, Mnemonic

import os

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
			url 				=	'http://www.bvl.com.pe/jsp/Inf_EstadisticaGrafica.jsp?Cod_Empresa=%s&Nemonico=%s' % (item['code'][0], item['mnemonic'][0])
			
			print "------------------------------------------------------------------------------------"
			print str(item['name'])
			print str(item['link'])
			print str(item['code'])
			print str(item['mnemonic'])
			print "------------------------------------------------------------------------------------"
			
			os.mkdir('results/'+item['name'][0])
			request = Request(url, callback=self.parseMnemonics)
			request.meta['company'] = item['name'][0].encode('utf-8')
			yield request


	def parseMnemonics(self, response):
		items		=	[]
		sel 		=	Selector(response)
		mnemonics 	=	sel.xpath('//div[contains(@id,"divTipo")]/table/tr/td/select/option/text()').extract()
		company 	=	response.meta['company']

		print "------------------------------------------------------------------------------------"
		print company
		print mnemonics
		print "------------------------------------------------------------------------------------"
		
		for i in mnemonics:
			if not i.strip() == "":
				directory	= company.decode('utf-8')+'/'+i
				os.mkdir('results/'+directory)	
		