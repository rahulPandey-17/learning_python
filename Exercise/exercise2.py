import time

current_time = int(time.strftime("%H"))

if current_time < 12 :
    print("Good Morning")
elif current_time <=17 :
    print("Good Afternoon")
elif current_time <= 19 :
    print("Good Evening")
else :
    print("Good Night")