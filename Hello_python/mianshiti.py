'''给定一个int类型的数字123，要求编写一个函数，返回1+2+3'''
def demo_01(A):
    tem = 0
    while A != 0:
        tem += A % 10
        A = A // 10
    return tem
print(demo_01(123))

''' 给定2个int类型的参数x和y，要求编写一个函数，用加法和减法实现x*y '''
pass

'''  交换两个数据的值  第一种 借用第三个参数'''
a = 1
b = 2
c = a
a = b
b = c
print('a的值是：%d，b的值是：%d'%(a,b))

'''  交换两个数据的值  第二种 不借用第三个参数'''
a = 1
b = 2
a = a+b
b = a-b
a = a-b
print('a的值是：%d，b的值是：%d'%(a,b))

'''  交换两个数据的值  第二种 不借用第三个参数'''
a = 1
b = 2
a,b = b,a
print('a的值是：%d，b的值是：%d'%(a,b))
