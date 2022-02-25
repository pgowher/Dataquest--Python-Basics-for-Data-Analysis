## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]

sum_manual = 0
for element in a_list:
    sum_manual += element
print(sum_manual)
print(sum(a_list))

## 2. Built-In Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings = {}
for element in ratings:
    if element in content_ratings:
        content_ratings[element] += 1
    else:
        content_ratings[element] = 1
print(content_ratings)

## 3. Creating Our Own Functions ##

def square(number):
    squared = number * number
    return squared

squared_10 = square(number = 10)
squared_16 = square(number = 16)

print(squared_10)
print(squared_16)

## 4. The Structure of a Function ##

def add_10(number):
    added = number + 10
    return added

add_30 = add_10(number = 30)
add_90 = add_10(number = 90)
print(add_30)
print(add_90)

## 5. Parameters and Arguments ##

def date(year, month, day):
    dated = month + " " + str(day) + "," + " " + str(year)
    return dated

firstdate = date(2006, 'July', 15)
seconddate = date(2004, 'February', 4)
thirddate = date(1949, 'June', 9)
print(firstdate)
print(seconddate)
print(thirddate)

## 6. The Return Statement ##

def square(a_number):
    return a_number * a_number
squared_6 = square(6)
squared_11 = square(11)
print(squared_6)
print(squared_11)