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
    @classmethod
    def setUpClass(self):
        book = xlrd.open_workbook("../data/data1.xlsx")
        res = book.sheet_by_name("Sheet1")
        #print(res.nrows)
        #print(res.row_values(1)[0])
        global city
        city = res.row_values(1)[0]
        global key
        key = res.col_values(1)[1]
        #print(city)
        #print(key)

    def test01(self):
        url = "http://apis.juhe.cn/simpleWeather/query"
        #print(city)
        #print(key)
        par = {"city":city,"key":key}
        res = requests.get(url,params=par).json()
        print(res)
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])
    def test02(self):
        url = "http://apis.juhe.cn/simpleWeather/wids"
        post_res = requests.post(url,data ={"key":key}).json()
        print(post_res['reason'])
        self.assertEqual(post_res['reason'],'查询成功')


if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    unittest.main()
    #API_Test.xlsx("self")