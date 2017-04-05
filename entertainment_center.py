# Udacity Introdution to Programming Nanodegree
# Stage 3 Project: Movies Website
# By Stephen Fox (with heavy assistance from Udacity!)

# Movie storylines are courtesy of www.imdb.com


# import media tells the program to use the contents of media.py

import media
import fresh_tomatoes

# Media.Movie() implies the class Movie inside the file called media
# Each movie listed below is an instance of the class Movie

bourne_identity = media.Movie("The Bourne Identity",
                              "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, before racing to elude assassins and regain his memory.",
                              "http://www.getbourneidentity.com/images/posters/bourne-identity-poster-2.jpg",
                              "https://www.youtube.com/watch?v=cD-uQreIwEk")

hurt_locker = media.Movie("The Hurt Locker",
                          "During the Iraq War, a Sergeant recently assigned to an army bomb squad is put at odds with his squad mates due to his maverick way of handling his work.",
                          "http://www.impawards.com/2009/posters/hurt_locker.jpg",
                          "https://www.youtube.com/watch?v=2GxSDZc8etg")

no_country = media.Movie("No Country for Old Men",
                         "Violence and mayhem ensue after a hunter stumbles upon a drug deal gone wrong and more than two million dollars in cash near the Rio Grande.",
                         "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                         "https://www.youtube.com/watch?v=YBqmKSAHc6w")

platoon = media.Movie("Platoon",
                      "A young recruit in Vietnam faces a moral crisis when confronted with the horrors of war and the duality of man.",
                      "http://ecx.images-amazon.com/images/I/51GecejycjL._AC_UL320_SR228,320_.jpg",
                      "https://www.youtube.com/watch?v=hGsyEkfjhQk")

shawshank = media.Movie("The Shawshank Redemption",
                        "Two imprisoned men bond over a number of years, " +
                        "finding solace and eventual redemption through acts of common decency.",
                        """http://topmoviesbygenre.com/wp-content/uploads/2015/01/the-shawshank-redemption-movie-poster-1994.jpg""",
                        "https://www.youtube.com/watch?v=NmzuHjWmXOc")

lost_ark = media.Movie("Raiders of the Lost Ark",
                       "Archaeologist and adventurer Indiana Jones is hired by the US government to find the Ark of the Covenant before the Nazis.",
                       "https://www.movieposter.com/posters/archive/main/157/MPW-78987",
                       "https://www.youtube.com/watch?v=gz4crpFaW4M")


movies = [bourne_identity, hurt_locker, no_country, platoon, shawshank, lost_ark]                            

# open_movies_page is a function inside fresh_tomatoes.py that generates
# a website from the preceding list of movies (function input)

fresh_tomatoes.open_movies_page(movies)
