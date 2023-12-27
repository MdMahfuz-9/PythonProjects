password = input("Enter a password:- ")

result = {} # creating a dictionary to store the values


if len(password) > 8 : #check lenth
    result["lenth"] = True
else:
    result["lenth"] = False


digit = False # check for digit

for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit


upper = False

for i in password:
    if i.isupper():
        upper = True

result["upper"] = upper

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")
