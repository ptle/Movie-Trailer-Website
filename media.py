import webbrowser

class Movie():
    """ This class provides a way to store movie related information """

    #Constructor for Movie object
    def __init__(self, movie_title, movie_storyline,
    poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #Method to display the trailer of movie object
    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
