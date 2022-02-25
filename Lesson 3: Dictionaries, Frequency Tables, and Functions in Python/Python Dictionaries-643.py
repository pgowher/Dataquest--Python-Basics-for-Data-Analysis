## 1. Storing Data ##

content_ratings = ['4+', '9+', '12+', '17+']
numbers = [4433, 987, 1155, 622]
content_rating_numbers = [content_ratings, numbers]
print(content_rating_numbers)

## 2. Dictionaries ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
print(content_ratings)

## 3. Indexing ##

content_ratings = {'4+': 4433, '9+': 987, '12+': 1155, '17+': 622}
over_9 = content_ratings['9+']
over_17 = content_ratings['17+']
print(over_9)
print(over_17)

## 4. Alternative Method of Creating a Dictionary ##

content_ratings = {} 
content_ratings['4+'] = 4433
content_ratings['9+'] = 987
content_ratings['12+'] = 1155
content_ratings['17+'] = 622
over_12_n_apps = content_ratings['12+']
print(over_12_n_apps)

## 5. Key-Value Pairs ##

{4: 'four',
1.5: 'one point five',
'string_key': 'string_value',
4: 'True',
6: 'a list',
7: 'a dictionary'
}
error = True

## 6. Key-Value Pairs Continued ##

d_1 = {'key_1': 'first_value', 
 'key_2': 2,
 'key_3': 3.14,
 'key_4': True,
 'key_5': [4,2,1],
 'key_6': {'inner_key' : 6}
 }

print(d_1)