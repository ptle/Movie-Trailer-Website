import media
import fresh_tomatoes
import urllib
import json

# List of names of my favorite movies
favorite_movie_names = ["500 Days of Summer", "Lilo & Stitch", "WALL-E",
                        "Hercules", "The Dark Knight", "Inception"]
# List of trailers in corresponding indices of names
trailers = ["https://www.youtube.com/watch?v=PsD0NpFSADM",
            "https://www.youtube.com/watch?v=hu9bERy7XGY",
            "https://www.youtube.com/watch?v=ZisWjdjs-gM",
            "https://www.youtube.com/watch?v=ZvtspevZxpg",
            "https://www.youtube.com/watch?v=EXeTwQWrcwY",
            "https://www.youtube.com/watch?v=8hP9D6kZseM"]

# Empty list that movie objects will be appended to
favorite_movies = []

# Repeats process for all movies in list
for index in range(len(favorite_movie_names)):

    # Four variables that will be used to construct movie object
    title = favorite_movie_names[index]
    storyline = ""
    image = ""
    url = trailers[index]

    # Opens connection to Open Movie Database API
    connection = urllib.urlopen("http://www.omdbapi.com/?t="
                                + favorite_movie_names[index])
    # Loads the API call into JSON and pulls the plot and poster from data
    output = json.load(connection)
    storyline = output["Plot"]
    image = output["Poster"]

    # Close connection
    connection.close()

    # Appends movie object with necessaey parameters into favorite_movies list
    favorite_movies.append(media.Movie(title, storyline, image, url))

# Used to check to make sure contents of movies are correct
"""
for movie in favorite_movies:
    movie.debug()
"""

# Calles open_movies_page method from fresh_tomatoes using favorite_movies list
fresh_tomatoes.open_movies_page(favorite_movies)
