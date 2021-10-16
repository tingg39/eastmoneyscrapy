# Scrapy settings for gubaSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gubaSpider'

SPIDER_MODULES = ['gubaSpider.spiders']
NEWSPIDER_MODULE = 'gubaSpider.spiders'
COMMANDS_MODULE = 'gubaSpider.commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gubaSpider (+http://www.yourdomain.com)'

REACTOR_THREADPOOL_MAXSIZE = 100

CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100
DOWNLOAD_DELAY = 0

# DOWNLOAD_TIMEOUT = 40

COOKIES_ENABLES=False

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

RANDOM_UA_TYPE = "random"

DOWNLOADER_MIDDLEWARES = {
    'gubaSpider.middlewares.RandomUserAgentMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
       # 'youx.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
    'gubaSpider.middlewares.ProxyMiddleware': 200,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': None
}

RANDOM_UA_TYPE = 'random'

# import datetime
#
# ROBOTSTXT_OBEY = False
#
# LOG_LEVEL = 'DEBUG'
# to_day = datetime.datetime.now()
# log_file_path = 'log/scrapy_{}_{}_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day,to_day.hour,to_day.minute)
# LOG_FILE = log_file_path


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# SPIDER_MIDDLEWARES = {
#    'gubaSpider.middlewares.seleniumSpiderMiddleware': 200,
# }


# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

# DOWNLOADER_MIDDLEWARES = {
#     'gubaSpider.middlewares.seleniumSpiderMiddleware': 200,
#     'gubaSpider.middlewares.GubaspiderDownloaderMiddleware': None,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'gubaSpider.pipelines.GubaspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_DB_NAME='guba'
MYSQL_HOST='localhost'
MYSQL_PORT=3306
MYSQL_USER='root'
MYSQL_PASSWORD='123456'