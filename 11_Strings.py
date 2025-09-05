name = "Harry"
friend = "Rohan"
anotherFriend = "Lovish"
apple = 'He said, "I want to eat an apple'
apple1 = 'He said, "I want to eat an apple'
apple2 = """He said,
Hi Divyanshu
Hey, I'm Good
I want to eat an apple"""

print("Hello, " + name, "\n")
print(apple, "\n")
print(apple1, "\n")
print(apple2, "\n")

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4], "\n")
# print(name[5]) # Throws an error

print("Let's use a for loop\n")
for character in apple2:
    print(character)