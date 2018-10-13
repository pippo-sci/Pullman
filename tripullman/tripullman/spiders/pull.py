# -*- coding: utf-8 -*-
import scrapy


class PullSpider(scrapy.Spider):
    name = 'pull'
    allowed_domains = ['tripadvisor.com.au']
    start_urls = ['https://www.tripadvisor.com.au/Hotel_Review-g255070-d619468-Reviews-Pullman_Port_Douglas_Sea_Temple_Resort_Spa-Port_Douglas_Queensland.html']
    download_delay = 1.5

    def cargar(self,response):
        yield scrapy.Request(responseurljoin(href), callbacl=self.parse)

    def parse(self, response):
        for href in response.xpath('//*[@class="listing_title"]/a/@href').extract():
            yield scrapy.Request(response.urljoin(href),
                                 callback=self.parse_hotel)
