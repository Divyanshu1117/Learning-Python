import time

hour = time.localtime().tm_hour

if hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")