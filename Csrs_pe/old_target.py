from Csrs_pe  import Headers_demo,Oldname_demo
import  requests,json,random
class old_name(object):
    head = Headers_demo.headers_demo().New_headers()
    old_post_name,old_uid = Oldname_demo.old_name().My_oldname()
    url1 = 'http://10.28.200.165/csrc_pe/api/v1.0/risk/investigation/index/self/check'
    #range只能跟范围，列表就需要用random.choices
    for temp in random.choices(old_uid):
        print(temp)
        data1 = json.dumps({
            "account": "admin",
            "deptName": "default",
            "allIndex": "false",
            "indexNames": old_post_name,
            "pofMngmntPsnIds": [temp]
        }
    )
    def My_oldName(self):
        res = requests.post(self.url1,headers = self.head,data=self.data1)
        #print(res.json())
        print('发送结果是：%s'%(res.json()["message"]))

if __name__ == '__main__':
    old_name().My_oldName()
