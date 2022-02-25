## 1. Multiple Conditions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    # Complete code from here
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
avg_rating_free_games = sum(free_games_ratings) / len(free_games_ratings)
print(avg_rating_free_games)

## 2. The or Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    # Complete code from here
    
    if genre == 'Social Networking' or genre == 'Games':
        games_social_ratings.append(rating)

avg_games_social = sum(games_social_ratings) / len(games_social_ratings)
print(avg_games_social)

## 3. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

not_free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price != 0:
        not_free_games_social_ratings.append(rating)
        
avg_not_free = sum(not_free_games_social_ratings) / len(not_free_games_social_ratings)

# Not-free apps (average)
print(avg_not_free)

## 4. Comparison Operators ##

x = -6
y = 14
z = 8.5

if x > z:
    print('x is greater than z.')
if y != z:
    print('y is not equal to z')
if z > x and z < y:
    print('z is between x and y')

## 5. Comparison Operator Applications ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

ratings = []
n_apps_more_9 = 0
n_apps_less_9 = 0
for element in apps_data[1:]:
    price = float(element[4])
    if price > 9.0:
        rating = float(element[7])
        ratings.append(rating)
        
avg_rating = sum(ratings) / len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = (len(apps_data) -1) - n_apps_more_9
print('Average rating: ', avg_rating)
print('apps have a price greater than $9: ', n_apps_more_9)
print('apps have a price less than or equal to $9: ', n_apps_less_9)

## 6. The else Clause ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    else:
        app.append('not free')
apps_data[0].append('free_or_not')
print(apps_data[:5])

## 7. The elif Clause ##

app_ratings = [['Facebook', 3.5], ['Notion', 4.0], ['Astropad Standard', 4.5], ['NAVIGON Europe', 3.5]]

for element in app_ratings:
    rating = float(element[1])
    if rating < 3.0:
        element.append('below average')
    elif rating >= 3.0 and rating < 4.0:
        element.append('roughly average')
    elif rating >= 4.0:
        element.append('better than average')
print(app_ratings)

## 8. Else vs. elif ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    # Complete code from here
    if price == 0.0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price >= 20 and price < 50:
        app.append('expensive')
    elif price >= 50:
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[:5])