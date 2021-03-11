''' 创建模块'''
def xxx():
    print(1)

'''  导入模块  第一种'''
#from xxx import  xx 或者 from xxx import  * 这个*慎用，只需要导入想用的就好；此外会依据就近原则覆盖其他同名的方法
#xx() #直接调用里边的方法

'''  导入模块  第二种'''
#import  xxx
xxx.xx() #用模块名调用里边的方法
