import media
from ud036_StarterCode import fresh_tomatoes

movie_details = {"toy_story":{"title":"Toy Story",
				"storyline":"A story of a boy and his toys that come to life",
				"poster_image_url":"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=bbmzuoBC1Rs"},
				"transcendence":{"title":"Transcendence",
				"storyline":"A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
				"poster_image_url":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=VCTen3-B8GU"}}
movies = []
for key, movie_detail in movie_details.items():
	movies.append(media.Movie(movie_detail['title'], movie_detail['storyline'], movie_detail['poster_image_url'], movie_detail['trailer_youtube_url']))
fresh_tomatoes.open_movies_page(movies)

