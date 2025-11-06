import requests
import time
from datetime import datetime
import movies

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.request_count = 0
    
    def get_headers(self):
        headers = {'Content-Type': 'application/json'}
        return headers
    
    def make_request(self, method='GET', data=None):
        headers = self.get_headers()
        
        self.request_count += 1
        print(f"Request #{self.request_count}: {method} {url}")
        
        if method == 'GET':
            response = requests.get(self.base_url, headers=headers)
        elif method == 'POST':
            response = requests.post(self.base_url, headers=headers, json=data)
        
        return response.json()


class CachedClient(APIClient):
    def __init__(self, base_url, cache_duration=300):
        super().__init__(base_url)
        self.cache = {}
        self.cache_duration = cache_duration  # seconds
    
    def make_request(self, method='GET', data=None):
        pass



# Main section

url = movies.url_for_movies('top_rated')
client = APIClient(url)
data = client.make_request()
print("\n")
[print(f"{movie['vote_average']}\t{movie['title']}") for movie in data['results']]

