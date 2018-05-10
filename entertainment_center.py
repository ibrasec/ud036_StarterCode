#!/usr/bin/env python
"""
This module is used to create a list of movie instances that fresh_tomatoes
module needs as input to its open_movies_page() function in order to build the
HTML file, so that a website is produced showing the favorite movies.
"""

import media
import fresh_tomatoes


# creating last_smaurai instance
last_samurai = media.Movie("The Last Samurai",
                           "An American military officer training japan's first army in the art of modern warfare.",
                           "https://i.pinimg.com/originals/1e/bd/c1/1ebdc14e46f452eacb9bcf6b331d09ed.jpg",
                           "https://www.youtube.com/watch?v=T50_qHEOahQ")


# creating the_gladiator instance
the_gladiator = media.Movie("The Gladiator",
                            "The story of a once-powerful general forced to become a common gladiator.",
                            "https://www.movieposter.com/posters/archive/main/22/A70-11370",
                            "https://www.youtube.com/watch?v=AxQajgTyLcM")


# creating the_matrix instance
the_matrix = media.Movie("The Matrix",
                         "a computer programmer Neo, who is contacted by two hackers escaped from the matrix",
                         "https://consequenceofsound.files.wordpress.com/2018/03/the-matrix-4k.png?w=807",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")


# defining a list of movies to be called by fresh_tomatoes module
movies = [last_samurai, the_gladiator, the_matrix]


if __name__ == "__main__":
    fresh_tomatoes.open_movies_page(movies)
