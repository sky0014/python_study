from multiprocessing import Process, Queue
from multiprocessing.pool import Pool
import os
import time
import random


def run_proc(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s complete in %.2f s (%s)' % (name, end - start, os.getpid()))


def write(q):
    for c in ['A', 'B', 'C']:
        print('write %s pid=%s' % (c, os.getpid()))
        q.put(c)
        time.sleep(random.random() * 3)


def read(q):
    while True:
        c = q.get(True)
        print('read %s pid=%s' % (c, os.getpid()))


if __name__ == '__main__':
    print('\ntest multi process pool\n')
    pool = Pool(4)
    for i in range(4):
        pool.apply_async(run_proc, ('child' + str(i),))
    pool.close()
    pool.join()
    print('all done!')

    print('\ntest multi process communication\n')
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print('end')
