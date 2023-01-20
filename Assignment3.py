# Assignment - String Data Type

#1
print("1. Create a string")
myString = "this is a new string"
print(myString)

#2
print("\n2. How would you convert each word in a string to a capital letter?")
upStr = myString.upper()
print(upStr)

#3
print("\n3. Count the total number of characters in a string")
res = len([c for c in myString if c.isalpha()])
print(res)

#4
print("\n4. Count the number of a specific character in a string")
res1 = myString.count('i')
print(res1)

#5
print("\n5. Capitalize the first character of a string")
myString = "this is a new string"
res2 = myString.capitalize()
print(res2)
print(myString.title())

#6
print("\n6. Split a string on a specific character")
word = "hello everyone how are you"
res3 = word.split()#This by default consider space
print(res3)

#7
print("\n7. Check if a string is composed of all lower case characters")
str1 = 'Welcome'
str2 = 'welcome'
print(str1.islower())
print(str2.islower())

#8
print("\n8. Check if the first character in a string is lowercase")
str1 = 'welcome'
res4 = str1[0].islower()
print(res4)

#9
print("\n9. Can an integer be added to a string in Python?")#No
test_str = "Geeks"
test_int = 4
res5 = test_str + str(test_int) + test_str
print("The string after adding number is : " + res5)

#10
print("\n10. Join strings into a single string, delimited by hyphens")
# Input = 'abc'
# Output = a-b-c
inp = 'hello'
res7 = '-'.join(inp)
print(res7)
print('OR')
asd = 'hello'
s = '-'
res10 = s.join(asd)
print(res10)

#11
print("\n11. Uppercase or lowercase an entire string. Sentence = 'The Cat in the Hat'")
sen = "The Cat in the Hat"
print(sen.lower())
print(sen.upper())

#12
print("\n12. Uppercase the first and last character of a string")
s = "welcome to geeksforgeeks"
print("String before:", s)
a = s.split()
res = []
for i in a:
    x = i[0].upper()+i[1:-1]+i[-1].upper()
    res.append(x)
res = " ".join(res)
print("String after:", res)

#13
print("\n13. Check if a string is all uppercase")
s = "Welcome"
print(s.isupper())

#14
print("\n14. Convert an integer to a string")
num = 20
print(type(num))
conv = str(num)
print(type(conv))

#15
print("\n15. Check if a string contains only characters of the alphabet")
sen = "Hello"
sen1 = "He7lo"
if sen.isalpha():
    print("Contains only characters")
else:
    print("Contains number")

#16
print("\n16. Replace all instances of a substring in a string. sentence = 'Sally sells sea shells by the sea shore'")
# Replace all  'sea' with  'Mountain'
# End result --->  'Sally sells Mountain shells by the Mountain shore'
sen = 'Sally sells sea shells by the sea shore'
res11 = sen.replace('sea','mountain')
print(res11)

#17
print("\n17. Remove whitespace from the left, right or both sides of a string. string = '  string of whitespace   '")
# Explore lstrip(), rstrip(), strip() methods and solve the question
string = '  string of whitespace   '
#remove spaces from left
print (string.lstrip())
#remove spaces from right
print (string.rstrip())
#remove spaces from both side
print (string.strip())

#18
print("\n18. Check if a string begins with or ends with a specific character?")
# Python code to implement startswith()
# and endswith() function.
# Explore endswith(), startswith() methods, and solve the question
string = "GeeksforGeeks"
# startswith()
print(string.startswith("Geeks"))
print(string.startswith("Geeks", 4, 10))
print(string.startswith("Geeks", 8, 14))
print()
# endswith
print(string.endswith("Geeks"))
print(string.endswith("Geeks", 2, 8))
print(string.endswith("for", 5, 8))

#19
print("\n19. What is the effect of multiplying a string by 3?")
sen = "Hello"
print(sen * 3)


# 20. Does defining a string twice (associated with 2 different variable names) create one or two objects in memory?

#21
print("\n21. Write a Python program that accepts the user's first and last name and prints them in reverse order "
      "with a space between them")
# Sample Input :
# first_name = 'Learn'
# last_name = 'Python'
# Sample Output :
# result = Python Learn
first_name = 'Learn'
last_name = 'Python'
print(last_name+" "+first_name)


#22
print("\n22. Find the frequency of occurrence")
a = 'have a nice day'
symbol = 'abcdefghijklmnopqrstuvwxyz'
for key in symbol:
    if a.count(key)>0:
        print(key,'-',a.count(key), end="   ")