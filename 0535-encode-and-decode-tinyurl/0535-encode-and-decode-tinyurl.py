class Codec:
    
    def __init__(self):
        self.url = {}
        self.count = -1

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.count += 1
        self.url[self.count] = longUrl
        return f"http://tinyurl.com/${self.count}" 

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url[int(shortUrl[20:])]
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))