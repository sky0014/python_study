from multiprocessing.managers import BaseManager
import time
import random


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    manager = QueueManager(('127.0.0.1', 5000), b'abc')
    manager.register('get_task_queue')
    manager.register('get_resule_queue')
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_resule_queue()

    for i in range(10):
        try:
            n = task.get(True)
            print('get task %d' % n)
            result.put(n * n)
            time.sleep(random.randint(0, 5))
        except BaseException as e:
            print('master exit')
            break

    print('worker exit')
