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
    col = Name_demo.New_name().my_name()

    def Target_new(self):
        for temp in self.col:
            par = json.dumps({"account":"admin","deptName":"default","updateTime":self.time2,
                              "feedbackIndex":"naturalPerson","content":temp,"operation":0})
            res = requests.post(self.url1,headers = self.header,data=par)
            #print(res.text)
            #print(res.json())
            print('后端指标---%s---的反馈内容是:---%s---,反馈结果是:---%s---'%("naturalPerson",temp,res.json()['data']))

if __name__ == '__main__':
    target().Target_new()