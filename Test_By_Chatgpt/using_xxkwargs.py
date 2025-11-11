# Write a function print_info(**kwargs) that prints key-value pairs in the following format:
''' output example:
name: Alice
age: 30
'''

def print_info(**person_details):

    for key,value in person_details.items():
        print(f"{key} : {value}")

print_info(name = 'Alice', age = 30)