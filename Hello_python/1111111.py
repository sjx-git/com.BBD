re = [{"name":"sunjiaxing","age":11,"adress":"ssss"},{"name":"wangzhne","age":11,"adress":"sssss"}]

nn = []
#print(nn.append(1))
for temp in re:

    #print(temp)
    #va = temp.get("name")
    va = temp.get("name")
    #print(va)
    nn.append(va)


print(nn)

    #print(nn.append(va))

if "sunjiaxing" in nn:
    print("ok")
else:
    print("no")
#print(na.append(va))
