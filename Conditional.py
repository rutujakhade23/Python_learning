#if and else if 
age = 15
if age >= 18:
    print("You can drive")
else:
    print("not drive")

#elif
color = input("enter color:")
if color == "red":
    print("stop")
elif color == "green":
    print("Go")
elif color == "yellow":
    print("look")
else:
    print("wrong color")

# Practice of conditional
age = int(input("enter the age:"))

if (age < 13):
    print("child")
elif (age >= 13 and age < 18) :
    print("Teenager")
elif (age >= 18) :
    print("adult")

if (age < 13):
    print("child")
elif (age >= 13 and age < 18):
    print("teenager")
else:
    print("adult")

username = input("enter username:")
password = input("enter password:")
if(username == "admin" and password == "pass"):
    print("LOGIN Successful!")
elif (username != "admin"):
    print("Wrong Username")
else:
    print("Wrong password")

n = int(input("enter num:"))
if (n % 5 == 0):
    print("multiple of 5")
else:
    print("not multiple of 5")

# odd or even
n = int(input("enter num:"))
if (n % 2 == 0):
    print("no is even")
else:
    print("Odd")

# nesting
username = input("enter username:")
password = input("enter password:")

if(username == "admin"and password == "pass"):
    print("success")
else :
    if(username != "admin"):
        print("wrong username")
    else:
        print("wrong password")

color = input("enter color:")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("wrong color")