'''
一个包下，必须有此方法 在别的地方才可以导入这个包，即便此方法是空的，但是也仅仅是允许导入包，它下面的模块却是不能用的；
若是想用，那么就要用到 __all__ = ['模块名']；或者 from . import 模块名---这两有点麻烦；
发布模块，作用相当于系统内置模块 是在所有地方都可用，不用再用all啥的写明，见setup文件内容
'''
"""__all__ = []
from . import caiquan"""


def task_demo(func):

    class Task(object):
        __instance = None
        __res = False

        def __new__(cls, *args, **kwargs):
            if cls.__instance == None:
                cls.__instance = object.__new__(cls)
                return cls.__instance
            else:
                return cls.__instance

        def __init__(self,name):

            if self.__res == False:
                self.name = name
                self.__res = True
    return Task


@task_demo
class Temp(object):
    def __init__(self,name):
        self.name = name


dog = Temp('汤姆')
print(dog.name)
dog1 = Temp('啸天犬')
print(dog1.name)
if id(dog) == id(dog1):
    print('对象单例设置成功，dog对象的id地址是：%d，dog1对象的id地址是：%d'%(id(dog),id(dog1)))
else:
    print('对象单例设置失败')

