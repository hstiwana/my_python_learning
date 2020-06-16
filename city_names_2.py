''' This is fun little program to deal with lists and showing use of "if elif else"
 it takes a 2 city names as input and returns name of country based on its small database :)  '''
usa = [ "atlanta", "new york", "chicago", "baltimore"]
uk = ["london", "bristol", "cambridge"]
india = ["mumbai","delhi", "banglore"]

city1 = input('Please enter first city name: ')
city2 = input('Please enter second city name: ')
if city1 in usa and city2 in usa:
    print(f'{city1.capitalize()} and {city2.capitalize()} both are in USA')
elif city1 in uk and city2 in uk:
    print(f'{city1.capitalize()} and {city2.capitalize()} both are in UK')
elif city1 in india and city2 in india:
    print(f'{city1.capitalize()} and {city2.capitalize()} both are in India')
else:
    print(f'Based on my little knowledge about cities, I am not sure what country {city1.capitalize()} or {city2.capitalize()} belongs to :( ')
