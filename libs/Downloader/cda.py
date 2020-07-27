import libs.Downloader.Downloader as d # pylint: disable=import-error
from bs4 import BeautifulSoup
import requests
import time, wget, os
from urllib.parse import urlparse
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

class Downloader(d._Downloader):
    def get_links(self, links: list):
        output = []
        for u in links:
            self.driver.get(u)

            # Check for Form id=upload_form    
            if self.is_element_exist((By.ID, "upload_form")):
                print("Found form to be filled!")
                dzien = self.driver.find_element_by_id("dzien")
                dzien.click()
                first = self.driver.find_element_by_xpath("//select[@name='dzien']/option[text()='1']")
                first.click()

                miesiac = self.driver.find_element_by_id("miesiac")
                miesiac.click()
                styczen = self.driver.find_element_by_xpath("//select[@name='miesiac']/option[text()='Styczeń']")
                styczen.click()

                rok = self.driver.find_element_by_id("rok")
                rok.click()
                dwutysieczny = self.driver.find_element_by_xpath("//select[@name='rok']/option[text()='2000']")
                dwutysieczny.click()

                zapamietaj = self.driver.find_element_by_xpath("//input[@type='checkbox']")
                zapamietaj.click()

                inp = self.driver.find_element_by_xpath("//button[@class='btn btn-my']")
                inp.click()

                print("Filled! Waiting: 3s")
                time.sleep(3)


            # Define Max resolution
            if self.is_element_exist((By.CLASS_NAME, "quality-btn")):
                quality = self.driver.find_elements_by_class_name("quality-btn")
                highest = None
                for q in quality:
                    check = (q.get_attribute('data-quality'), q.get_attribute("href"))
                    if highest == None:
                        highest = check
                        continue

                    if highest[0] == "vl" and check[0] == "lq":
                        highest = check
                    elif highest[0] == "lq" and check[0] == "sd":
                        highest = check
                    elif highest[0] == "sd" and check[0] == "hd":
                        highest = check

                print(highest)
                if not highest == u:
                    self.driver.get(highest[1])

            video = self.driver.find_element_by_tag_name("video")
            link = video.get_attribute("src")
            print("Found video: " + link)
            output.append((link, str(self.driver.title) + ".mp4"))
        
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
