class Movie():  # create class Movie with constructor containing arguments
    """ This creates the Movie class to define each movie's parameters"""

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

# creating space in memory for these variables
