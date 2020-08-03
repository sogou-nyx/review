import time
import functools
"""装饰器本质上是一个返回函数的高阶函数。用于在不修改原有目标函数的基础上，动态的给该函数增加功能"""
"""下面是定义了一个log装饰器，让now方法输出时间前先打印一行日志"""
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print(f'call {func.__name__}')
        return func(*args, **kw)
    return wrapper
"""定义一个更复杂的装饰器，自定义日志文本"""
def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(f'call {text}, {func.__name__}')
            return func(*args, **kw)
        return wrapper
    return decorator

@log1('excute')
def now():
    print(time.time())
    
# log是一个装饰器，写在now()之前相当于执行了now = log(now)，我们调用的now不再指向定义的now()函数，而是指向log中定义的wrapper函数，此时now的name是wrapper，可以通过functools.wraps使得now的name不变
# now()

"""实现一个装饰器，统计函数执行时间"""
def excute_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start_time = time.time()
        print(f'{func.__name__} start time: {start_time}' )
        temp = func(*args, **kw)
        finish_time = time.time()
        print(f'{func.__name__} finish time: {finish_time}' )
        print(f'{func.__name__} cost: {finish_time - start_time}' )
        return temp
    return wrapper

@excute_time
def cal():
    sum = 0
    for i in range(10000):
        sum += i
    return sum

# print(cal())
