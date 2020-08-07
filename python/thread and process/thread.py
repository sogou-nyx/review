import threading
import time

# def run():
#     print('当前线程的名字是： ', threading.current_thread().name)
#     time.sleep(2)
#     print('当前线程结束： ', threading.current_thread().name)


# if __name__ == '__main__':

#     start_time = time.time()

#     print('这是主线程：', threading.current_thread().name)
#     thread_list = []
#     for i in range(5):
#         t = threading.Thread(target=run)
#         thread_list.append(t)

#     for t in thread_list:
#         t.setDaemon(True)
#         t.start()

#     for t in thread_list:
#         t.join()

#     print('主线程结束！' , threading.current_thread().name)
#     print('一共用时：', time.time()-start_time)

# local_school = threading.local()

# def process_student():
#     std = local_school.student
#     print(f'Hello {std} in {threading.current_thread().name}')

# def process_thread(name):
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread, args=('bob',), name='Thread_bob')
# t2 = threading.Thread(target=process_thread, args=('tom',), name='Thread_tom')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

"""Event模拟红绿灯，每隔五秒换颜色"""
"""一个车线程和一个信号灯线程，使用Event标记信号灯颜色，信号灯线程中操作Event，车线程根据Event状态判断是否可以通行"""
event = threading.Event()

def lights():
    count = 0
    # 初始设置标记位，为绿灯
    event.set()
    while True:
        if count <= 5:
            print(f'light is green')
        elif 5 < count <= 10:
            event.clear()
            print(f'light is red')
        else:
            event.set()
            count = 0
        
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print(f'{name} running')
            time.sleep(1)
        else:
            print(f'{name} meets red light, wait')
            event.wait()
            print(f'light turns to green, {name} start running')

t1 = threading.Thread(target=lights)
t2 = threading.Thread(target=car, args=('BMW',))
t1.start()
t2.start()