#!/usr/bin/env python
import webbrowser
"""class movie():
it is a class object in this there are three
variables they are
movie_title
poster_image
trailer_youtube"""

class Movie():
    def __init__(self, movie_title,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
