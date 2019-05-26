import requests
import unittest
class API_Test(unittest.TestCase):
    Appkey = "959e4fc1aa5787e67ae143901b2d2673"
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    def test01(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        #city = input("请输入要查询的城市名称：")
        par = {"city":"北京","key":API_Test.Appkey}
        res = requests.get(url,params=par).json()
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])
    def test02(self):
        url = "http://apis.juhe.cn/simpleWeather/wids"
        post_res = requests.post(url,data ={"key":API_Test.Appkey}).json()
        print(post_res['reason'])
        self.assertEqual(post_res['reason'],'查询成功')

    def re_session(self):
        pass
        """
        当有需要验证信息比如：session的时候，就需要用
        s = request.session() 来保持和下一个接口建立相同的链接通道
        res = s.get(url) 正常用就好了
        导入正则包 re 
        usersession = re.findall(r'正则表达式(.+？)'，res)
        此时的session就可以用了  取出的是列表  用usersession[0]
        """

if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    unittest.main()