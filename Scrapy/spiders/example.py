# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:02:45 2015

@author: IZFE_BAU
"""

import scrapy
# import pdb; pdb.set_trace()

class TripAdvisor(scrapy.Spider):
    name = 'tripadv'
    allowed_domains = ['www.tripadvisor.com']
    start_urls = [
        'http://www.tripadvisor.com/Restaurants-g187457-San_Sebastian_Donostia_Guipuzcoa_Province_Basque_Country.html'
        ]
        
    def parse(self, response):
        """
        Parsea una página con una lista de restaurante. 
        Lanza el analisis para cada restaurante de la lista, y de la siguiente página
        """
        msg = 'A response from %s has arrived' % response.url
        self.logger.info(msg)
        
        resturls = response.xpath('//h3[@class="title"]/a/@href').extract()
        for url in resturls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_restaurant)
                
        #urls = response.xpath('//a[text()="Next"]/@href').extract()
        nexturl = response.xpath('//a[contains(@class,"next")]/@href').extract()
        if nexturl:
            nexturl = response.urljoin(nexturl[0])
        #for urlnext in urls:
        yield scrapy.Request(nexturl, callback=self.parse)

    def parse_restaurant(self, response):
        """
        Parsea la página de un restaurante, y extrae nombre y coordinadas
        """
        # <div class="mapContainer" data-lat="43.311714" data-lng="-1.9001" data-name="Borda Berri" data-locid="1519796" data-pinimg="http://static.tacdn.com/img2/maps/icons/pin_centroid_addressblock.png">
        container = response.xpath("//div[@class='mapContainer']")
        
        name = container.xpath("@data-name").extract_first()
        lat = container.xpath("@data-lat").extract_first()
        lng = container.xpath("@data-lng").extract_first()
        data = {'name': name, 'lat': lat, 'lng': lng}
        yield data