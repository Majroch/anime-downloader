#!/usr/bin/env python3
from ..Downloader import _Downloader # pylint: disable=import-error
from bs4 import BeautifulSoup
import requests
import time, wget, os
from urllib.parse import urlparse
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

class Downloader(_Downloader):
    def get_links(self, links: list):
        output = []
        for u in links:
            self.driver.get(u)
            filename = self.driver.title
            
            if self.is_element_exist((By.CLASS_NAME, "mirror_dl")):
                download_button = self.driver.find_element_by_css_selector("a.mirror_dl")
                href = download_button.get_attribute("href")
                output.append((href, filename))
        
        return output
    
    def download(self, links: list, destination: str="./video/"):
        getl = self.get_links(links)
        if not os.path.isdir(destination):
            os.mkdir(destination)

        for link in getl:
            print("Downloading...")
            filename = wget.download(link[0], out=destination)
            print("\nDownloaded: " + filename)
            # os.rename(filename, out=destination)
            print("")
