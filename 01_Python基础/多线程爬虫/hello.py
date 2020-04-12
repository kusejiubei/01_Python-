import threading
import time


def sorry():
    time.sleep(1)
    print("i am sorry")


if __name__ == '__main__':
    cur = time.time()
    for i in range(5):
        sorry()
    cur2 = time.time()
    print("耗时1： %s " % (cur2 - cur))
    for i in range(5):
        t = threading.Thread(target=sorry)
        t.start()
    cur3 = time.time()
    print("耗时2： %s " % (cur3 - cur2))
    for i in range(5):
        t = threading.Thread(target=sorry)
        t.start()
    cur4 = time.time()
    print("耗时3： %s " % (cur4 - cur3))
