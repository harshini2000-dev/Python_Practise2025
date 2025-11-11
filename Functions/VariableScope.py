name = "Harshini"

def call_me():
    name = "Ammu"
    print(name)

print("before call ",name)
call_me()
print("after call ", name)

##################

num = 10
def inc():
    num = 10000
    return num

print(num) # before calling
changed = inc()
print(changed) # store the returned value and use it instead because num is still 10
print(num) # global variable remains same