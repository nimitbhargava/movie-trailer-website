import webbrowser


# Class definition for Movie
class Movie():
    """
	This class when initialized require movie title, storyline, poster imag
	e url, and youtube trailer link.
	"""
    def __init__(self, movie_title, movie_storyline, poster_image_url,
                trailer_youtube):
        """
        Initialize movie title, storyline, poster image url, and youtube trail
        er link of the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """opens the youtube trailer url in the default browser.opens the yout
    	ube trailer url in the default browser."""
        webbrowser.open(self.trailer_youtube_url)

