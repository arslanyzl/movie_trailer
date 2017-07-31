import fresh_tomatoes
import media


# media file movie structure (self, movie_title, movie_storyline, poster_image, trailer_youtube)
# Repeating for every movie
inception = media.Movie("Inception",
                        "",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=E1iqGiX0lSg")

spider_man = media.Movie("Spider-Man",
                         "Homecoming",
                         "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
                         "https://www.youtube.com/watch?v=39udgGPyYMg")

king_arthur = media.Movie("King Arthur",
                          "Legend of the sword",
                          "https://upload.wikimedia.org/wikipedia/en/a/a4/King_Arthur_LotS_poster.jpg",
                          "https://www.youtube.com/watch?v=jIM4-HLtUM0")

wonder_woman = media.Movie("Wonder Woman","Rise of the Warrior",
                           "https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

mad_max = media.Movie("Mad Max",
                      "Fury Road",
                      "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

pirates = media.Movie("Pirates of the Caribbean",
                      "Dead Men Tell No Tales",
                      "https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
                      "https://www.youtube.com/watch?v=Hgeu5rhoxxY")

#Creates an array of movies
movies = [inception, spider_man, king_arthur, wonder_woman, mad_max, pirates]

#Call to open the generated fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)

