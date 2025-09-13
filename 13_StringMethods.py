# Strings are immutable
a = "!!!!!!Divyanshu!! !! !! Divyanshu"
print(len(a))
print(a)
print(a.lower())
print(a.upper())
print(a.rstrip("!"))
print(a.replace("Divyanshu", "Vashishth"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))
print(a.count("Divyanshu"))

str2 = "Welcome to the Console !!!"
print(str2.endswith("!!!"))

str3 = "Welcome to the Console !!!"
print(str3.endswith("to", 4, 10))

str4 = "He's name is DV. He is an Honest man."
print(str4.find("is"))
print(str4.find("ishh"))
# print(str1.index("ishh"))

str5 = "WelcomeToTheConsole"
print(str5.isalnum())

str6 = "Welcome"
print(str6.isalpha())

str7 = "hello world"
print(str7.islower())

str8 = "We wish you a Merry Christmas"  # \n
print(str8.isprintable())

str9 = "        "  # Using Spacebar
print(str9.isspace())

str10 = "        "  # Using Tab
print(str10.isspace())

str11 = "World Health Organization"
print(str11.istitle())

str12 = "To Kill a Mocking Bird"
print(str12.istitle())

str13 = "Python is a Interpreted Language"
print(str13.startswith("Python"))

str14 = "Hello DV"
print(str14.swapcase())

str15 = "His name is DV. DV is an honest man."
print(str15.title())