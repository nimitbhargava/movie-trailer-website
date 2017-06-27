import media
from ud036_StarterCode import fresh_tomatoes

movie_details = {"narnia":{"title":"The Chronicles of Narnia",
				"storyline":"While playing, Lucy and her siblings find a wardrobe that lands them in a mystical place called Narnia. Here they realise that it was fated and they must now unite with Aslan to defeat an evil queen.",
				"poster_image_url":"https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",
				"trailer_youtube_url":"https:/	/upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg"},
				"transcendence":{"title":"Transcendence",
				"storyline":"A scientist's drive for artificial intelligence, takes on dangerous implications when his consciousness is uploaded into one such program.",
				"poster_image_url":"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=VCTen3-B8GU"},
				"limitless":{"title":"Limitless",
				"storyline":"Eddie, dismayed by his bleak future, is urged to try a drug that gives him a razor-sharp mind. As he rises in the corporate world, he also attracts the attention of a few negative elements.",
				"poster_image_url":"http://t1.gstatic.com/images?q=tbn:ANd9GcQSJVRsIEFYFBlTfJAygejBNdbFFlvOEShCKNeeYMSEqwyFtyW0",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=jOLqNOfzus4"},
				"ratatouille":{"title":"Ratatouille",
				"storyline":"Remy, a rat, aspires to become a renowned French chef. He doesn't realise that people despise rodents and will never enjoy a meal cooked by him.",
				"poster_image_url":"http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=c3sBBRxDAqk"},
				"vertigo":{"title":"Vertigo",
				"storyline":"Detective Scottie who suffers from acrophobia is hired to investigate the strange activities of an old friend's wife. She commits suicide while Scottie becomes dangerously obsessed with her.",
				"poster_image_url":"http://t0.gstatic.com/images?q=tbn:ANd9GcQ6PhsSTM1eMgrEQKc4qdy9Ds6ES7xTdvsRABLmqkI5iEQA_lM1",
				"trailer_youtube_url":"https://www.youtube.com/watch?v=Z5jvQwwHQNY"}}
movies = []
for key, movie_detail in movie_details.items():
	movies.append(media.Movie(movie_detail['title'], movie_detail['storyline'], movie_detail['poster_image_url'], movie_detail['trailer_youtube_url']))
fresh_tomatoes.open_movies_page(movies)