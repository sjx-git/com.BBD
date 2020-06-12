'''给定一个int类型的数字123，要求编写一个函数，返回1+2+3'''
def demo_01(A):
    tem = 0
    while A != 0:
        tem += A % 10
        A = A // 10
    return tem
print(demo_01(123))

''' 给定2个int类型的参数x和y，要求编写一个函数，用加法和减法实现x*y '''

