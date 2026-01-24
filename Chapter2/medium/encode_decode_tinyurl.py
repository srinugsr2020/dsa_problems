"""
Encode and Decode TinyURL Problem

Problem Statement:
------------------
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as 
http://tinyurl.com/4e9iAk.

Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You just need 
to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to 
the original URL.

Implement the Codec class:
- encode(longUrl) returns a tiny URL for the given longUrl
- decode(shortUrl) returns the original longUrl from the tiny URL

Constraints:
------------
- 1 <= url.length <= 10^4
- url is guaranteed to be a valid URL

Examples:
---------
Example 1:
    Input: url = "https://leetcode.com/problems/design-tinyurl"
    Output: "https://leetcode.com/problems/design-tinyurl"
    Explanation: 
        codec = Codec()
        short = codec.encode(url)   # Returns something like "http://tinyurl.com/abc123"
        codec.decode(short)         # Returns original url

Hints:
------
1. Use two hash maps: one for long->short, one for short->long
2. Generate a unique short code for each URL
3. Several strategies for generating short codes:
   - Counter-based (simple, predictable)
   - Random string (harder to guess)
   - Hash-based (deterministic)
4. Handle the case where the same URL is encoded multiple times

Design Considerations:
- Should the same URL always get the same short code?
- How to handle collisions with random codes?
- What characters to use in the short code?

Expected Time Complexity: O(1) for both encode and decode
Expected Space Complexity: O(n) where n is the number of URLs encoded
"""

import random
import string
import hashlib


class Codec:
    """
    URL shortening service using random short codes.
    
    Uses two hash maps for bidirectional lookup:
    - long_to_short: original URL -> short code
    - short_to_long: short code -> original URL
    """
    
    BASE_URL = "http://tinyurl.com/"
    CODE_LENGTH = 6
    CHARS = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    
    def __init__(self):
        """Initialize the codec with empty mappings."""
        self._long_to_short = {}  # long URL -> short code
        self._short_to_long = {}  # short code -> long URL
    
    def encode(self, longUrl: str) -> str:
        """
        Encode a URL to a shortened URL.
        
        If the URL was already encoded, return the same short URL.
        
        Args:
            longUrl: The original URL to shorten
        
        Returns:
            The shortened URL
        """
        # Return existing short URL if already encoded
        if longUrl in self._long_to_short:
            return self.BASE_URL + self._long_to_short[longUrl]
        
        # Generate a unique short code
        code = self._generate_code()
        while code in self._short_to_long:
            code = self._generate_code()  # Regenerate if collision
        
        # Store bidirectional mapping
        self._long_to_short[longUrl] = code
        self._short_to_long[code] = longUrl
        
        return self.BASE_URL + code
    
    def decode(self, shortUrl: str) -> str:
        """
        Decode a shortened URL to its original URL.
        
        Args:
            shortUrl: The shortened URL
        
        Returns:
            The original URL
        """
        code = shortUrl.replace(self.BASE_URL, "")
        return self._short_to_long.get(code, "")
    
    def _generate_code(self) -> str:
        """Generate a random short code."""
        return ''.join(random.choices(self.CHARS, k=self.CODE_LENGTH))


class CodecCounter:
    """
    Alternative approach using a simple counter.
    
    Pros: Simple, no collisions
    Cons: Predictable (easy to guess other URLs)
    """
    
    BASE_URL = "http://tinyurl.com/"
    
    def __init__(self):
        """Initialize with counter starting at 0."""
        self._counter = 0
        self._long_to_short = {}
        self._short_to_long = {}
    
    def encode(self, longUrl: str) -> str:
        """Encode URL using counter as the short code."""
        if longUrl in self._long_to_short:
            return self.BASE_URL + self._long_to_short[longUrl]
        
        code = str(self._counter)
        self._counter += 1
        
        self._long_to_short[longUrl] = code
        self._short_to_long[code] = longUrl
        
        return self.BASE_URL + code
    
    def decode(self, shortUrl: str) -> str:
        """Decode short URL to original."""
        code = shortUrl.replace(self.BASE_URL, "")
        return self._short_to_long.get(code, "")


class CodecHash:
    """
    Alternative approach using hash of the URL.
    
    Pros: Deterministic (same URL always gives same code)
    Cons: Possible collisions (though rare with good hash)
    """
    
    BASE_URL = "http://tinyurl.com/"
    CODE_LENGTH = 8
    
    def __init__(self):
        """Initialize with empty mappings."""
        self._short_to_long = {}
    
    def encode(self, longUrl: str) -> str:
        """Encode URL using MD5 hash truncated to CODE_LENGTH."""
        # Use MD5 hash of the URL
        hash_obj = hashlib.md5(longUrl.encode())
        code = hash_obj.hexdigest()[:self.CODE_LENGTH]
        
        # Handle collision by appending counter
        original_code = code
        counter = 0
        while code in self._short_to_long and self._short_to_long[code] != longUrl:
            counter += 1
            code = original_code + str(counter)
        
        self._short_to_long[code] = longUrl
        return self.BASE_URL + code
    
    def decode(self, shortUrl: str) -> str:
        """Decode short URL to original."""
        code = shortUrl.replace(self.BASE_URL, "")
        return self._short_to_long.get(code, "")


class CodecBase62:
    """
    Production-style approach using Base62 encoding of counter.
    
    Converts counter to base62 (0-9, a-z, A-Z) for compact representation.
    """
    
    BASE_URL = "http://tinyurl.com/"
    CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def __init__(self):
        """Initialize with counter and mappings."""
        self._counter = 1  # Start at 1
        self._long_to_short = {}
        self._short_to_long = {}
    
    def encode(self, longUrl: str) -> str:
        """Encode URL using Base62 of counter."""
        if longUrl in self._long_to_short:
            return self.BASE_URL + self._long_to_short[longUrl]
        
        code = self._to_base62(self._counter)
        self._counter += 1
        
        self._long_to_short[longUrl] = code
        self._short_to_long[code] = longUrl
        
        return self.BASE_URL + code
    
    def decode(self, shortUrl: str) -> str:
        """Decode short URL to original."""
        code = shortUrl.replace(self.BASE_URL, "")
        return self._short_to_long.get(code, "")
    
    def _to_base62(self, num: int) -> str:
        """Convert number to base62 string."""
        if num == 0:
            return self.CHARS[0]
        
        result = []
        while num > 0:
            result.append(self.CHARS[num % 62])
            num //= 62
        
        return ''.join(reversed(result))


# Test cases
if __name__ == "__main__":
    # Test the main Codec class
    print("=" * 50)
    print("Testing Codec (Random)")
    print("=" * 50)
    
    codec = Codec()
    
    # Test case 1
    url1 = "https://leetcode.com/problems/design-tinyurl"
    short1 = codec.encode(url1)
    decoded1 = codec.decode(short1)
    print(f"Original:  {url1}")
    print(f"Shortened: {short1}")
    print(f"Decoded:   {decoded1}")
    print(f"Match: {url1 == decoded1}\n")
    
    # Test case 2: Same URL should give same short URL
    short1_again = codec.encode(url1)
    print(f"Encoding same URL again: {short1_again}")
    print(f"Same as before: {short1 == short1_again}\n")
    
    # Test case 3: Different URL
    url2 = "https://www.google.com"
    short2 = codec.encode(url2)
    decoded2 = codec.decode(short2)
    print(f"Original:  {url2}")
    print(f"Shortened: {short2}")
    print(f"Decoded:   {decoded2}")
    print(f"Match: {url2 == decoded2}\n")
    
    # Test other implementations
    print("=" * 50)
    print("Testing CodecCounter")
    print("=" * 50)
    codec_counter = CodecCounter()
    for i, url in enumerate([url1, url2, "https://example.com"]):
        short = codec_counter.encode(url)
        print(f"URL {i+1}: {short}")
    
    print("\n" + "=" * 50)
    print("Testing CodecHash")
    print("=" * 50)
    codec_hash = CodecHash()
    for url in [url1, url2]:
        short = codec_hash.encode(url)
        decoded = codec_hash.decode(short)
        print(f"Short: {short}")
        print(f"Decoded matches: {url == decoded}\n")
    
    print("=" * 50)
    print("Testing CodecBase62")
    print("=" * 50)
    codec_base62 = CodecBase62()
    for i in range(5):
        url = f"https://example.com/page{i}"
        short = codec_base62.encode(url)
        print(f"URL {i}: {short}")
