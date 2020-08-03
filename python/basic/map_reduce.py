from functools import reduce

"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
"""
def f(x):
    return x * x

res = map(f, [x for x in range(10)])
# print(list(res))
# for data in res:
    # print(data)

"""reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算"""
def g(x, y):
    return x + y

res = reduce(g, [x for x in range(4)])
# print(res)


"""map和reduce结合使用，把字符串数字转为int"""
def cal(x, y):
    return x * 10 + y

def char2int(x):
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return d[x]

res = reduce(cal, map(char2int, '13579'))
# print(res, type(res))

"""列表中各个名字首字母大写"""
origin_list = ['adam', 'LISA', 'barT']
def convert(name: str):
    # return name.capitalize()
    return name[0].upper()+name[1:].lower()

res = map(convert, origin_list)
# print(list(res))

"""列表中数据求积"""
nums = [3, 5, 7, 9]
def prod(x, y):
    return x*y

res = reduce(prod, nums)
# print(res)

"""str '123.456' convert to float 123.456"""
s = '123.456'
def str2float(s):
    str2int = reduce(cal, map(char2int, [num for num in s if num != '.']))
    split_s = s.split('.')
    low_num = split_s[1]
    return str2int / 10 ** len(low_num)

res = str2float(s)
# print(res)

"""filter:接收一个函数和一个序列,然后根据返回值是True还是False决定保留还是。丢弃该元素"""
"""使用filter生成一个素数队列"""
# 除2以外的偶数肯定不是素数，所以先构造一个奇数队列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def filter_func(num):
    return lambda x: x % num > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(filter_func(n), it)

for n in primes():
    if n > 100:
        break
    # print(n)

"""filter筛选回数:101,11011类似的"""
def is_palindrome(n):
    s = str(n)
    return s[::1] == s[::-1]

res = filter(is_palindrome, [x for x in range(1000)])
# print(list(res))
