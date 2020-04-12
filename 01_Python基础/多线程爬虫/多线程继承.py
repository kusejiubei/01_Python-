import threading
import time


class MyThread(threading.Thread):
    def run(self):
        print("i am %s" % self.name)
        time.sleep(1)


if __name__ == '__main__':
    l = time.time()
    for i in range(5):
        my = MyThread()
        my.start()
    print("耗时： %d" % (time.time() - l))
