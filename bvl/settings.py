# Scrapy settings for bvl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bvl'

SPIDER_MODULES = ['bvl.spiders']
NEWSPIDER_MODULE = 'bvl.spiders'
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bvl (+http://www.yourdomain.com)'
