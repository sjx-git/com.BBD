#列别名  当模块名很长的时候  可以用as 重新命名
import time as  tt
tt.sleep(1)
class Demo(object):#类方法的命名，大驼峰的方式
    #第一行，用来描述这是干嘛用的意义所在
    #类属性
    num = 0
    #实例方法
    def __fun_demo__(self):#实例方法的命名方式，下划线    __名字__私有方法      方法self 必须写上     函数可以不写
        pass
    #类方法
    @classmethod
    def all_demo(cls):
        pass
    #静态方法
    @staticmethod
    def print_menu():# 可以不写self
        pass

if __name__ == '__main_':
    demo = Demo()
    #调用类方法 第一种
    demo.all_demo()
    #调用类方法，第二种
    Demo.all_demo()