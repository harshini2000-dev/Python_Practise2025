# Create a dictionary named car with these key-value pairs:

car = {
    "brand" : "Toyota",
    "model" : "Camry",
    "year" : 2025
}

print(car["brand"], car["year"]) # access value with keys

#Add a new key "color" with value "Black" to your car dictionary
car["color"] = "Black"
#Update the "model" value to "Corolla"
car["model"] = "Corolla"
#Print the full dictionary after the changes
print(car)

# If you try to access a key that doesn’t exist like this
'''print(car["owner"]) ''' # ❌ This will raise a KeyError
# SO use get(),
print(car.get("owner"))      # ➝ None (no error)
print(car.get("owner", "Not available"))  # ➝ N/A (custom default)
print(car.get("brand")) 

# Remove the "color" key using del
del car["color"]
# Remove the "year" key using .pop()
car.pop("year")
# Print the dictionary after changes
print(car)


## Loop thru dicts

'''
You can loop through:

Keys: for key in dict:

Values: for value in dict.values():

Items (key-value pairs): for key, value in dict.items(): '''

for key,value in car.items():
    print(key, ":", value)

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

# Add a new student "David" with a score of 88.
students["David"] = 88
# Update "Charlie"’s score to 83.
students["Charlie"] = 83
# Remove "Alice" from the dictionary.
students.pop("Alice")
# Use a loop to print each student's name and score in this format:
"Bob scored 92"

for key,value in students.items():
    print(f"{key} scored {value}")