#!/usr/bin/env python
import media
import fresh_tomatoes

print("Content-type:text/html \n")


rouge = media.Movie("rouge", "https://bit.ly/2wXTIuC",
                    "https://youtu.be/ii_KxlHcm3A")

tamasha = media.Movie("tamasha", "https://bit.ly/2ICJ2H5",
                      "https://youtu.be/o-e5eWVCzx8")

arya2 = media.Movie("arya2", "https://bit.ly/2KI2y1C",
                    "https://youtu.be/vpfXFqlLA3A")

ban = media.Movie("bharath ane nenu", "https://bit.ly/2rY9Abm",
                  "https://youtu.be/KMWS5y2gZ6E")

Rangasthalam = media.Movie("rangasthalam", "https://bit.ly/2KI5NGe",
                           "https://youtu.be/mhhb6JAJKbE")

# rangastalam.show_trailer()

movies = [rouge, tamasha, arya2, ban, Rangasthalam]
fresh_tomatoes.open_movies_pages(movies)
