list = ['hi','world','are','you','ok?']
list1 = ['Good']
'添加单个字符或者列表 在最后，会将列表整个加进去[[新加的列表]]'
list.append('yes')
print(list)
'按下标添加'
list.insert(0,'haha')
print(list)
'只能合并列表，不能添加单个字符，不同于append ，[,新增的列表数据，合并到一起]'
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

'排序 从小到大'
list.sort()
print(list)
'排序 从小到大'
list.sort(reverse=True)
print(list)
'排序 颠倒位置'
list.reverse()
print(list)