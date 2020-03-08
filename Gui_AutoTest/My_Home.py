import unittest
from  Gui_AutoTest.Ui_demo import UiTest
class my_demo(UiTest):
    def my_test(self):
        self.driver.switch_to_default_content()
        self.driver.implicitly_wait(1)
        self.action.move_to_element(self.driver.find_element_by_xpath('//*[@id="US"]/header/div[1]/div[2]/div[2]/a')).perform()
        self.action.move_to_element(self.driver.find_element_by_xpath('//*[@id="user_item"]/li[2]')).click().perform()
        self.driver.implicitly_wait(5)
        my_txt = self.driver.find_element_by_xpath('//*[@id="US"]/div[2]/div[1]/div').text
        l = list(my_txt)[5:9]
        B = ''.join(l)
        C = B.replace(' ','')
        try:
            if self.assertEqual('我的收藏',C) == None:
                print('成功进入到我的收藏页面')
        except:
            print('未进入到我的收藏页面')

if __name__ == '__main__':
    my_demo().my_test()