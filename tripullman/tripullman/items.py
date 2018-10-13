# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TripullmanItem(scrapy.Item):
    # define the fields for your item here like:
    nombre = scrapy.Field()
    N_opinion = scrapy.Field()
    calificacion = scrapy.Field()
    direccion = scrapy.Field()
    tipo = scrapy.Field()
    region = scrapy.Field()
    #coordenadas = scrapy.Field() 
    web = scrapy.Field()
    tipo1 = scrapy.Field()
    Op_sobre = scrapy.Field()
    titulo = scrapy.Field()
    comentario = scrapy.Field()
    califica = scrapy.Field()
    autor = scrapy.Field()
    lugar = scrapy.Field()
    fecha = scrapy.Field()
    Nivel = scrapy.Field()
