from  Gui_AutoTest.Ui_demo import UiTest
class sign_demo(UiTest):
    def SignTest(self):
        self.driver.find_element_by_class_name('icon-pic-reg').click()
        self.driver.implicitly_wait(1)
        #当iframe 没有id name  index也切不过去 发现是出于div下的，只能先切到div在切进去
        g = self.driver.find_element_by_xpath('//div[@id="loginiframe"]//iframe')
        UiTest.driver.switch_to.frame(g)
        #隐式等待
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath('//div[@class="input-box email"]').click()
        self.driver.find_element_by_xpath('//input[@type = "text"]').send_keys('1064200847@qq.com')
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('//div[@class="input-box pw"]').click()
        self.driver.find_element_by_xpath('//input[@type = "password"]').send_keys('1992111122')
        self.driver.find_element_by_xpath('html/body/div[1]/div[4]/a[1]').click()
        self.driver.close()
if __name__ == '__main__':
    sign_demo.SignTest('self')