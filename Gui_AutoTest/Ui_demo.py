from selenium import webdriver
class UiTest(object):
    #初始化driver
    driver = webdriver.Chrome()
    def Open_dealmoon(self):
        url1 = 'http://www.dealmoon.com'
        #初始化driver
        #WebDriverWait(driver,10,0.5) #显示等待
        self.driver.get(url1)

if __name__ == '__main__':
    UiTest().Open_dealmoon()
