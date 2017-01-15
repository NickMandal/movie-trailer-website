import fresh_tomatoes
import json
import media
import requests

# Pulls information from tmdb and parses it to get desired information
def create_movie(id):
  image_url = "https://image.tmdb.org/t/p/w500"
  trailer_url= "https://www.youtube.com/watch?v="
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
  release_date = data["release_date"].partition('-')[0]
  movie = media.Movie(title, overview, image, trailer, runtime, genre, 
                      content_rating, rating, release_date)
  return movie

# Creates the movies by passing in tmdb number
concussion = create_movie(321741)
why_him = create_movie(356305)
suicide_squad = create_movie(297761)
the_social_network = create_movie(37799)
dope = create_movie(308639)
end_of_watch = create_movie(77016)
i_am_legend = create_movie(6479)
the_imitation_game = create_movie(205596)
snowden = create_movie(302401)

# Create an array of all the movies
movies = [concussion, why_him, suicide_squad, the_social_network, dope, 
end_of_watch, i_am_legend, the_imitation_game, snowden]

# Pass the movies into the webpage
fresh_tomatoes.open_movies_page(movies)
