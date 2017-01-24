import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="styles.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="script.js"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Nick Mandal's Fresh Tomatoes</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center">
    <h2>{movie_title} <div class="lead">({movie_release_year})</div></h2>
    <img src="{poster_image_url}" width="220" height="342">
    <h3>
    <span style="font-size:0.8em;"class="glyphicon glyphicon-star" aria-hidden="true"></span> {movie_rating}
    </h3>
    <button type="button" class="btn btn-danger trailer" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">Watch Trailer</button>
    <button type="button" class="btn btn-info" data-toggle="modal" data-target="#{trailer_youtube_id}" id="movieInfo">Movie Information</button>    

    <!-- Movie Information Modal -->
    <div class="modal fade" id="{trailer_youtube_id}">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header" style="text-align: center;">
                  <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  <div id="title"><h3 class="modal-title">{movie_title}</h3></div>
                  <div id="title"><h3 style="opacity: 0.6; font-size: 1.2em; font-weight: 400;">({movie_release_year})</h3></div>
                </div>
                <div class="modal-body row">
                    <div class="col-xs-5">
                        <img src="{poster_image_url}" class="img-responsive" width="220" height="342">
                    </div>
                    <div class="col-xs-7">
                        <p>
                            <strong>
                                <bdi>Overview: </bdi>
                            </strong>
                            {movie_overview}
                        </p>
                        <p>
                            <strong>
                                <bdi>Genre: </bdi>
                            </strong>
                            {movie_genre}
                        </p>
                        <p>
                            <strong>
                                <bdi>Rating: </bdi>
                            </strong>
                            {content_rating}
                        </p>
                        <p>
                            <strong>
                                <bdi>Runtime: </bdi>
                            </strong>
                            {movie_runtime} minutes
                        </p>
                    </div>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</div>

'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_overview=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_runtime=movie.movie_duration,
            movie_genre=movie.movie_genre,
            content_rating=movie.rating,
            movie_rating=movie.movie_rating,
            movie_release_year=movie.release_year
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
