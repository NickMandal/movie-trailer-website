import fresh_tomatoes
import json
import media
import requests

image_url = "https://image.tmdb.org/t/p/w500"
trailer_url= "https://www.youtube.com/watch?v="

url = "https://api.themoviedb.org/3/movie/321741?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
print(data)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

concussion = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date) 

url = "https://api.themoviedb.org/3/movie/356305?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

why_him = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date)

url = "https://api.themoviedb.org/3/movie/297761?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

suicide_squad = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date)

url = "https://api.themoviedb.org/3/movie/37799?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

the_social_network = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date) 

url = "https://api.themoviedb.org/3/movie/308639?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

dope = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date)

url = "https://api.themoviedb.org/3/movie/77016?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases"
response = requests.get(url)
data = json.loads(response.text)
title = data["original_title"]
overview = data["overview"]
image = image_url + data["poster_path"]
trailer = trailer_url + data["videos"]["results"][0]["key"]
runtime = data["runtime"]
genre = data["genres"][0]["name"]
content_rating = data["releases"]["countries"][0]["certification"]
rating = data["vote_average"]
release_date = data["release_date"]

end_of_watch = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date) 


movies = [concussion, why_him, suicide_squad, the_social_network, dope, end_of_watch]
fresh_tomatoes.open_movies_page(movies)
