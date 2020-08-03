"""
列表元素可以按照某种算法推算出来，那我们可以在循环的过程中不断推算出后续的元素，这种机制称为生成器。
generator保存的实际上是一个算法，generator也是可迭代的
"""
# 直接定义一个生成器
# g1 = (x for x in range(10))
# print(g1)
# for x in g1:
    # print(x)

# 生成器函数
# 一个函数中有yield的话，这个函数就是一个生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'

for x in fib(5):
    print(x)
