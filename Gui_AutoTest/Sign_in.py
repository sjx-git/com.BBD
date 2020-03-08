from selenium.webdriver.support.wait import WebDriverWait
from  Gui_AutoTest.Ui_demo import UiTest
import time
class sign_demo(UiTest):
    def SignTest(self):
        self.driver.find_element_by_class_name('icon-pic-reg').click()
        self.driver.implicitly_wait(1)
        #当iframe 没有id name  index也切不过去 发现是出于div下的，只能先切到div在切进去
        g = self.driver.find_element_by_xpath('//div[@id="loginiframe"]//iframe')
        self.driver.switch_to.frame(g)
        #隐式等待
        self.driver.implicitly_wait(10)
        #当imput在div标签下，需要先定位到div，然后click，之后再定位到input，才能send   不可以直接定位到input那
        self.driver.find_element_by_xpath('//div[@class="input-box email"]').click()
        self.driver.find_element_by_xpath('//input[@type = "text"]').send_keys('1064200847@qq.com')

        self.driver.switch_to_default_content()
        self.driver.switch_to.frame(g)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath('//div[@class="input-box pw"]').click()
        self.driver.find_element_by_xpath('//input[@type = "password"]').send_keys('1992111122')
        #self.driver.implicitly_wait(50000)
        self.driver.find_element_by_xpath('html/body/div[1]/div[4]/a[1]').click()
        #返回默认iframe
        #

        self.driver.switch_to_default_content()
        time.sleep(4)
        try:

            txt = self.driver.find_element_by_xpath('//*[@id="US"]/header/div[1]/div[2]/div[2]/a/em').text
            if self.assertIn('哈哈哈哈哈哈哈不好哈哈哈哈',txt) == None:
                print('%s 登录成功'%(txt))
        except:
            print('没获取到名字')
if __name__ == '__main__':
    sign_demo.SignTest('self')