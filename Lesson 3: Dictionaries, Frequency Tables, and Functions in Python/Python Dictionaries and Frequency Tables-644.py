## 1. Checking for Membership ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}

is_in_dictionary_1 = '9+' in content_ratings
is_in_dictionary_2 = 987 in content_ratings

if '17+' in content_ratings:
    result = "It exists"
    print(result)
    
print(is_in_dictionary_1)
print(is_in_dictionary_2)

## 2. Updating Dictionary Values ##

content_ratings = {'4+': 622, '12+': '1155', '9+': 987, '17+': 4433}
temp = content_ratings['4+']
content_ratings['4+'] = content_ratings['17+']
content_ratings['17+'] = temp
content_ratings['12+'] = int(content_ratings['12+'])

print(content_ratings)

## 3. Counting with Dictionaries ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {'4+': 0, '9+': 0, '12+': 0, '17+': 0}
ratings = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']

for element in apps_data[1:]:
    c_rating = element[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)
            

## 4. Finding the Unique Values ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

content_ratings = {}

for element in apps_data[1:]:
    c_rating = element[10]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
    else:
        content_ratings[c_rating] = 1

print('Final dictionary:')
print(content_ratings)

## 5. Proportions and Percentages ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

genre_counting = {}
for element in apps_data[1:]:
    genre = element[11]
    if genre in genre_counting:
        genre_counting[genre] += 1
    else:
        genre_counting[genre] = 1
print(genre_counting)

## 6. Looping over Dictionaries ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
percentage_17_plus= 0
percentage_15_allowed= 0

for key in content_ratings:
    content_ratings[key] /= total_number_of_apps
    content_ratings[key] *= 100
    if key == '17+':
        percentage_17_plus= content_ratings[key]
    if key == '4+'or key == '12+'or key == '9+':
        percentage_15_allowed +=content_ratings[key]

print(content_ratings)
print("Percentage of apps that have a content rating of '17+': ", percentage_17_plus)
print("Percentage of apps that a 15-year-old can download: ", percentage_15_allowed)

## 7. Keeping the Dictionaries Separate ##

content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197


c_ratings_proportions = {}
c_ratings_percentages = {}
for key in content_ratings:
    proportion = (content_ratings[key] / total_number_of_apps)     
    c_ratings_proportions[key] = proportion
    percentage = (c_ratings_proportions[key] * 100)
    c_ratings_percentages[key] = percentage
print("Proportions: ", c_ratings_proportions)
print("Percentages: ", c_ratings_percentages)

## 8. Frequency Tables for Numerical Columns ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

data_sizes = []
for element in apps_data[1:]:
    size = float(element[2])
    data_sizes.append(size)
min_size = min(data_sizes)
max_size = max(data_sizes)

print(min_size)
print(max_size)
print(data_sizes)