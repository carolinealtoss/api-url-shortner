import hashlib

class UrlShortner:

    def __init__(self):
        self.url_mapping = {}

    def url_shortner(self, original_url):
        hash_object = hashlib.md5(original_url.encode())
        short_url = hash_object.hexdigest()[:6]

        self.url_mapping[short_url] = original_url
        return short_url