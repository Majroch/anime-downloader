from urllib.parse import urlparse

links = (
    ("cda.pl", "Cda"),
    ("4anime.one", "ForAnimeDotOne"),
    # ("wbijam.pl", "Wbijam"),
)

# https://www.cda.pl/video/1453770d9

def identifyUrl(url: str) -> str:
    parsed = urlparse(url)
    for link in links:
        # print(parsed.netloc)
        if link[0] in parsed.netloc:
            return link[1]
    return ""
