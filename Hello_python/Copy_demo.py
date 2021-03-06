'''  深拷贝和浅拷贝  栈中存放的是变量；堆中存放的是id地址和值;
        深/浅拷贝 可用于 列表/元组/字符串/字典；
        深/浅拷贝 用于不可变类型时，地址和值都是一样的；
        深/浅拷贝 用于可变类型时，=浅拷贝 地址和值都是一样的；copy浅拷贝 地址不同，值相同；deepcopy深拷贝，地址和值都不同。


'''
import copy
'''浅拷贝：拷贝第一层的关系，深一点的关系不会被拷贝
        会新开一个栈内存，用来存放新的变量，也就会导致id 不同；
        但值仍然是指向被拷贝对象的值,因此当原变量值被修改后，新变量值也会随着更改   --》这个针对的是可变类型
        不会新开一个栈内存，用来存放新的变量，也就会导致id 相同；
        但值仍然是指向被拷贝对象的值,因此当原变量值被修改后，新变量值也会随着更改   --》这个针对的是不可变类型     
'''

''' copy浅拷贝   也就是第一种浅拷贝'''
a = [1]
b = [10]
c = [a,b]
e = copy.copy(c)
a.append(3)
print(c,e)
print(id(c),id(e))

''' =浅拷贝   第二种浅拷贝'''
'''   此处有个大坑！ 如果用a[0].append就可以符合 浅拷贝的特性--a变b也变；
                  但是 用a.append那么 a列表就是个新的列表和b对应的原a列表就不一样了 就会导致 a变了而b却不会百变
'''
a = [[1]]
b = copy.copy(a)
a[0].append(2)
print(a,b)
print(id(a),id(b))


'''深拷贝：拷贝所有的层级关系
        会新开一个栈内存，用来存放新的变量，也就会导致id 不同；
        此时的值 不会 再指向被拷贝对象的值,而是再堆中新开一片内存；也因此当原变量值被修改后，新变量值 不会随着更改
'''
a1 = [1]
b1 = [10]
c1 = [a1,b1]
e1 = copy.deepcopy(c1)
a1.append(2)
print(c1,e1)
print(id(c1),id(e1))



