import libs.Downloader.url as url
from . import *
import importlib

class Browser: # pylint: disable=function-redefined
    def __init__(self, links: list, destination: str="./video/"):
        self.links = links
        self.destination = destination

        mods = {}
        modules = {}
        for l in self.links:
            module = url.identifyUrl(l) # pylint: disable=undefined-variable
            if not module in mods:
                mods[module] = 1
        
        for key in mods:
            modules[key] = importlib.import_module("libs.Downloader." + key)

        last_driver = None
        for l in links:
            module = url.identifyUrl(l) # pylint: disable=undefined-variable
            if not last_driver == module:
                try:
                    downloader.driver.close()
                except:
                    pass
                downloader = eval(module + ".Downloader()")

            downloader.download([l], destination)
            last_driver = module
