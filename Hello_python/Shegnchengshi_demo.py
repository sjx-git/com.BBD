'''生成器的演练
1.斐波那契数列
2.打印出生成式的结果，可以用next或者__next__但是这两种会在最后无数据可取得时候报错，最好用for循环
3.yield 暂停运行 下次再从当前位置继续运行
4.可用send在yield处 传递参数'''
def fbnq():
    a,b = 0,1
    for i in range(5):
        a,b = b,a+b
        #只要包含了 yield 这个函数就不再是函数了  所以直接调用fbnq()是不会执行，因为只要到这个地方就
        #是停止于运行，直到下次用next或者.__next__会从当前位置仅需运行
        temp = yield b
        if temp != None:
            print(temp)
t = fbnq()
print(t.__next__())#先调用一次 不然会报错
t.send('hi')

for i in fbnq():
    print(i)