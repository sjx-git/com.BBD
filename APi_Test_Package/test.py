import xlrd
import requests
import unittest
class API_Test(object):
    key = None
    city = None
    def xlsx(self):
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
        print(city)
        print(key)
        par = {"city":city,"key":key}
        res = requests.get(url,params=par).json()
        print(res)
        print(res['result']['realtime']['info'])
        self.assertIn('晴',res['result']['realtime']['info'])
if __name__ == '__main__':
    #API_Test.get_url('self')
    #API_Test.post_url("self")
    #unittest.main()
    API_Test.xlsx("self")
    API_Test.test01('self')