# -*- coding: utf-8 -*-
# Import the instance methods needed to run our website

import fresh_tomatoes
import media

# Creating instance of our Movie class containing Title, Storyline, Poster image and Trailer URL of my favorite Movies

sallskapsresan = media.Movie("Sällskapsresan",
                             "Följ Stig-Helmer på hans resa till Kanarieöarna",
                             "https://mz-prod.s3.amazonaws.com/uploads/photo/file/73087/original.jpg",
                             "https://youtu.be/T4m2rBqTFDo")

avatar = media.Movie ("Avatar",
                      "A marine on an alien planet",
                      "http://ecx.images-amazon.com/images/I/41vuODnDSuL.jpg",
                      "https://youtu.be/5PSNL1qE6VY")

blues_brothers = media.Movie ("Blues Brothers",
                              "Follow the Blues Brothers on their journey to save a children's home",
                              "http://cdn.traileraddict.com/content/universal-pictures/blues_brothers-4.jpg",
                              "https://youtu.be/ma-rkV6wVJM")

lord_of_the_rings = media.Movie ("Lord of the Rings",
                             "Follow Frodo on his dangerous journey to destroy the Ring to rule them all.",
                             "http://www.movieartarena.com/imgs/lotr1final.jpg",
                             "https://youtu.be/V75dMMIW2B4")

woman_in_red = media.Movie ("The Woman in Red",
                           "Teddy Pierce falls in love with a Mysterious woman in Red threatening to destroy his long time marriage.",
                           "https://70srichard.files.wordpress.com/2014/08/the-woman-in-red-movie-poster-1984-1020195918.jpg",
                           "https://youtu.be/JDHhDanYAcQ")

star_wars = media.Movie ("Star Wars",
                        "An adventure far out in the sky many years from now!",
                        "http://screenrant.com/wp-content/uploads/star-wars-episode-7-image.jpg",
                        "https://youtu.be/vP_1T4ilm8M")

# generate a list 'movies' containing the above instances

movies = [sallskapsresan, avatar, blues_brothers, lord_of_the_rings, woman_in_red, star_wars]

# generate the webpage with trailers

fresh_tomatoes.open_movies_page(movies)


