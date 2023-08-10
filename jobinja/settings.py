from fake_useragent import UserAgent

user_agent = UserAgent()

# This number (20) can be customized
USER_AGENT_LIST = [user_agent.random for _ in range(20)]

BOT_NAME = "jobinja"

SPIDER_MODULES = ["jobinja.spiders"]
NEWSPIDER_MODULE = "jobinja.spiders"

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400
}

ITEM_PIPELINES = {
    'jobinja.pipelines.JobinjaPipeline': 200
}

PROXY_POOL_ENABLED = True

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
