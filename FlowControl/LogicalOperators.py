''' and or not '''

fresher = True
good_name = False
manager_approval = False
high_salary = False

if not fresher: 
    # we don't want freshers or students
    print("Can apply for senior posts")
elif  manager_approval and good_name : 
    # you are a fresher but you have good name AND manager permission you can apply
    print("Can apply for post")
elif high_salary or good_name: 
    # you dont have manager approval but earn high OR have good name 
    print("Can apply in other teams")
else:
    print("Not eligible to apply anywhere")


###############

student = False # false = working || true = studying
high_salary = False
good_name = True
if (high_salary or good_name) and not student:
    print("Ok")
else:
    print("Not ok")




