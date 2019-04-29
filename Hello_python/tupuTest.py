print("="*50)
print("   名片管理系统")
print("1  添加一个名片")
print("2  修改一个名片")
print("3  查询一个名片")
print("4  删除一个名片")
print("5  退出系统")
print("="*50)


cards_info = []
while True:
    num = int(input("请输入要进行的操作："))

    if num == 1:
        cards = {}
        name = input("请输入名字：")
        age = int(input("请输入年龄："))
        address = input("请输入地址：")
        cards["name"] = name
        cards["age"] = age
        cards["address"] = address
        cards_info.append(cards)
        print(cards_info)
    elif num == 2:
        pass
    elif num == 3:
        mm = []
        nam = input("要查询的名字是：")
        for temp in cards_info:
            gg = temp.get("name")
            mm.append(gg)
            # a =  mm.append(gg)
        if nam in mm:
            print("已找到")
        else:
            print("这个人不存在")
    elif num == 4:
        pass
    elif num == 5:
        break
    else:
        print("输入错误，请重新输入")