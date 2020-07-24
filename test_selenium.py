#!/usr/bin/env python3
import libs


urls = []
try:
    with open("list.txt", "r") as file:
        for line in file.readlines():
            l = line.strip()
            if not l == "" and not l == None and not l[0] == "#":
                urls.append(l)
except FileNotFoundError:
    print("Cannot find `list.txt` file! Creating!")
    print("Note: Please, fill it with your links")
    with open("list.txt", 'w') as file:
        file.write("")
    exit()

# Mute browser
# profile = webdriver.FirefoxProfile()
# profile.set_preference("media.volume_scale", "0.0")

# Launch downloader
browser = libs.Downloader.Browser(urls)
