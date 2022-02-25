## 1. Returning Multiple Variables ##

def pythagorean(a, b):
    a_squared = a * a
    b_squared = b * b
    c_squared = a_squared + b_squared
    return a_squared, b_squared, c_squared

print(pythagorean(5, 12))

## 2. Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
    
all_data = open_dataset()
header = all_data[1]
apps_data = all_data[0]

## 3. More About Tuples ##

def open_dataset(file_name='AppleStore.csv', header=True):        
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    
    if header:
        return data[1:], data[0]
    else:
        return data
apps_data, header = open_dataset()
print(header)
print("=============")
print(apps_data[:5])