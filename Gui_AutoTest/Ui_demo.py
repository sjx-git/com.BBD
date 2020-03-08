from selenium import webdriver
import unittest
class UiTest(unittest.TestCase):
    #初始化driver
    driver = webdriver.Chrome()
    action = webdriver.ActionChains(driver)
    def Open_dealmoon(self):
        url1 = 'http://www.dealmoon.com'
        #初始化driver
        #WebDriverWait(driver,10,0.5) #显示等待
        self.driver.get(url1)
        #print(self.driver.current_url)
        title_1  = self.driver.title
        if self.assertEqual(title_1,'北美省钱快报 - 北美网购指南 - 24小时滚动更新北美商家折扣信息') == None:
            print('国内镜像站')
        else:
            print('国外镜像站')

if __name__ == '__main__':
    UiTest().Open_dealmoon()
