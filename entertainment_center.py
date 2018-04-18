import media  # import media file/module containing Movie class
import fresh_tomatoes

# Creating instances of movies based on Movie class
die_hard = media.Movie("Die Hard",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_"
                       "hard.jpg",
                       "https://www.youtube.com/watch?v=QIOX44m8ktc")

analyze_this = media.Movie("Analyze This",
                           "https://upload.wikimedia.org/wikipedia/en/d/d1/An"
                           "alyze_this.jpg",
                           "https://www.youtube.com/watch?v=rS-5L1-7BY4")

alien = media.Movie("Alien",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_mov"
                    "ie_poster.jpg",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

get_out = media.Movie("Get Out",
                      "https://upload.wikimedia.org/wikipedia/en/e/eb/"
                      "Teaser_poster_for_2017_film_Get_Out.png",
                      "https://www.youtube.com/watch?v=sRfnevzM9kQ")

davinci_code = media.Movie("The Da Vinci Code",
                           "https://upload.wikimedia.org/wikipedia/en"
                           "/6/6b/DaVinciCode.jpg",
                           "https://www.youtube.com/watch?v=lfqHb6INj3w")

forgetting_sarah_marshall = media.Movie("Forgetting Sarah Marshall",
                                        "https://upload.wikimedia.org/"
                                        "wikipedia/en/7/7c/Forget"
                                        "ting_sarah_marshall_ver2.jpg",
                                        "https://www.youtube.com/"
                                        "watch?v=K4xD8ZMdJms")

movies = [die_hard, analyze_this, alien, get_out,
          davinci_code, forgetting_sarah_marshall]

fresh_tomatoes.open_movies_page(movies)
# Runs function to open movie page/HTML in browser
