# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import fake_useragent
from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import time
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import random
import scrapy
from scrapy import log
import requests


# logger = logging.getLogger()

import json
import requests
import logging


class ProxyMiddleware(object):
    def __init__(self, proxy_url = 'http://http1.9vps.com/getip.asp?username=sxj18905815982&pwd=91d3f6fd6240c80592834c7be0aec384&geshi=1&fenge=1&fengefu=&getnum=100'):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = 'http://http1.9vps.com/getip.asp?username=sxj18905815982&pwd=91d3f6fd6240c80592834c7be0aec384&geshi=1&fenge=1&fengefu=&getnum=100'

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                # p = json.loads(response.text)
                # proxy = '{}:{}'.format(p.get('ip'), p.get('port'))
                p = response.text
                proxy = p

                print('get proxy ...')
                ip = {"http": "http://" + proxy, "https": "https://" + proxy}
                r = requests.get("http://www.baidu.com", proxies=ip, timeout=1.1)
                if r.status_code == 200:
                    return proxy
        except:
            print('get proxy again ...')
            return self.get_random_proxy()

    def process_request(self, request, spider):
            proxy = self.get_random_proxy()
            if proxy:
                self.logger.debug('======' + '使用代理 ' + str(proxy) + "======")
                request.meta['proxy'] = 'http://{proxy}'.format(proxy=proxy)

    def process_response(self, request, response, spider):
        if response.status != 200:
            print("again response ip:")
            request.meta['proxy'] = 'http://{proxy}'.format(proxy=self.get_random_proxy())
            return request
        return response

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )

# class ProxyMiddleWare(object):
#     """docstring for ProxyMiddleWare"""
#     def process_request(self,request, spider):
#         '''对request对象加上proxy'''
#
#         proxy = 'http://'+self.get_random_proxy()
#         print("this is request ip:" + proxy)
#         request.meta['proxy'] = proxy
#
#
#     def process_response(self, request, response, spider):
#         '''对返回的response处理'''
#         # 如果返回的response状态不是200，重新生成当前request对象
#         if response.status != 200:
#             proxy = self.get_random_proxy()
#             print("this is response ip:"+proxy)
#             # 对当前reque加上代理
#             request.meta['proxy'] = proxy
#             return request
#         return response
#
#     def get_random_proxy(self):
#         '''随机从文件中读取proxy'''
#         while 1:
#             headers = {
#                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)'
#             }
#             proxy_url = 'http://http.9vps.com/getip.asp?username=sxj18905815982&pwd=8028de19d788bad46cf10e91916ee48a&geshi=1&fenge=1&fengefu=&getnum=1'
#             aaa=requests.get(proxy_url, headers=headers).text
#             proxies = aaa.split('\r\n')
#             if proxies:
#                 break
#             else:
#                 time.sleep(1)
#         proxy = random.choice(proxies).strip()
#         return proxy



class seleniumSpiderMiddleware(object):
    def process_request(self, request, spider):
        #webdriver.Chrome('chromedriver.exe')
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        # 指定谷歌浏览器路径
        self.driver = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:/Anaconda3/envs/spider/chromedriver.exe')
        self.driver.get(request.url)
        #time.sleep(0.1)
        html = self.driver.page_source
        self.driver.quit()
        return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',
                                        request=request)

class GubaspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class GubaspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import os

from fake_useragent import UserAgent

class RandomUserAgentMiddleware(object):
    # 随机更换user-agent

    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        location = os.getcwd() + '/fake_useragent.json'
        self.ua = fake_useragent.UserAgent(path=location)
        self.ua_type = crawler.settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            return getattr(self.ua, self.ua_type)

        request.headers.setdefault('User-Agent', get_ua())

