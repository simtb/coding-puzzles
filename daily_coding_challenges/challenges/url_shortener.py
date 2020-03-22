"""
Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""

from random import randint

class UrlShortener:

    lookup: dict = {}

    @staticmethod
    def shorten(url: str) -> str:
        if UrlShortener.lookup.get(url) != None:
            return UrlShortener.lookup.get(url)
        else:
            characters: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
            shortened_url: str = ""

            for i in range(6):
                random_index: int = randint(0, 61)
                random_character: str = characters[random_index]
                shortened_url += random_character
            
            UrlShortener.lookup[url]: str = shortened_url
            return shortened_url
    
    @staticmethod
    def restore(shortened_url: str) -> str:
        for url in UrlShortener.lookup:
            if UrlShortener.lookup[url] == shortened_url:
                return url
        else:
            return None

