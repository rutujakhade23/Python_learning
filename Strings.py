word = "python"
# print(len(word))
print(word[3])

#concatenate
word1 = "I love"
word2 = "ML"

sentence = word + " " + word1 + word2
print(sentence)
print(word1 + " " + word2)

for ch in word:
    print(word)

print(word[2:len(word)])
print(word[-4:-2])    #Reverse fasion of printing

#string formating
a = 5
b = 10
sum = a + b
print("sum is {} ".format(sum))
print("Language is {}". format("Python"))
print("sum of {} & {} is {}".format(a,b,sum))

#index based formating
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based
print("values of vars{a} & {b}".format(a=3, b=4))

#f-strings
print(f"sum of {a} & {b} is {a+b}")
print(f"avg of {a} & {b} is {(a+b)/2}")