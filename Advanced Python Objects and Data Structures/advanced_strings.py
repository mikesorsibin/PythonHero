#Advanced string methods

s ='hello world'
w='hello'

#Built in Regular Expressions
print(s.split('e'))
print(s.partition('e'))


#changing cases
print(s.upper())
print(s.lower())
print(s.capitalize())

#location and counting
print(s.count('o'))# returns the number of occurences without overlap
print(s.find('o'))# returns the starting index position of first occurence


#formatting

print(s.center(20,'z'))


#is check methods

print(s.islower())
print(s.isupper())
print(s.isalnum())
print(s.isalpha())
print(s.isspace())
print(s.istitle())
print(s.endswith('d'))

