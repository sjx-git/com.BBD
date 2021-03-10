'类方法：用classmethod标识，可以直接用类名.类方法()调用，括号里边不需要穿self或者cls ' \
'类属性：和类有关系；同一个类属性是可以在不同的实例对象之间共享的，直接拿来用就可以 ' \
'实例方法：初始化一个类之后得到的' \
'实例属性：和具体的实例对象有关系；每个实例属性在不同的实例对象之间是不共享的，需要去调用才可以用   ' \
'静态属性：用staticmethod标识，可以直接用类名.静态方法()调用；也可以用实例化的对象去调用，'
class Demo(object):
    #类属性
    num = 0
    #类方法
    @classmethod
    def cls(cls):
        Demo.num = 10
    #实例方法
    def def_demo(self):
        #实例属性
        self.name = 'liming '
    #静态方法
    @staticmethod
    def sta_demo():
        print('静态方法')
demo = Demo()
'调用类方法和类属性，直接类名.   调用就可以'
Demo.cls()
print(Demo.num)
print(demo.num)

'调用实例方法和实例属性'
demo.def_demo()
'调用静态方法 直接用类名.静态方法()调用；也可以用实例化的对象去调用 '
Demo.sta_demo()
demo.sta_demo()
