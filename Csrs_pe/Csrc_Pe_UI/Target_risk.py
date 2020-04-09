#coding:utf-8
from Csrs_pe.Csrc_Pe_UI import Open_csrc
from selenium.webdriver.support.wait import WebDriverWait
import re,time
from selenium import webdriver


class target_risk(object):
    """
        投资者数量指标
    """
    driver1 = Open_csrc.Open.driver
    action = webdriver.ActionChains(driver1)
    #lists = Open_csrc.Open.lists
    def risk(self):
        WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/ul/li[1]/a'))
        self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div/ul/li[1]/a').click()#进入风险指标页面
        #获取指标名称
        WebDriverWait(self.driver1,20,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[1]/div/button'))
        txt = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[1]/div/button').text
        #print(txt)

        # 叹号 位置
        WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[2]/i'))
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[3]/div[1]/div[3]/div[1]/div[7]/span[2]/i').click()
        #定位到相关 富文本框，然后发送相关指标信息
        self.driver1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]').click()
        self.driver1.find_element_by_class_name('textSuggest__5q6iX').send_keys(txt)

        #点击提交
        self.action.move_to_element(self.driver1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[5]/button[1]')).click().perform()

        #点击反馈意见管理
        self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[2]/div[2]/button[4]').click()
        #获取涉及指标
        WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[5]'))
        txt_1= self.driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[5]').text
        #print(txt_1)
        #获取反馈内容
        WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[6]'))
        txt_1_1 = self.driver1.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[6]').text
        #print(txt_1_1)
        if (txt == txt_1_1) & (txt == txt_1):
            print('---指标：%s---的反馈信息内容是：%s---反馈信息 成功 涉及到的指标是：%s'%(txt,txt_1_1,txt_1))
        else:
            print('---指标：%s---的反馈信息内容是：%s---反馈信息 失败 涉及到的指标是：%s'%(txt,txt_1_1,txt_1))

        #关闭窗口，首先必须要先将该元素高亮显示(用检查是否存在即可达到该效果)
        WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rcDialogTitle1"]/div/button/span'))
        self.driver1.find_element_by_xpath('//*[@id="rcDialogTitle1"]/div/button').click()

        #time.sleep(10)


if __name__ == '__main__':

    target_risk().risk()