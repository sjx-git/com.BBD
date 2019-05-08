
'''
c = int(input("请输入第一个个数字："))
a = int(input("请输入第二个数字："))
b = int(input("请输入第三个数字："))
def sum1(a,b,c):
    d = a + b + c
    return d

re = sum1(a,b,c)
print((re))

'''
def ss():
    f = open("test.txt","w+")
    f.write("Hello first txt  ")
    f.close()
    a = open("test.txt","r+")
    print(a.read())
    open()
    #print(a.read(1))

if __name__ == '__main__':
    ss()


