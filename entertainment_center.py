#imports modules
#iMedia module creates defintion of the class function for Movie
#fresh_tomatoes renders the web page

import media
import fresh_tomatoes

#Create instances of favorite movies
terminator= media.Movie("Terminator", "The story of a cyborg sent back to change time","http://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg","http://youtu.be/c4Jo8QoOTQ4","1984","Arnold Schwarzenegger")
raiders= media.Movie("Raiders of the Lost Ark", "Man seeks adventure searching to the lost ark","http://upload.wikimedia.org/wikipedia/en/4/4b/Raiders.jpg","http://youtu.be/0ZOcoxjeUYo","1981","Harrison Ford")
force_awakens = media.Movie("Star Wars: The Force Awakens", "Rebirth of the Star Wars series","http://upload.wikimedia.org/wikipedia/en/2/28/Starwarsviitheforceawakens.jpg","http://youtu.be/erLk59H86ww","2015","John Boyega")
sniper = media.Movie("American Sniper", "Biography of an American Hero during the Iraq War","http://upload.wikimedia.org/wikipedia/en/1/10/American_Sniper_poster.jpg","http://youtu.be/99k3u9ay1gs","2015","Bradley Cooper")
shrek = media.Movie("Shrek", "Ugly Ogre sets out to save the princess","http://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg","http://youtu.be/jYejzdBwvY4","2001","Mike Meyers")


#Creating a list for passing to fresh_tomatoes
movies = [terminator,raiders,force_awakens,sniper,shrek]

#Calling fresh_tomatoes to create HTML and render page
fresh_tomatoes.open_movies_page(movies)
