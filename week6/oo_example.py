import requests
import time
from datetime import datetime
import movies

class APIClient:
    def __init__(self):
        self.base_url = None
        self.request_count = 0
    
    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        return headers
    
    def make_request(self, url, method='GET', data=None):
        self.base_url = url
        headers = self.get_headers()
        
        self.request_count += 1
        print(f"Request #{self.request_count}: {method} {url}")
        
        if method == 'GET':
            response = requests.get(self.base_url, headers=headers)
        elif method == 'POST':
            response = requests.post(self.base_url, headers=headers, json=data)
        
        return response.json()


class CachedClient(APIClient):
    def __init__(self, cache_duration=300):
        super().__init__()
        self.cache = {}
        self.cache_duration = cache_duration  # seconds
    
    def make_request(self, url, method='GET', data=None):
        pass



client = APIClient()

url = movies.url_for_movies('top_rated')
data = client.make_request(url)
print("\n")
[print(f"{movie['vote_average']}\t{movie['title']}") for movie in data['results']]

url = movies.url_for_movies('now_playing')
data = client.make_request(url)
print("\n")
[print(f"{movie['vote_average']}\t{movie['title']}") for movie in data['results']]
