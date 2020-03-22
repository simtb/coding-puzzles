import unittest
from challenges.url_shortener import UrlShortener

class TestUrlShortener(unittest.TestCase):
    test_url_1: str = "www.foo.com"
    test_url_2: str = "www.bar.com"

    def test_url(self):
        shortened_url: str = UrlShortener.shorten(self.test_url_1)
        self.assertEqual(len(shortened_url), 6)
        shortened_url_2: str = UrlShortener.shorten(self.test_url_2)
        self.assertEqual(len(shortened_url_2), 6)
        shortened_url_3: str = UrlShortener.shorten(self.test_url_1)
        self.assertEqual(shortened_url, shortened_url_3)
        self.assertEqual(UrlShortener.restore(shortened_url), self.test_url_1)



if __name__ == "__main__":
    unittest.main()