#coding:utf-8
#!/usr/bin/python3

class Demo_1(object):
    def Nice(self):
        i = 1
        while i <= 9:
             j = 1
             while j <= i:
                print("%d * %d = %d \t "%(j,i,i*j),end = " ")
                j += 1
             print(" ")
             i += 1
if __name__ == '__main__':
     Demo_1.Nice('self')