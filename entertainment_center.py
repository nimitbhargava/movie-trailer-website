import media
import fresh_tomatoes

# Saving movie details in dictionary
movie_details = {"narnia": {"title": "The Chronicles of Narnia",
                            "storyline": "While playing, Lucy and her siblings"
                            "find a wardrobe that lands them in a mystical pla"
                            "ce called Narnia. Here they realise that it was f"
                            "ated and they must now unite with Aslan to defeat"
                            " an evil queen.",
                            "poster_image_url": "https://upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg",  # noqa
                            "trailer_youtube_url": "https:/ /upload.wikimedia.org/wikipedia/en/1/10/The_Chronicles_of_Narnia_-_The_Lion%2C_the_Witch_and_the_Wardrobe.jpg"},  # noqa
                 "transcendence": {"title": "Transcendence",
                                   "storyline": "A scientist's drive for artif"
                                   "icial intelligence, takes on dangerous imp"
                                   "lications when his consciousness is upload"
                                   "ed into one such program.",
                                   "poster_image_url": "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc1MjQ3ODAyOV5BMl5BanBnXkFtZTgwNjI1NDQ0MTE@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",  # noqa
                                   "trailer_youtube_url": "https://www.youtube.com/watch?v=VCTen3-B8GU"},  # noqa
                 "limitless": {"title": "Limitless",
                               "storyline": "Eddie, dismayed by his bleak futu"
                               "re, is urged to try a drug that gives him a ra"
                               "zor-sharp mind. As he rises in the corporate w"
                               "orld, he also attracts the attention of a few "
                               "negative elements.",
                               "poster_image_url": "http://t1.gstatic.com/images?q=tbn:ANd9GcQSJVRsIEFYFBlTfJAygejBNdbFFlvOEShCKNeeYMSEqwyFtyW0",  # noqa
                               "trailer_youtube_url": "https://www.youtube.com/watch?v=jOLqNOfzus4"},  # noqa
                 "ratatouille": {"title": "Ratatouille",
                                 "storyline": "Remy, a rat, aspires to become "
                                 "a renowned French chef. He doesn't realise t"
                                 "hat people despise rodents and will never en"
                                 "joy a meal cooked by him.",
                                 "poster_image_url": "http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg",  # noqa
                                 "trailer_youtube_url": "https://www.youtube.com/watch?v=c3sBBRxDAqk"},  # noqa
                 "vertigo": {"title": "Vertigo",
                             "storyline": "Detective Scottie who suffers from "
                             "acrophobia is hired to investigate the strange a"
                             "ctivities of an old friend's wife. She commits s"
                             "uicide while Scottie becomes dangerously obsesse"
                             "d with her.",
                             "poster_image_url": "http://t0.gstatic.com/images?q=tbn:ANd9GcQ6PhsSTM1eMgrEQKc4qdy9Ds6ES7xTdvsRABLmqkI5iEQA_lM1",  # noqa
                             "trailer_youtube_url": "https://www.youtube.com/watch?v=Z5jvQwwHQNY"}}  # noqa
movies = []

# Looping through the movies to build their object and saving them in an array
for key, movie_detail in movie_details.items():
    movies.append(media.Movie(movie_detail['title'],
                              movie_detail['storyline'],
                              movie_detail['poster_image_url'],
                              movie_detail['trailer_youtube_url']))
fresh_tomatoes.open_movies_page(movies)
