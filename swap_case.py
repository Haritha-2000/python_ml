# str1 = "Pythonist 2"
# k  = ""
# for i in str1:
#     if i.islower():
#         k += i.upper()
#     else:
#         k += i.lower()
# print(k)

def swapi(x):
    k = ""
    for i in x:
        if i.islower():
            k += i.upper()
        else:
            k += i.lower()
    return(k)
name = input("Enter a name:" )
name1 = swapi(name)
print(name1)