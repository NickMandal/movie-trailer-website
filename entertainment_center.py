import fresh_tomatoes
import json
import media
import requests

image_url = "https://image.tmdb.org/t/p/w500"
trailer_url= "https://www.youtube.com/watch?v="

def create_movie(id):
  url = "https://api.themoviedb.org/3/movie/%s?api_key=a04cb5827933e112089c0827a6fbf635&append_to_response=videos,releases" % id
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
  movie = media.Movie(title, overview, image, trailer, runtime, genre, content_rating, rating, release_date)
  return movie

concussion = create_movie(321741)
why_him = create_movie(356305)
suicide_squad = create_movie(297761)
the_social_network = create_movie(37799)
dope = create_movie(308639)
end_of_watch = create_movie(77016)

movies = [concussion, why_him, suicide_squad, the_social_network, dope, end_of_watch]
fresh_tomatoes.open_movies_page(movies)
