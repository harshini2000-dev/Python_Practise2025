msg = "python is fun"

# upper, lower
print(msg.upper())
print(msg.lower())

# capitalize()
''' Makes only the first character uppercase
Converts the rest to lowercase'''
statement = "pYTHON IS aweSome"
print(statement.capitalize())

#title()
''' Capitalizes the first letter of each word in the string
Turns all other letters lowercase'''
headline = "wELCOME to THE jungle"
print(headline.title())

# replace(old, new)
'''Replaces all occurrences of the substring old with the substring new
Returns a new string (original stays unchanged)'''
text = "I like cats. Cats are cute!"
text1 = text.lower().replace("cats","dogs")
print(text1)

#.find(substring)
'''Returns the index of the first occurrence of substring inside the string
Returns -1 if the substring is not found'''
phrase = "Finding Nemo is a fun movie"
print(phrase.find('Nemo'))
print(phrase.find('Dory'))

# strip()
'''Removes leading and trailing whitespace (spaces, tabs, newlines) from a string
Returns a new string without those extra spaces'''
data = "    lots of spaces around    "
print(data.strip())

#.startswith() and .endswith()
'''
.startswith(substring) — returns True if the string starts with the given substring
.endswith(substring) — returns True if the string ends with the given substring'''

test_str = "hello world"
print(test_str.startswith('hello'))
print(test_str.startswith('Hello'))
print(test_str.endswith('world'))

#count()
'''Counts how many times a substring appears in the string
Returns an integer count'''

sentence = "The quick brown fox jumps over the lazy dog"
print(sentence.count('o'))
print(sentence.lower().count('the'))

# split():
'''Splits a string into a list of substrings, using a separator (default is whitespace)'''

line = "apple,banana,grape,orange"
fruits = line.split(",")
print(fruits)
line1 = "; ".join(fruits)
print(line1)



test1 = "HelloWorld"
test2 = "123456"
test3 = "Python3"
print(test3.isalnum())
print(test1.isalpha())
print(test2.isdigit())
