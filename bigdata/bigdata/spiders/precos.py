import scrapy
from bs4 import BeautifulSoup
import requests


class PrecosSpider(scrapy.Spider):
    name = "precos"
    start_urls = ["https://drogasil.com.br"]

    def parse(self, response):
        pass

