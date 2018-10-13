# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 23:35:42 2017

@author: Cami
"""

import scrapy


class TripullmanSpider(scrapy.Spider):
    name = 'tripullman'

    start_urls = ['https://www.tripadvisor.com.au/Hotel_Review-g255070-d619468-Reviews-Pullman_Port_Douglas_Sea_Temple_Resort_Spa-Port_Douglas_Queensland.html']
    download_delay = 1
    LOG_ENCODING = 'Latin-1'
    #FEED_EXPORT_ENCODING = 'utf-8'

    def parse(self, response):
        # follow links to author pages
        for href in response.xpath('//*[@class="listing_title"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_hotel)

        # follow pagination links
        #next_page = response.xpath('//*[@class="unified pagination standard_pagination]/a/@href').extract_first()
        #next_page = response.xpath('//a[contains(text(), "Next")]/@href').extract_first()
        #if next_page and len(next_page) > 0:
        #    next_page = response.urljoin(next_page)
         #   yield scrapy.Request(next_page, callback=self.parse)

    def parse_hotel(self, response):
        
        for href in response.xpath('//*[@class="quote"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href), 
                                 callback=self.parse_comentario)
            
        #siguiente = response.xpath('//a[contains(text(), "Next")]/@href').extract_first()
        #if siguiente is not None:
         #   siguiente = response.urljoin(siguiente)
          #  yield scrapy.Request(siguiente, callback=self.parse_hotel)
            
        
        yield {
            'nombre': response.xpath('//h1[@id="HEADING"]/text()').extract(),
            'N_opinion': response.xpath('//*[@class="more taLnk"]/text()').extract(),
            'calificacion': response.xpath('//*[@class="prw_rup prw_common_bubble_rating bubble_rating"]/span/@alt').extract(),
            'direccion': response.xpath('//*[@class="format_address"]/span/text()').extract(),
            'coordenadas': response.xpath('//*[@id="STATIC_MAP"]/span/img/@src').extract()
            }
        
        
    def parse_comentario(self, response):
        def extract_with_xpath(query):
                return response.xpath(query).extract_first()
                
        yield {
             'Op_sobre': extract_with_xpath('[@class="alHeadInline"]/a'),
             'titulo': extract_with_xpath('//*[@class="quote"]/text()'),
             'comentario': extract_with_xpath('//*[@class="entry"]/p/text()'),
             'califica': extract_with_xpath('//*[@class="rating reviewItemInline"]/span/img/@alt'),
             'autor': extract_with_xpath('//*[@class="username mo"]/span/text()'),
             'lugar': extract_with_xpath('//*[@class="location"]/text()'),
             'fecha': extract_with_xpath('//*[@class="rating reviewItemInline"]/span/text()'),
             'Nivel': extract_with_xpath('//*[@class="reviewerBadge badge"]/span/text()')
             }
        
        