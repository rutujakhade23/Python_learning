info = [
    ("Alice", "Math"),
    ("Bob","Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice","English"),
    ("Charlie","English")
]

unique_courses = set() 
for tup in info:
    unique_courses.add(tup[1]) #course

print(unique_courses)

courses_set = set()
for name, course in info:
    print(name, course)

for name,course in info:
    if(course == "English"):
        print(name)

dict = {}

for name,course in info: 
    if(dict.get(name) == None):
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
print(dict)
