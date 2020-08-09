from urllib.parse import urlparse

links = (
    ("cda.pl", "Cda"),
    ("4anime.one", "ForAnimeDotOne"),
)

# https://www.cda.pl/video/1453770d9

def identifyUrl(url: str) -> str:
    parsed = urlparse(url)
    for link in links:
        if parsed.netloc == link[0] or parsed.netloc == "www." + link[0]:
            return link[1]
    return ""
