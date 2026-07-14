# # while loop
count = 1

while (count <= 5):
    print("HW", count)
    count += 1

print("after loop, count = ", count)

i = 1
while (i <= 5):
    print(i)
    i += 1
    
i = 5
while (i >= 1):
    print(i)
    i -= 1

i=0
while(i<5):
    print(i)
    i += 1

# multiplication table of any no
n = int(input("enter num: "))
i = 1
while (i <= 10):
    print(n * i)
    i += 1


# # break statement
i = 1
while(i <= 10):
    if(i % 6 == 0):
        break
    print(i)
    i += 1
print("out of loop now")

# # continue
i = 1
while(i <= 10):
    if(i % 3 == 0):
        i += 1
        continue
    print(i)
    i += 1
print("outof loop")

i=0
while(i <= 10):
    i+=1
    if(i % 2 ==0):
        continue
    print(i)
    
#for loop 
string = "abcd"
for var in string:
    print(var)

for i in range(5):
    print(i+1)


#count the number of i's  => 5
word = "Artificial intelligence"
ans = 0
for ch in word:
    if(ch == 'i'):
        count += 1

print("count of i =", ans)

# vowel count of string
word = "artificial"
count = 0
for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count += 1
print("ans =" , count)

#range function 
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(2,10,2):
    print(i)

#print sum of first n natural no's
n = int(input("enter number: "))
sum = 0
for i in range(1,n+1):
    sum += i

print("sum =", sum)