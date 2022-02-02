from time import sleep
from datetime import datetime
from playsound import playsound
from dateutil.parser import parse
if __name__ == "__main__":
    x = input("Enter the number of minutes or time : ")
    if x.count(':') == 1 and datetime.now() <= parse(x):
        sleep(int((parse(x) - datetime.now()).seconds))
        playsound('intro.wav')
    else:
        sleep(int(x)*60)
        playsound('intro.wav')