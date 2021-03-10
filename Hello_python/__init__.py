'''
一个包下，必须有此方法 在别的地方才可以引用，即便此方法是空的
'''

'''  这个方法有可用  不过好像还有个set函数可以直接找出相同的部分，待研究'''
class key_demo:
    ''' 用来找出重构后，新的json中不正确的key和value值'''
    old_json = [{'a':2,'b':3},{'e':4,'f':5,'q':{'w':7,'r':8}}]
    new_json = [{'a':2, 'b':3},{'e':4,'F':5,'Q':{'w':7,'r':8}}]
    o3 = []
    o2 = []
    L = []

    def xx(self):
        for temp in self.old_json:
            for o,p in temp.items():
                self.o3.append(o)
        else:
            return self.o3

    def new_jsons(self):
        for temp1 in self.new_json:
            for o1,p1 in temp1.items():
                self.o2.append(o1)
        else:
            return self.o2

    def if_demos(self):
        for A in self.new_jsons():
            if A not in self.xx():
                self.L.append(A)
        else:
            print('不正确的key为：%s'%self.L)


if __name__ == '__main__':

    #key_demo.if_demos('self')   在使用类名.方法名('self')时，会导致程序无法运行,是因为我在调用类属性时，用的是self而没有用类名调用才出现的问题
   ''' f = key_demo()
    f.if_demos()#调用的时候 需要先创建对象即f 再去调用方法；'''


'''上面的程序是个错误使用调用类属性的demo，下面才是正确的写法 唯一的区别就在于类属性的调用'''
class key_demo:
    ''' 用来找出重构后，新的json中不正确的key和value值'''
    old_json = [{'a':2,'b':3},{'e':4,'f':5,'q':{'w':7,'r':8}}]
    new_json = [{'a':2, 'b':3},{'e':4,'F':5,'Q':{'w':7,'r':8}}]
    o3 = []
    o2 = []
    L = []
    def xx(self):
        for temp in key_demo.old_json:#类属性 需要用类名去调用
            for o,p in temp.items():
                key_demo.o3.append(o)
        else:
            return key_demo.o3
    def new_jsons(self):
        for temp1 in key_demo.new_json:
            for o1,p1 in temp1.items():
                key_demo.o2.append(o1)
        else:
            return key_demo.o2
    def if_demos(self):
        for A in key_demo.new_jsons('self'):
            if A not in key_demo.xx('self'):
                key_demo.L.append(A)
        else:
            print('不正确的key为：%s'%key_demo.L)
if __name__ == '__main__':
    '''这两种调用方法都可以 不过还是建议选择先去初始化对象再去调用方法名'''
    #key_demo().if_demos()#调用的时候 需要先初始化创建对象即f 再去调用方法
    key_demo.if_demos('self')
