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
    """装饰器
    def b(name2):
        def c(name3):
            print(name2+name3)
            a()
        return c
        
    #闭包
    def d(name4):
        def e(name5):
            print(name5+name4)
            a()
        return e
    
    @b#等价于a=b(a)
    @d#等价于a=d(a)
    def a(name1):
        print("底层方法")
    a()
    """
    """装饰器 对有参数的&&不定长参数 装饰
    def b(name2):
        def c(*args,**kwargs):
            print(name2+name3)
            a(*args,**kwargs)
        return c
        
    @d#等价于a=d(a)
    def a(a,b):
        print("a= %d,b=%d"%(a,b))
    a(11,22)
    """
    """装饰器 对带有参数的&&有返回值&&不定长参数 装饰
    def b(name2):
        def c(*args,**kwargs):
            print(name2+name3)
           ret =  a(*args,**kwargs)
           return ret
        return c
        
    @d#等价于a=d(a)
    def a(a,b):
        print("a= %d,b=%d"%(a,b))
        return  "ret"
    a(11,22)
    """
    """装饰器 通用装饰器
   def b(name2):
       def c(*args,**kwargs):
           print(name2+name3)
          ret =  a(*args,**kwargs)
          return ret
       return c
       
   @d#等价于a=d(a)
   def a(a,b):
       print("a= %d,b=%d"%(a,b))
       return  "ret"
   a(11,22)
   """
"""装饰器 有参数的装饰器
   def f(arg) 
       def b(name2):
           def c(*args,**kwargs):
               print(name2+name3)
              ret =  a(*args,**kwargs)
              return ret
           return c
       return b
   @f("heihei")
   def a(a,b):
       print("a= %d,b=%d"%(a,b))
       return  "ret"
   a(11,22)
   """
if __name__ == '__main_':
    #调用类方法 第一种
    demo = Demo()
    demo.all_demo()
    #调用类方法，第二种
    Demo.all_demo()