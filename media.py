#!/usr/bin/env python
"""
This module it is used to allow creating a class instance for any movie, so
that it could be added later to the list of favorite movies passed to the
fresh_tomatoes moduel.

Each movie should have the following attributes passed as arguments:
- movie's title.
- movie's storyline.
- movie's poster image.
- movie's Youtube URL.

to use this module, you could simply import it using the import line of code

Example:
    import media
    x = media.Movie(*args)
"""

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ The contructor method for the Movie class

        Args:
            movie_title (str): a movie title.
            movie_storyline (str): a short story line for the passed movie.
            poster_image (str): an html link to the poster image of the passed movie.
            trailer_youtube (str): a youtube link for the movie trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
