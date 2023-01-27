#1
print("1. Write a function that takes in alphanumeric values and take out only the digits in it "
      "use return statement to save the digits to a variable")
a = "abc123def456"
b = ''.join(c for c in a if c.isdigit())
print(b)

#2
print("\n2 Write a function that takes in a alphanumeric values and print only the alphabets in "
      "it use return statement to save the alphabets to a variable")
a = "abc123def456"
b = ''.join(c for c in a if c.isalpha())
print(b)

# 3 a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']
# Using the above list, check if the length of each word is > 2 and
# first character and last character are same
# If the above two conditions are satisfied, then save that word
# to a variable else save the first character of the word to another variable
print("\n3. a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']")
a = ['aba', 'bab', 'India', 'America', 'Hi', 'Hello']
b = []
c = []
for i in a:
    if len(i)>2 and i[0]==i[-1]:
        b.append(i)
    if len(i)>0 and i[0]!=i[-1]:
        c.append(i[0])
print(b)
print(c)


