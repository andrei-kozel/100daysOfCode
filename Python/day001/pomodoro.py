from datetime import datetime, timedelta
import time


minutes = int(input('Enter minutes: '))
time_now = datetime.now()
time_in_x_minutes = time_now + timedelta(minutes=minutes)

print(f'I will alarm you in {minutes}, stay focused!')

while time_in_x_minutes > datetime.now():
    print(datetime.now())
    print(time_in_x_minutes)
    time.sleep(10)


print('Woooohoooo!!!')
