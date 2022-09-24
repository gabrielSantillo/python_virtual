import wikipedia

try:
    city = wikipedia.page(input("Which city do you wanna see?\n"))
    print(city.title)
    print(city.content)
except wikipedia.exceptions.PageError:
    print("This city is invalid. \nTry again.")
