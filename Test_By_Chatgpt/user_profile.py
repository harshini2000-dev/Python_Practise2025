
def user_profile(name,greet,*hobbies,**extradetails):
    print(f"{greet}, {name}!")
    #print(f"hobbies: {hobbies}") # gives tuple
    
    if hobbies:
        print(f"hobbies:", ", ".join(hobbies))

    for key,value in extradetails.items():
        print(f"{key}: {value}")

user_profile("Ammu", "Welcome", "Gaming","skating", age = 25, marital_status = "Single")