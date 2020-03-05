#coding:utf-8
import requests
import unittest
class Api_test(unittest.TestCase):
    key = '959e4fc1aa5787e67ae143901b2d2673'
    get_url = 'http://apis.juhe.cn/simpleWeather/wids'
    def test_get(self):
        par = {"key":self.key}
        ret = requests.get(self.get_url,params = par).json()
        #print(ret)
        try:
            ##assertIn 判断是否包含在里边 ,true的情况下会返回None 错误会报错
            if self.assertIn(ret['reason'],'查询成功') == None:
                print('查询成功！')
        except:
            if self.assertIn(ret['resultcode'],'112') ==None:
                 print('没次数了')


if __name__ == '__main__':
    t  = Api_test()
    t.test_get()