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
            
            if self.is_element_exist((By.CLASS_NAME, "pframe")):
                iframe = self.driver.find_element_by_css_selector("div.pframe iframe")
                title = str(self.driver.title)[6:] + ".mp4"
                self.driver.get(iframe.get_attribute("src"))
                if self.is_element_exist((By.TAG_NAME, "video")):
                    print("Found video!")
                    output.append((self.driver.find_element_by_tag_name("video").get_attribute("src"), title))
                else:
                    print("Ehhh...")
        
        return output
    
    def download(self, links: list, destination: str="./video/"):
        getl = self.get_links(links)
        if not os.path.isdir(destination):
            os.mkdir(destination)

        for link in getl:
            print("Downloading: " + link[1])
            filename = wget.download(link[0])
            os.rename(filename, destination + link[1])
            print("")
