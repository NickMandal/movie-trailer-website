import fresh_tomatoes
import media
import tmdbsimple as tmdb
tmdb.API_KEY = 'a04cb5827933e112089c0827a6fbf635'

concussion = media.Movie("Concussion",
                         "A forensic pathologist who fights against the National Football League trying to surpress his research on brain degeneration suffered by professional football players.",
                         "https://upload.wikimedia.org/wikipedia/en/e/ee/Concussion_poster.jpg",
                         "https://www.youtube.com/watch?v=Io6hPdC41RM")

why_him = media.Movie("Why Him?",
                      "This film follows a father who is horrified by his daughter's new boyfriend, an unconventional Silicon Valley entrepreneur.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a1/Why_Him.png",
                      "https://www.youtube.com/watch?v=CO6qLC4cL8E")

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency led by Amanda Waller recruits imprisoned supervillains to execute dangerous black ops missions and save the world from a powerful threat, in exchange for leaner sentences.",
                            "https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png",
                            "https://www.youtube.com/watch?v=CmRih_VtVAs")

wedding_crashers = media.Movie("The Social Network",
                               "This film portrays the founding of social networking website Facebook and the resulting lawsuits.",
                               "https://upload.wikimedia.org/wikipedia/en/7/7a/Social_network_film_poster.jpg",
                               "https://www.youtube.com/watch?v=lB95KLmpLR4")

dope = media.Movie("Dope",
                   "High-school senior Malcolm and his friends Jib and Diggy bond over '90s hip-hop culture, their studies and playing music in their own punk band. A chance encounter with a drug dealer named Dom lands Malcolm and company at the dealer's nightclub birthday party; when the scene turns violent, they flee -- with the Ecstasy that Dom secretly hid in Malcolm's backpack. A wild adventure ensues as the youths try to evade armed thugs who want the stash.",
                   "https://upload.wikimedia.org/wikipedia/en/d/d2/DopeTeaserPoster.jpg",
                   "https://www.youtube.com/watch?v=strEm9amZuo")

end_of_watch = media.Movie("End of Watch",
                           "Brian Taylor and Miguel Zavala, two Los Angeles Police Department officers who work in South Los Angeles. The film focuses on their day-to-day police work, their dealings with a certain group of gang members, and their personal relationships.",
                           "https://upload.wikimedia.org/wikipedia/en/6/64/End_of_Watch_Poster.jpg",
                           "https://www.youtube.com/watch?v=mf2K9GzgiF0")

movies = [concussion, why_him, suicide_squad, wedding_crashers, dope, end_of_watch]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
