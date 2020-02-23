dict = {'name':'liming','age':11}

'get key方式获取到value'
print(dict.get('name'))

'获取到key'
print(dict.keys())

'获取到value'
print(dict.values())

'获取到key,value'
print(dict.items())

'for循环遍历，并用元祖的拆包方式，取出key value的值'
for key,value in dict.items():
    print('key:%s,value:%s'%(key,value))