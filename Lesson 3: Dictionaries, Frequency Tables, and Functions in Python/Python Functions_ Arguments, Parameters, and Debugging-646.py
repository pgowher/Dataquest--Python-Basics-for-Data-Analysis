## 1. Extract Values from Any Column ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def extract(column):
    frequency_list = []
    for element in apps_data[1:]:
        value = element[column]
        frequency_list.append(value)
    return frequency_list

genres = extract(11)

## 2. Creating Frequency Tables ##

# CODE FROM THE PREVIOUS SCREEN
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []    
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)    
    return column

def freq_table(i_list):
    our_dict = {}
    for element in i_list:
        if element in our_dict:
            our_dict[element] += 1
        else:
            our_dict[element] = 1
    return our_dict

generes = extract(11)
genres_ft = freq_table(generes)

print(genres_ft)

## 3. Writing a Single Function ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def freq_table(index):
    freq_table = {}
    for element in apps_data[1:]:
        value = element[index]
        if value in freq_table:
            freq_table[value] += 1
        else:
            freq_table[value] = 1
    return freq_table

ratings_ft = freq_table(7)
print(ratings_ft)
        

## 4. Reusability and Multiple Parameters ##

# INITIAL FUNCTION
def freq_table(data_set, index):
    opened_file = open(data_set)
    from csv import reader
    read_file = reader(opened_file)
    read_data = list(read_file)
    
    frequency_table = {}
    
    for element in read_data[1:]:
        value = element[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table

ratings_ft = freq_table('AppleStore.csv', 7)
print(ratings_ft)

## 5. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
    
    
def freq_table(data_set, index):
    
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table

content_ratings_ft = freq_table(apps_data, 10)
ratings_ft = freq_table(data_set = apps_data, index = 7)
genres_ft = freq_table(index = 11, data_set = apps_data)
print(content_ratings_ft)
print(ratings_ft)
print(genres_ft)

## 6. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    i_list = extract(data_set, index)
    mean_value = find_sum(i_list) / find_length(i_list)
    return mean_value

avg_price = mean(apps_data, 4)
print(avg_price)
    
     
        

## 7. Debugging Functions ##

def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)

print(avg_price)
print(avg_rating)