import time
from datetime import datetime


def countdown(func):
    def inner(*args, **kwargs):
        time.sleep(1)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        func(*args, **kwargs)
    return inner()


@countdown
def what_time():
    t = datetime.today().time()
    print(t.strftime('%H:%M'))


