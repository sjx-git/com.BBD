list = ['hi','world','are','you','ok?']
list1 = ['Good']
'添加在最后'
list.append('yes')
print(list)
'按下标添加'
list.insert(0,'haha')
print(list)
'合并列表'
list3  = list1 +list
print(list3)
list.extend(list1)
print(list)

'删除最后一个'
list.pop()
print(list)
'删除关键字'
list.remove('hi')
print(list)
'按下标删除'
del  list[2]
print(list)

'按下标更改'
list[1] = 'no'
print(list)

'查询 in  或者  not in'
if  'yes' in list:
    print('查到了')
if  'gun' not in list:
    print('不在这里边')