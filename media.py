#imports modules
#webbrowser module provides a high-level interface to allow displaying Web-based documents to users
#Documentation:  https://docs.python.org/2/library/webbrowser.html
import webbrowser

#Creates movie class with arguments:  movie title, poster art, trailer, date released and key actor
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,release_date,star):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date=release_date
        self.star = star
        
#Function used to intiate playback of trailer based on a URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
