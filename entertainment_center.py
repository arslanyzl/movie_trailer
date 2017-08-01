import fresh_tomatoes
import media


# media file movie structure
# Repeating for every movie
inception = media.Movie("Inception",
                        "",
                        "https://goo.gl/Rr3zQ2",
                        "https://www.youtube.com/watch?v=E1iqGiX0lSg")

spider_man = media.Movie("Spider-Man",
                         "Homecoming",
                         "https://goo.gl/AZnLA8",
                         "https://www.youtube.com/watch?v=39udgGPyYMg")

king_arthur = media.Movie("King Arthur",
                          "Legend of the sword",
                          "https://goo.gl/w8QYpQ",
                          "https://www.youtube.com/watch?v=jIM4-HLtUM0")

wonder_woman = media.Movie("Wonder Woman",
                           "Rise of the Warrior",
                           "https://goo.gl/LKJmiF",
                           "https://www.youtube.com/watch?v=VSB4wGIdDwo")

mad_max = media.Movie("Mad Max",
                      "Fury Road",
                      "https://goo.gl/wQ7gsi",
                      "https://www.youtube.com/watch?v=hEJnMQG9ev8")

pirates = media.Movie("Pirates of the Caribbean",
                      "Dead Men Tell No Tales",
                      "https://goo.gl/LLbMxQ",
                      "https://www.youtube.com/watch?v=Hgeu5rhoxxY")

# Creates an array of movies
movies = [inception, spider_man, king_arthur, wonder_woman, mad_max, pirates]

# Call to open the generated fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)
