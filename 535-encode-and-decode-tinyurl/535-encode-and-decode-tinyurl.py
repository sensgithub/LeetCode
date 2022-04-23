class Codec:

    def __init__(self):
        self.m = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
    
        """
        self.m[longUrl] = str(len(self.m))
        return "http://tinyurl.com/" + self.m[longUrl]
   


    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
    
        value = shortUrl.split("/")
        value = value[len(value) - 1]
        for j in self.m:
            if self.m[j] == value:
                return j
        return -1