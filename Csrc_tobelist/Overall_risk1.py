#coding:utf-8
from Csrc_tobelist import New_rename,Overall_risk8
from selenium.webdriver.support.wait import WebDriverWait
import re,time
from selenium import webdriver


class Overall_1(object):
    driver1 = New_rename.Open.driver#此处并非是 不想直接使用webdriver声明，只是想用用open中的driver统一驱动，后边在研究各自声明driver  是不是还要各自打开一个浏览器 暂时这么用
    action = webdriver.ActionChains(driver1)
    lists = New_rename.Open.lists

    def risk_1(self):
        try:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()#返回总体页面
        tem = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#获取所有tab标签位置信息
        #WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[1]/a'))#进入交易对手风险,仅用于不需要改动的前提下
        tem = str(tem).replace('查看详情','').split('\n')#['交易对手风险', '关联交易风险', '指标风险', '财务异常', '智能预警风险', '法律风险', '舆情风险', '披露合规分析', '结构风险', '']
        #print(tem)
        if self.lists[36] == tem[0]:
            WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[37]))#进入交易对手风险
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[1]/a').click()
            WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span'))
            name1 = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/span').text#当前所在模块标题
            try:
                if name1 == self.lists[36]:
                    print('交易对手风险的：%s'%(name1))
            except:
                print('未定位到交易对手风险的模块...%s'%(name1))
            self.action.move_to_element(WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i')))#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
            self.action.move_to_element(self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[1]/i')).click_and_hold().perform()
            WebDriverWait(self.driver1,20,0.5).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div'))#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
            tx = self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div').text
            txt1 = re.sub(r'This text is displayed if your browser does not support the Canvas HTML element\.\n','',tx)
            try:
                if txt1 == self.lists[3]:
                    print('交易对手风险的 旧文案为：%s'%(txt1))
                elif txt1 == self.lists[2]:
                    print('交易对手风险的 新文案为：%s'%(txt1))
            except:
                print('交易对手风险的 新文案修改不正确：%s'%(txt1))
            return [txt1]
        elif self.lists[36] == tem[9]:
            pass



if __name__ == '__main__':
    Overall_1().risk_1()