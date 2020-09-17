import datetime

ct = datetime.datetime.now()

def currentTime():
    return str(f"{ct.year}. {ct.month}. {ct.day}. {ct.hour} : {ct.minute} : {ct.second}")
while True:
    print(currentTime())