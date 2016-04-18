from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import queue
import random


class QueueManager(BaseManager):
    pass


task_queue = queue.Queue()
resule_queue = queue.Queue()


def get_task():
    return task_queue


def get_result():
    return resule_queue


if __name__ == '__main__':
    freeze_support()

    manager = QueueManager(('127.0.0.1', 5000), b'abc')
    manager.register('get_task_queue', get_task)
    manager.register('get_resule_queue', get_result)
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_resule_queue()

    for i in range(10):
        n = random.randint(0, 100)
        task.put(n)
        print('put task %d' % n)

    print('trying to get result...')

    for i in range(10):
        r = result.get(True)
        print('get result %d' % r)

    manager.shutdown()
    print('master exit')
