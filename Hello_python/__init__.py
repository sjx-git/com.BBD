#coding:utf-8
#!/usr/bin/python3

class Hello(object):

    def Hi(self):
        age = input("请输入你要测试的的对象性别：")
        money = int(input("有多少钱"))
        high = input("多高")
        if age == '男':
            if money >10 and high >'160':
                print("你对象是高富帅")
            else:
                print("你对象是矮穷矬")

        else:
            if money >10 and high >'160':
                print("你对象是白富美")
            else:
                print("你对象是矮穷矬")
if __name__ == '__main__':
    Hello.Hi('self')