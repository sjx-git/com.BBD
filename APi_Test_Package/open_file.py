import xlrd
import requests
import unittest
class API_Test(unittest.TestCase):
    city = ''
    key = ''
    def setUp(self):
        print("开始")
    def tearDown(self):
        print("结束")
    def xlsx(self):
        book = xlrd.open_workbook("../data/data1.xlsx")
        res = book.sheet_by_name("Sheet1")
        #print(res.nrows)
        #print(res.row_values(1)[0])
        globals
        city = res.row_values(1)[0]
        globals
        key = res.col_values(1)[1]
        #print(city)
        #print(key)
    def test01(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        print(API_Test.city)
        print(self.key)
        par = {"city":API_Test.city,"key":API_Test.key}
        res = requests.get(url,params=par).json()
        print(res)
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])
    def test02(self):
        url = "http://apis.juhe.cn/simpleWeather/wids"
        post_res = requests.post(url,data ={"key":API_Test.key}).json()
        print(post_res['reason'])
        self.assertEqual(post_res['reason'],'查询成功')


if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    unittest.main()
    #API_Test.xlsx("self")