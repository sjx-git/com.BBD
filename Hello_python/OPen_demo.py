#def OpenDemo():
    #打开一个文件
    old_name = input("请输入你要打开的文件名字")
    #根据输入的文件名称，通过截取不带后缀的名称+复件两字+截取后缀 组成新的文件名称
    index = old_name.rfind(".")
    New_name = old_name[:index] + ("复件") + ".py"
    #打开输入的文件，并写入一些东西
    f = open(old_name,"w+")
    f.write("Hello  World")
    #读取出文件内容
    a = open(old_name,"r+").read()

    #打开输入的文件，并写入一些东西
    n = open(New_name,"w+")
    n.write(a)
    new_a = open(New_name,"r").read()
    #读取出文件内容

    print("new_a%s "%(new_a))
    print("old_a%s"%(a))
    f.close()
    n.close()
    #

#if __name__ == 'main':
 #   OpenDemo()