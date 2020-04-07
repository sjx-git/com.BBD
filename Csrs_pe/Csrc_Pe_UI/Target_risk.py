#coding:utf-8
from Csrs_pe.Csrc_Pe_UI import Open_csrc
from selenium.webdriver.support.wait import WebDriverWait
import re,time
from selenium import webdriver


class target_risk(object):
    driver1 = Open_csrc.Open.driver
    #action = webdriver.ActionChains(driver1)
    #lists = Open_csrc.Open.lists
    def risk(self):
        WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/ul/li[1]/a'))#返回总体页面
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/ul/li[1]/a').click()
        WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[1]/div/button'))
        txt = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[1]/div/button').text
        print(txt)
        WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[2]/i'))#获取所有tab标签位置信息
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[2]/i').click()

        self.driver1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]').click()
        time.sleep(1)
        self.driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]').send_keys(txt)
        # if self.lists[50] == tem[8]:
        #     WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[51]))
        #     self.driver1.find_element_by_xpath(self.lists[51]).click()
        #     name6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/span').text)#当前所在模块标题
        #     try:
        #         if name6 == '结构风险 ':
        #             print('结构风险 旧名称为：%s'%(name6))
        #         elif name6 == '结构风险':
        #             print('结构风险 新名称为：%s'%(name6))
        #
        #     except:
        #         print('未定位到结构风险模块...%s' %(name6))
        #
        #
        #     #self.driver1.refresh()
        #     #time.sleep(10)
        #     try:
        #         WebDriverWait(self.driver1,20,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i'))
        #         self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/i')).perform()
        #     except:
        #         txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        #
        #     txt6 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/p').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        #     #print(txt6)
        #     #txt6 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',txt6)
        #     try:
        #         if txt6 == self.lists[17]:
        #             print('结构风险的 旧文案为：%s'%(txt6))
        #         elif txt6 == self.lists[16]:
        #             print('结构风险的 新文案为：%s'%(txt6))
        #         else:
        #             print('结构风险的修改文案不正确：%s'%(txt6))
        #
        #     except:
        #         print('结构风险的修改文案不正确：%s'%(txt6))
        # return [txt6]
        time.sleep(10)
if __name__ == '__main__':
    target_risk().risk()