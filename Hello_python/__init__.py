'''
一个包下，必须有此方法 在别的地方才可以引用，即便此方法是空的
'''

'''  这个方法有可用  不过好像还有个set函数可以直接找出相同的部分，待研究'''
class key_demo:
    ''' 用来找出重构后，新的json中不正确的key和value值'''
    def xx(self):
        old_json = [{'a':2,'b':3},{'e':4,'f':5,'q':{'w':7,'r':8}}]
        o3 = []
        for temp in old_json:
            for o,p in temp.items():
                o3.append(o)
        else:
            return o3
    def new_json(self):
        new_json = [{'a':2, 'b':3},{'e':4,'F':5,'Q':{'w':7,'r':8}}]
        o2 = []
        for temp1 in new_json:
            for o1,p1 in temp1.items():
                o2.append(o1)
        else:
            return o2
    def if_demo(self):
        L = []
        for A in key_demo.new_json('self'):
            if A not in key_demo.xx('self'):
                L.append(A)
        else:
            print('不正确的key为：%s'%L)
if __name__ == '__main__':
    #print(xxx.xx('self'))
    #print(xxx.new_json('self'))
    key_demo.if_demo('self')



