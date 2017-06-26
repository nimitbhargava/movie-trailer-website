import media
from ud036_StarterCode import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=bbmzuoBC1Rs")

transcendence = media.Movie("Transcendence",
                            "A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
                            "https://www.youtube.com/watch?v=VCTen3-B8GU")
movies = [toy_story, transcendence]
fresh_tomatoes.open_movies_page(movies)

