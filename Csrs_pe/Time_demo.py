import datetime

class New_datetime(object):
    def my_time(self):
        time1 = datetime.datetime.now()#获取当前时间
        time2 = datetime.datetime.strftime(time1,'%Y-%m-%d %H:%M')#将时间对象转换成我们想要的字符串格式
        #print(time1,time2)
        return time2

if __name__ == '__main__':
    New_datetime().my_time()
