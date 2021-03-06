#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Overall_5(object):
    driver1 = New_rename.Open.driver
    action = webdriver.ActionChains(driver1)
    lists = New_rename.Open.lists
    def risk_5(self):
        try:
            WebDriverWait(self.driver1,5,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]).click())#返回总体页面
        except:
            self.driver1.find_element_by_xpath(self.lists[39]).click()
        tem = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#获取所有tab标签位置信息
        tem = str(tem).replace('查看详情','').split('\n')#['0交易对手风险', '1关联交易风险', '2指标风险', '3财务异常', '4智能预警风险', '5法律风险', '6舆情风险', '7披露合规分析', '8结构风险', '']
        if self.lists[48] == tem[7]:
            self.driver1.find_element_by_xpath(self.lists[49]).click()
            name5 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name5 == '披露合规分析 ':
                    print('当前的模块 旧名称为：%s'%(name5))
                elif name5 == '披露合规分析':
                    print('当前的模块 新名称为：%s'%(name5))

            except:
                print('未定位到披露合规分析模块...%s' %(name5))
            #time.sleep(10)#仅做调试中暂停使用，不可用在程序中

            try:
                WebDriverWait(self.driver1,15,1).until_not(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))
                print('披露合规分析的解释语句还未添加')
            except:
                self.action.move_to_element(WebDriverWait(self.driver1,15,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
                txt5 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取

                try:
                    if txt5 == self.lists[15]:
                        print('披露合规分析 旧文案为：%s'%(txt5))
                    elif txt5 == self.lists[14]:
                        print('披露合规分析 新文案为：%s'%(txt5))
                    else:
                        print('披露合规分析的修改文案不正确：%s'%(txt5))

                except:
                    print('披露合规分析的修改文案不正确：%s'%(txt5))

        else:
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[6]/a').click()
            name5 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name5 == '披露合规分析 ':
                    print('当前的模块 旧名称为：%s'%(name5))
                elif name5 == '披露合规分析':
                    print('当前的模块 新名称为：%s'%(name5))

            except:
                print('未定位到 %s 模块...' %(name5))
            #time.sleep(10)#仅做调试中暂停使用，不可用在程序中

            try:
                WebDriverWait(self.driver1,15,1).until_not(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))
                print('披露合规分析的解释语句还未添加')
            except:
                self.action.move_to_element(WebDriverWait(self.driver1,15,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
                txt5 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取

                try:
                    if txt5 == self.lists[15]:
                        print('披露合规分析 旧文案为：%s'%(txt5))
                    elif txt5 == self.lists[14]:
                        print('披露合规分析 新文案为：%s'%(txt5))
                    else:
                        print('披露合规分析的修改文案不正确：%s'%(txt5))

                except:
                    print('披露合规分析的修改文案不正确：%s'%(txt5))
        return [txt5]


if __name__ == '__main__':
    Overall_5().risk_5()