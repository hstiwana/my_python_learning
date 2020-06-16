''' This is fun little program to deal with lists and showing use of "if elif else"
 it takes a single input and returns name of country based on its small database :)  '''
usa = [ "atlanta", "new york", "chicago", "baltimore"]
uk = ["london", "bristol", "cambridge"]
india = ["mumbai","delhi", "banglore"]

city = input('Please enter a city name: ')
if city in usa:
    print(f'This {city.capitalize()} belongs to USA')
elif city in uk:
    print(f'This {city.capitalize()} belongs to UK')
elif city in india:
    print(f'This {city.capitalize()} belongs to India')
else:
    print(f'Based on my little knowledge about cities, I am not sure what country {city.capitalize()} belongs to :( ')
