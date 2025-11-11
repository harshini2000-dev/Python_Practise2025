def full_name(firstn, lastn):
    return f"Full name is {firstn} {lastn}"

name1 = full_name(firstn= "Sai", lastn="Harshini")
name2 = full_name(lastn="Druthi", firstn="DR..") # order doesn't matter for keyw args
name3 = full_name("P S", lastn="Rao")  # PS is positional arg, Rao is Keyw arg
# name4 = full_name(lastn = "Meghan", "ms.") # Error: Positional argument cannot appear after keyword arguments

print(name1)
print(name2)
print(name3)