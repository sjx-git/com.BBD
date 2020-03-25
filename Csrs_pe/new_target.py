import requests,json
from Csrs_pe import Headers_demo
from Csrs_pe import Time_demo
from Csrs_pe import Name_demo
class target(object):
    #第一步设置url信息
    url1 = 'http://10.28.200.165/csrc_pe/api/v1.0/risk/investigation/index/feedback/insert'
    #第二步设置header信息
    header = Headers_demo.headers_demo().New_headers()
    #第三部设置必要的参数
    time2 = Time_demo.New_datetime().my_time()
    post_name,get_name = Name_demo.New_name().my_name()

    def Target_new(self):
        '''
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
        '''
        for temp,tem in zip(self.post_name,self.get_name):
            par = json.dumps({"account":"admin","deptName":"default","updateTime":self.time2,
                              "feedbackIndex":tem,"content":temp,"operation":0})
            res = requests.post(self.url1,headers = self.header,data=par)
            #print(res.text)
            #print(res.json())
            print('后端指标---%s---的反馈内容是:---%s---,反馈结果是:---%s---'%(tem,temp,res.json()['data']))

if __name__ == '__main__':
    target().Target_new()