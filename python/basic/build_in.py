from collections import ChainMap, Counter, namedtuple
import time
import argparse
import os
import itertools

"""nametupled"""
"""表示坐标"""
# Point = namedtuple('Point', 'x y')
# p = Point(1, 2)
# print(p.x, p.y)

"""ChainMap，把多个映射组合在一起"""
"""解析命令行，优先级按照命令行参数、环境变量和默认参数的顺序"""
# default = {
#     'user': 'guest',
#     'color': 'red'
# }

# parse = argparse.ArgumentParser(description='python cmdline test')
# parse.add_argument('-u', '--user')
# parse.add_argument('-c', '--color')
# namespace = parse.parse_args()
# cmdline_args = {k: v for k, v in vars(namespace).items() if v}

# chain_map = ChainMap(cmdline_args, os.environ, default)

# print(f"user={chain_map['user']}")
# print(f"color={chain_map['color']}")

"""Counter， 计数器"""
# counter = Counter()
# for i in 'programing':
#     counter[i] = counter[i] + 1
# print(counter)

"""itertools"""
# count按照传入的数字进行无限迭代
# for i in itertools.count(2):
#     print(i)

# cycle把传入的序列无限循环重复
# for i in itertools.cycle('123'):
    # print(i)

# repeat按照指定次数重复下去，无参数就无限重复
# for i in itertools.repeat('a', 5):
    # print(i)

# 使用takewhile限制无限迭代:
# ns = itertools.takewhile(lambda x: x <= 10, itertools.count(1))
# print(list(ns))

# 使用chain把多个迭代对象串联起来
# for i in itertools.chain('abc', 'xyz'):
    # print(i)

# 使用groupby按照相同元素分组
for k, v in itertools.groupby('aaabbbdfsfvvvxxx'):
    print(k, list(v))