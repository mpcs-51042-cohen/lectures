import base64

def url_for_movies(resource):
  apiKey = f"api_key={getMoviesApiKey()}"
  language = "language=en-US"
  region = "region=US"
  filter = "include_adult=false"
  base_url = f"https://api.themoviedb.org/3/movie/{resource}"
  return f"{base_url}?{apiKey}&{language}&{region}&{filter}"

def getMoviesApiKey(): 
  return base64.b64decode('YmRlMDI0ZjNlYjQzZjU5N2FhZmUwMWVkOWM5MDk4YzY=').decode()
