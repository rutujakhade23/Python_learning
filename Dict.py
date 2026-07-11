info = {
    "name":"Rutuja",
    "cgpa":8.3,
    "subjects": ["ANN","CS", "DS","CC"],
    3.14: "PI"
}
print(info)
print(type(info))
print(info.keys())

dict_keys = list(info.keys())
print(dict_keys)

dict_vals = list(info.values())
print(dict_keys)

print(info.items())

print(info.get("cgpa"))

info.update({
    "city":"Delhi"
})

print(info)