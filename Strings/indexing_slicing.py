word = "programming"  

# print first char
print(word[0]) 
# print last char
print(word[-1])
# print 5th char
print(word[4]) 

#Print the first 4 characters
print(word[0:4])

#Print characters from index 3 to 7 (inclusive of index 3, exclusive of 8)
print(word[3:8])

#Print everything except the first and last character
print(word[1:-1])

#Print every second character
print(word[::2])
#Reverse the string using slicing
print(word[::-1])
#Print characters from index 2 to 9, skipping every 2 characters
print(word[2:10:2])

sentence = "Learning Python is fun!"

#Print just the word "Python"
wrd = sentence[9:15]
print(wrd)
#Print the last 4 characters
wrd = sentence[-4:]
print(wrd)
#Print the string without the first and last word (hint: use slicing, not .split())
wrd = sentence[9:-4]
print(wrd)