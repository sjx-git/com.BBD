#coding:utf-8
import requests
import unittest
class Api_test1(unittest.TestCase):
    key = '959e4fc1aa5787e67ae143901b2d2673'
    url = 'http://apis.juhe.cn/simpleWeather/query'
    def test_post(self,city):
        #判断city是否为数字或者为汉字  （是否为字母 (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a')）
        if (city >= u'\u4e00' and city <=u'\u9fa5') or (city >= u'\u0030' and city<=u'\u0039' ) :
            par = {'key':self.key,'city':city}
            rets = requests.post(self.url,data=par).json()
            #print(rets)
            '''        
            if rets['error_code'] == 207301:
                print('暂不支持该城市')
            else:
                eq = rets['result']['city']
                if self.assertTrue(eq,city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
                    print('查询成功')
            '''
            try:
                eq = rets['result']['city']
                if self.assertTrue(eq,city) == None:##assertEqual 判断是否一致 ,true的情况下会返回None 错误会报错
                    print('查询成功')
            except:
                #print(rets)
                if rets['error_code'] == 207301:
                    print('暂不支持该城市')
                else:
                    print('输入不正确')
if __name__ == '__main__':
     Api_test1().test_post('1')