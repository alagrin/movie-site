class Movie():  # create class Movie with constructor containing arguments
    """ This class creates the Movie class to define each movie's parameters
    Attributes:
       title (str): Movie instance title.
       poster_image_url (str): Movie poster pic.
       trailer_youtube_url (str): Movie trailer link.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url