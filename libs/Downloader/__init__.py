# from . import *
from .url import identifyUrl
import importlib
import os

class Browser: # pylint: disable=function-redefined
    def __init__(self, links: list, destination: str="./video/"):
        self.links = links
        self.destination = destination

        mods = {}
        modules = {}
        for l in self.links:
            module = identifyUrl(l) # pylint: disable=undefined-variable
            if not module in mods:
                mods[module] = 1
        
        current_pkg = os.path.dirname(os.path.abspath(__file__)).replace(os.getcwd(), "")[1:].replace("/", ".")
        for key in mods:
            try:
                modules[key] = importlib.import_module("." + key, current_pkg)
            except ImportError:
                print("No Module named: " + key + ". Ommiting...")

        last_driver = None
        for l in links:
            module = identifyUrl(l) # pylint: disable=undefined-variable
            if module in modules.keys():
                try:
                    if not last_driver == module:
                        try:
                            downloader.driver.close()
                        except:
                            pass
                            downloader = eval(module + ".Downloader()")

                    downloader.download([l], destination)
                    last_driver = module
                except SyntaxError:
                    print("Cannot load module: " + module)
        if downloader:
            downloader.driver.close()
