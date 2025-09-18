# i = int(input("Enter the number: "))
# while i <= 38:
#     i = int(input("Enter the number: "))
#     print(i)
#     # i = i + 1
# print("Done with the loop")

# count = 5
# while (count > 0):
#     print(count)
#     count = count - 1

# count = 5
# while count > 0:
#     print(count)
#     count = count - 1
# else:
#     print("I am inside else")

# -----------------------------------------------
# Python does not have a built-in do...while loop.
# We can simulate it using while True + break.
# The behavior:
#   - Loop body executes at least once
#   - Then condition is checked to possibly exit
# -----------------------------------------------

# Simulating do { ... } while(condition)
while True:
    # Loop body: get input from the user
    num = int(input("Enter a number: "))
    print("You entered:", num)

    # Condition check (like while-condition in do..while)
    if num < 0:  # Stop the loop if negative number is entered
        break