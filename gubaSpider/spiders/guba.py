import scrapy
import time
import pandas as pd
import time
import random
import re

from gubaSpider.items import GubaspiderItem#,ContentspiderItem#,AuthorspiderItem #,DataspiderItem

class GubaSpider(scrapy.Spider):

    name = 'guba'
    baseurl = 'http://guba.eastmoney.com'

    #ticket_count = '300014'
    start_num = 1
    #end_num = 1000000

    hs300 = pd.read_csv('C:/Users/CML/情绪因子/hs300_page.csv', index_col=0, dtype={'stock_num': str})

    def start_requests(self):
        # tqdm(range(1, int((browser.find_elements_by_xpath('//*[@id="articlelistnew"]/div')[a - 2].
        #                          find_element_by_xpath('span/span/span[1]/span').text)))):
        for j in range(240,300):
            self.ticket_count = str(self.hs300.stock_num[j])
            self.end_num = int(self.hs300.pages_sum[j]) + 100
            for i in range(self.start_num, self.end_num):
                self.url="http://guba.eastmoney.com/list,"+self.ticket_count+",f_{}.html".format(i)
                yield scrapy.Request(self.url,meta={'url': self.url}, callback=self.parse,dont_filter=True)
                #time.sleep(0.1*(random.random()))
            #time.sleep(1)
        # author_url="https://i.eastmoney.com/3006113720930996"
        # yield scrapy.Request(author_url,callback=self.parse_author)

    def parse(self, response):
        # self.responseURL = response.url
        # self.requestURL = response.meta['url']
        # if response.xpath('//*[@id="articlelistnew"]/div[2]').extract_first() == '最近一年无帖子！':
        #     continue

        # if str(self.responseURL) == (self.requestURL):
        #     print('ok!')
        # else:
        #     print('--------------------->>>>>>>>Your request is redirect,retrying.....<<<<<-------------------------')
        #     yield scrapy.Request(url=self.requestURL, meta={'url': self.requestURL}, callback=self.parse,dont_filter=True)

        for item in response.xpath('//div[@id="articlelistnew"]/div[contains(@class,"articleh normal_post")]'):
            guba=GubaspiderItem()
            guba['ticket'] = response.xpath('//*[@id="stockname"]/@data-popstock').get()
            if len(guba['ticket']) < 6:
                print(guba['ticket'])
                print("=================================太累了，该摸鱼了！！！！！！！===========================================")
                break

            guba['read_number']=item.xpath('span[@class="l1 a1"]/text()').extract_first()
            guba['command_number']=item.xpath('span[@class="l2 a2"]/text()').extract_first()
            guba['title']=item.xpath('span[@class="l3 a3"]/a/@title').get()
            if item.xpath('span[@class="l3 a3"]/a/@href').extract_first()[:5] == '/news':
                guba['title_url']=self.baseurl+item.xpath('span[@class="l3 a3"]/a/@href').extract_first()
            else:
                guba['title_url'] = item.xpath('span[@class="l3 a3"]/a/@href').extract_first()
            # guba['author']=item.xpath('span[@class="l4 a4"]/a//text()').extract_first()
            # guba['author_url']=item.xpath('span[@class="l4 a4"]/a/@href').extract_first()
            # if guba['author_url'][0]=='/':
            #     guba['author_url']=self.baseurl+guba['author_url']
            guba['date']=item.xpath('span[@class="l5 a5"]/text()').extract_first()
            guba['update_times'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

            # try:
            #     guba['symble'] = item.xpath('span[@class="l3 a3"]/em/text()').extract_first() # 新闻类型（图片、公告等）
            # except:
            #     guba['symble'] = '投稿'
                # guba['ticket'] = self.ticket_count
                # time.sleep(1)
            # guba['date']=self.baseurl
            # yield scrapy.Request(guba['title_url'],callback=self.parse_data)
            # yield scrapy.Request(guba['author_url'],callback=self.parse_author)
            # yield scrapy.Request(guba['date'], callback=self.parse_data)
            yield guba
        # print(self.responseURL)
        # print(self.requestURL)
        # print(self.url)
        if len(guba['ticket']) < 6 and len(guba['ticket']) > 1 :
            yield scrapy.Request(url=response.url, callback=self.parse,dont_filter=True)

        # for item in response.xpath('//div[@id="articlelistnew"]/div[@class="articleh normal_post odd"]'):
        #     guba=GubaspiderItem()
        #     guba['read_number']=item.xpath('span[@class="l1 a1"]/text()').extract_first()
        #     guba['command_number']=item.xpath('span[@class="l2 a2"]/text()').extract_first()
        #     guba['title']=item.xpath('span[@class="l3 a3"]/a/@title').get()
        #     if item.xpath('span[@class="l3 a3"]/a/@href').extract_first()[:5] == '/news':
        #         guba['title_url']=self.baseurl+item.xpath('span[@class="l3 a3"]/a/@href').extract_first()
        #     else:
        #         guba['title_url'] = item.xpath('span[@class="l3 a3"]/a/@href').extract_first()
        #     # guba['author']=item.xpath('span[@class="l4 a4"]/a//text()').extract_first()
        #     # guba['author_url']=item.xpath('span[@class="l4 a4"]/a/@href').extract_first()
        #     # if guba['author_url'][0]=='/':
        #     #     guba['author_url']=self.baseurl+guba['author_url']
        #     guba['ticket'] = response.xpath('//*[@id="stockname"]/@data-popstock').get()
        #     guba['date']=item.xpath('span[@class="l5 a5"]/text()').extract_first()
        #     guba['update_times'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        #
        #     # try:
        #     #     guba['symble'] = item.xpath('span[@class="l3 a3"]/em/text()').extract_first() # 新闻类型（图片、公告等）
        #     # except:
        #     #     guba['symble'] = '投稿'
        #     # guba['date']=self.baseurl
        #     # yield scrapy.Request(guba['title_url'],callback=self.parse_data)
        #     # yield scrapy.Request(guba['author_url'],callback=self.parse_author)
        #     yield guba



        #print(guba['ticket'])
        # if guba['ticket'] is not self.ticket_count:
        #     #guba['page_now'] = self.page_now
        #     self.COUNT += 1
        #     if self.COUNT > 10:
        #         self.crawler.engine.close_spider(self, 'closespider')
        #         self.COUNT=0
    #
    # def parse_data(self,response):
    #     content=ContentspiderItem()
    #     content['title_url']=response._url
    #     content['data_real']=response.xpath('//*[@id="zwconttb"]/div[2]/text()').extract_first()
    #     yield content

    # def parse_author(self,response):
    #     author=AuthorspiderItem()
    #     author['author_url']=response._url
    #     author['following_number']=response.xpath('//*[@id="tafollownav"]/p/span/text()').extract_first()
    #     author['follower_number']=response.xpath('//*[@id="tafansa"]/p/span/text()').extract_first()
    #     yield author

    # def parse_data(self,response):
    #     guba['date']=response.xpath('//*[@id="zwconttb"]/div[2]/text()').extract_first()
    #     yield guba
