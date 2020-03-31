#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import re


class Overall_1(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action

    def risk_1(self):
        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[1]/a'))
        self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[1]/a').click()
        try:
            WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span'))
            name1 = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span').text#当前所在模块标题
            print('当前的模块为：%s'%(name1))
        except:
            print('未定位到 %s 模块...'%(name1))
        #time.sleep(3)#仅做调试中暂停使用，不可用在程序中
        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i'))
        self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i')).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div'))
        tx = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div').text#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        # print(tx)
        # print(type(tx))
        txt1 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',tx)
        try:
            if txt1 == '利用业务经验整理的指标体系评价公司，触发阈值的指标越多，风险值越高。':
                print('交易对手风险的 旧文案为：%s'%(txt1))
            elif txt1 == '利用工商数据对公司交易对手进行真实性分析，客户、供应商为新成立公司、注册资本少等情况越多，风险值越高。':
                print('交易对手风险的 新文案为：%s'%('利用工商数据对公司交易对手进行真实性分析，客户、供应商为新成立公司、注册资本少等情况越多，风险值越高。'))
        except:
            print('交易对手风险的 新文案修改不正确：%s'%(txt1))
        #time.sleep(10)
if __name__ == '__main__':
    Overall_1().risk_1()