# -*- coding: utf-8 -*-

import scrapy
from tripullman.items import TripullmanItem
import re

#download_delay = 1
#LOG_ENCODING = 'Latin-1'
#FEED_EXPORT_ENCODING = 'utf-8'

class breveSpider(scrapy.Spider):
    name = 'breve'
    allowed_domains = ["tripadvisor.com.au"]
    start_urls = ['https://www.tripadvisor.com.au/Hotel_Review-g255070-d619468-Reviews-Pullman_Port_Douglas_Sea_Temple_Resort_Spa-Port_Douglas_Queensland.html']
    #'https://www.tripadvisor.cl/Hotels-g2615208-Coquimbo_Region-Hotels.html'

    def start_request(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        cookies = {'TALanguage':'ALL'}
        urls = ['https://www.tripadvisor.com.au/Hotel_Review-g255070-d619468-Reviews-Pullman_Port_Douglas_Sea_Temple_Resort_Spa-Port_Douglas_Queensland.html']
        yield scrapy.Request(urls, headers = headers, cookies = cookies, callback=self.parse)

    def parse(self, response):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        i = TripullmanItem()
        i['nombre'] = response.xpath('//h1[@id="HEADING"]/text()').extract()
        i['N_opinion'] = response.xpath('//*[contains(@class,"reviewCount")]/text()').extract()
        i['calificacion'] = str.split(response.xpath('//*[@class="prw_rup prw_common_bubble_rating rating"]/span/@alt').extract()[0])[0]
        i['direccion'] = response.xpath('//*[contains(@class,"blEntry address")]/span/span/text()').extract()
        i['tipo'] = re.findall("\w+(?=_Review)",response.url)
        i['region'] = response.xpath('//*/li[3]/a/span[@itemprop="title"]/text()').extract()
        #i['coordenadas'] = response.xpath('//*[@id="STATIC_MAP"]/span/img/@src').extract()
        i['web'] = response.url
        i['tipo1'] = response.xpath("//*[contains(@class,'header_popularity')]/text()").extract()

        for href in response.xpath('//*[contains(@class,"rev_wrap")]/div[2]/div/a/@href').extract():
            yield scrapy.Request(response.urljoin(href), meta={'i': i},
                                 callback=self.parse_comentario)
        
        prueba = response.xpath('//a[contains(text(), "Next")]/@data-offset').extract_first()
        algo = 'Reviews-or'+ str(''.join(prueba)) +'-'
        siguiente = re.sub('Reviews-',algo,i['web'])
        #cookies = {'TALanguage': 'ALL', 'Domain':'.tripadvisor.com.au', 'Expires':'Tue, 16-Jul-2019 21:34:13 GMT', 'Path':'/'}
        if prueba is not None:
            yield scrapy.Request(siguiente, 
                                 callback=self.parse, headers = headers)
            
    def parse_comentario(self, response):
        i = response.meta['i']
        i['Op_sobre'] = response.xpath('//*[@class="altHeadInline"]/a/text()').extract()
        i['titulo'] = response.xpath('//*[@id="HEADING"]/text()').extract_first()
        i['comentario'] = response.xpath('//*[contains(@class,"fullText")]/text()').extract_first()
        i['califica'] = str.replace(str.split(response.xpath('//*[contains(@class, "rev_wrap")]/div[2]/span/@class').extract_first())[1],"bubble_","")
        i['autor'] = response.xpath('(//*[@class="info_text"])[1]/*/text()').extract_first()
        i['lugar'] = response.xpath('(//*[@class="info_text"])[1]/*[2]/text()').extract_first()
        i['fecha'] = response.xpath('//*[@class="ratingDate"]/@title').extract_first()
        x = response.xpath('//*[@class="badgetext"]/text()').extract_first()
        if x is not None:
            i['Nivel'] = x
        yield i
        
        """
        headers = {
                            'Accept': ' text/html, */*',
                            'Accept-Encoding': 'gzip,deflate, br',
                            'Accept-Language': 'en-US,en;q=0.5',
                            'Cache-Control': 'no-cache',
                            'Connection': 'keep-alive',
                            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                            'Host': 'www.tripadvisor.com.au',
                            'Pragma': 'no-cache',
                            'Referer': 'https://www.tripadvisor.com.au/Hotel_Review-g255070-d619468-Reviews-Pullman_Port_Douglas_Sea_Temple_Resort_Spa-Port_Douglas_Queensland.html',
                            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
        
        
        
        
        
        
        """