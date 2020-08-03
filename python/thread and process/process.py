import os
from multiprocessing import Pool, Process, Queue
import time
import subprocess
import random

"""linux或unix系统中可以使用fork新起一个子进程"""
# p = os.fork()

# if p == 0:
#     print(os.getpid())
#     print(os.getppid())

"""使用Process创建新的进程"""
# def run(name: str):
#     print(f'Run child process {name} {os.getpid()}')

# if __name__ == '__main__':
#     print(f'Parent process {os.getpid()}.')
#     p = Process(target=run, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join() # 用于等待子进程结束再往下执行
#     print('Child process end.')

"""进程池"""
# def long_time_task(name):
#     print(f'run task {name} {os.getpid()}')
#     start = time.time()
#     time.sleep(3)
#     end = time.time()
#     print(f'task {name} runs {end - start} seconds')

# if __name__ == '__main__':
#     print(f'Parent process {os.getpid()}.')
#     process_pool = Pool(5) #Pool默认大小是cpu核数
#     for i in range(5):
#         process_pool.apply_async(long_time_task, args=(i,))
#     print('waiting for all processes end')
#     process_pool.close() # 确保不会再有新的子进程加入
#     process_pool.join()
#     print('all processes done')

"""subprocess启动子进程"""
# subprocess.call(['df', '-h'])

"""进程间通信，一般使用queue或者pipe进行数据交换"""
def write(q: Queue):
    print(f'start write process {os.getpid()}')
    for n in ['a', 'b', 'c']:
        print(f'put {n} to queue')
        q.put(n)
        time.sleep(random.random())

def read(q: Queue):
    print(f'start read process {os.getpid()}')
    while True:
        value = q.get(True)
        print(f'get {value} from queue')


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()