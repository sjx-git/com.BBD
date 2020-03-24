import  requests,json
from Csrs_pe import Headers_demo
from Csrs_pe import Time_demo

class target(object):
    #第一步设置url信息
    url1 = 'http://10.28.200.165/csrc_pe/api/v1.0/risk/investigation/index/feedback/insert'
    #第二步设置header信息
    header = Headers_demo.headers_demo().New_headers()
    #第三部设置必要的参数
    time2 = Time_demo.New_datetime().my_time()
    par = json.dumps({"account":"admin","deptName":"default","updateTime":time2,
                      "feedbackIndex":"naturalPerson","content":"1","operation":0})
    def Target_new(self):
        res = requests.post(self.url1,headers = self.header,data=self.par)
        #print(res.text)
        print(res.json())

if __name__ == '__main__':
    target().Target_new()