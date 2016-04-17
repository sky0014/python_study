import threading

local = threading.local()


def run_thread(name):
    local.name = name
    process_name()


def process_name():
    name = local.name
    print('Thread : %s name : %s' % (threading.current_thread().name, name))


if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread, name='T1', args=('Sara',))
    t2 = threading.Thread(target=run_thread, name='T2', args=('Tara',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
