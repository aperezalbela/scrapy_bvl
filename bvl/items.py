# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class Company(Item):
	name		=	Field()
	link		=	Field()
	code		=	Field()
	mnemonic	=	Field()


class Mnemonic(Item):
	name		=	Field()