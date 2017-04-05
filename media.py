# Udacity Introdution to Programming Nanodegree
# Stage 3 Project: Movies Website
# By Stephen Fox (with heavy assistance from Udacity!)

import webbrowser


class Movie():
    """This class provides a way to store movie related information"""    
    
    # The __init__ function initializes an instance of class Movie (e.g. Hurt Locker)
    # Inputs are the movie title, storyline, poster image and trailer video

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # show_trailer opens the You Tube trailer for the movie instance

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
