"""返回函数，就是高阶函数可以把函数作为return值返回。与闭包的关系是：闭包需要以返回函数的形式实现。"""
"""返回函数"""
def lazy_sum(*args):
    def sum():
        count = 0
        for n in args:
            print("n", n)
            count = count + n
        return count
    return sum
nums = [x for x in range(5)]
f = lazy_sum(*nums)
print(f) # f是求和函数
print(f()) # 调用f才能返回结果

"""闭包"""