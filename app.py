import webbrowser
import wikipedia

try:
    city = wikipedia.page(input("Which city do you wanna see?\n"))
    print(city.title)
    print(city.content)
    webbrowser.open(city.url)
except wikipedia.exceptions.PageError:
    print("This city is invalid. \nTry again.")
except:
    print("Sorry, something went wrong. The appropriate person has been notified.")
