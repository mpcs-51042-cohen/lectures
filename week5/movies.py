import requests
import base64

# Here are some helpful functions.

def getApiKey(): 
  return base64.b64decode('YmRlMDI0ZjNlYjQzZjU5N2FhZmUwMWVkOWM5MDk4YzY=').decode()

# Resource can be "top_rated" or "now_playing"
def url_for_movies(resource):
  apiKey = f"api_key={getApiKey()}"
  language = "language=en-US"
  region = "region=US"
  filter = "include_adult=false"
  base_url = f"https://api.themoviedb.org/3/movie/{resource}"
  return f"{base_url}?{apiKey}&{language}&{region}&{filter}"


# Pass in the movie title or keyword to search for
def url_for_search(keyword):
  apiKey = f"api_key=${getApiKey()}"
  language = "language=en-US"
  search = f"query={keyword}"
  region = "region=US"
  filter = "include_adult=false"
  base_url = "https://api.themoviedb.org/3/search/movie"
  return f"{base_url}?{apiKey}&{search}&{language}&{region}&{filter}"


# Example Usage

url = url_for_movies('top_rated') # now_playing
print("Calling", url)

response = requests.get(url)

if response.status_code == 200:
  results = response.json()
  print("Got results!")
  titles = [movie['title'] for movie in results['results']]
  for title in titles:
    print(title)
  
  # TO DO:
  # Display movie titles and rating + whatever else seems interesting
  
else:
  print("Request failed", response.status_code)

