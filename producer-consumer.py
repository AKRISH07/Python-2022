from threading import Lock, Thread, Condition
import time
import random

queue = []
#lock = Lock()
condition = Condition()
MAX_NUM = 10

class ProducerThread(Thread):
    def run(self):
        value = range(50)
        global queue
        while True:
            condition.acquire()
            if len(queue) == MAX_NUM:
                print("Queue is full")
                condition.wait()
                print("Space in Queue")
            count = random.choice(value)
            queue.append(count)
            print("Producer:", count)
            condition.notify()
            condition.release()
            time.sleep(random.random())
        
class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing")
                condition.wait()
                print("Producer added something")
            num = queue.pop(0)
            print("Consumer:", num)
            condition.notify()
            condition.release()
            time.sleep(random.random())


ProducerThread().start()
ConsumerThread().start()