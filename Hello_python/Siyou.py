'''  私有方法'''

class Siyou():
    def __siyou(self):#私有方法
        print('发送短信ing')
    def siyou_demo(self,money):#共有方法
        if money>0:
            self.__siyou()
        else:
            print('余额不足')
if __name__ == '__main__':
    Siyou().siyou_demo(-1)
    #Siyou().__siyou()  类的私有方法 不允许调用，但可以在实例中调用