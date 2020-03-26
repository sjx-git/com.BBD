from Csrs_pe  import Headers_demo,Oldname_demo
import  requests,json,random
class old_name(object):
    '''
    #此类方法，是用for循环的方式 通过以列为单位，获取到id，但是没法同时获取到name，所以用下面的方法
    #range只能跟范围，列表就需要用random.choices；random.sample(list，2)  #随机返回参数列表中任意两个元素，参数二指定返回的数量
    for temp in random.choices(old_uid):
        #print(temp)
        data1 = json.dumps({   "account": "admin","deptName": "default","allIndex": "false","indexNames": old_post_name,
            "pofMngmntPsnIds": [temp]   }
                )
        '''
    head = Headers_demo.headers_demo().New_headers()
    old_post_name,old_name1,old_id = Oldname_demo.old_name().My_oldname()
    url1 = 'http://10.28.200.165/csrc_pe/api/v1.0/risk/investigation/index/self/check'
    data1 = json.dumps({
        "account": "admin", "deptName": "default","allIndex": "false","indexNames": old_post_name,
        "pofMngmntPsnIds": [old_id]}
     )#这里的参数需要的是列表，转一下

    def My_oldName(self):
        res = requests.post(self.url1,headers = self.head,data=self.data1)
        #print(self.data1)
        #print(res.json())
        print('发送的指标的个数是：%s，管理人id是：---%s---,管理人名称是：%s，结果是：---%s---'%(len(self.old_post_name),self.old_id,self.old_name1,res.json()["message"]))

if __name__ == '__main__':
    old_name().My_oldName()
