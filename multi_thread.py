import threading
import multiprocessing

balance = 0
lock = threading.Lock()


def change(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()


def loop():
    x = 0;
    while True:
        x = x ^ 1


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)

    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        t.start()
        # p = multiprocessing.Process(target=loop)
        # p.start()
