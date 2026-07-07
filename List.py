#list : lists are mutable

# L1 = ["Rutuja", 0.1, 100, True]
# L1 = list()
# print(type(L1))

# print(L1[-2])
# L1.append("Kolkata")
# L1.append("India")
# L1.insert(2, "Sare")
# print(L1)
# L1.remove(0.1)
# print(L1)
# L1[0] = "Khade"
# print(L1)
# char_list = ["Rutuja", "Python", "Data"]
# num_list = [8,4,9,1,4]
# print("Before sorting " , num_list)
# num_list.sort()
# print("After sorting " , num_list)
# num_list.reverse()
# print(num_list)

# L1 = ["Rutuja", 100, 0.2, True]
# num_list = [8,2,4,5]
# L1.extend(num_list)
# print(L1)
# print(L1[5:-1])
# L1.clear()
# print(L1)

marks = [99, 100,90,29]
print(marks)
print(len(marks))
marks[2] = 70
print(marks)

marks1 = [100, 80, 90, 69, 92, "abc", 100.99]
print(marks[0:5])
print(marks1[5:])

marks1.append(64)
print(marks1)

marks1.insert(2, 10)
print(marks1)

marks.sort()
print(marks)

marks.sort(reverse=True)
print(marks)

marks1.reverse()
print(marks1)

nums = [1,2,3,4,5,9,10, 7,8,1]
for val in nums:
    print(val)

x = 10
idx = 0
for val in nums:
    if (val == x):
        print(f"{x} found at idx={idx}")
        break
    idx += 1

