#!/usr/bin/env python3
import libs

try:
    links = []
    with open("list.txt", "r") as file:
        for link in file.readlines():
            link = link.strip()
            if link and not link[0] == "#":
                links.append(link)
except FileNotFoundError:
    print("File `list.txt` not found! Creating one, please fill it.")
    with open("list.txt", "a") as file:
        file.write("")
    exit()

downloader = libs.Downloader.Browser(links)