#coding:utf-8
from Csrc_tobelist.Tobelist_GUI import New_rename
from selenium.webdriver.support.wait import WebDriverWait


class Overall_3(object):
    ''' 智能预警风险 '''
    driver1 = New_rename.Open.driver
    lists = New_rename.Open.lists
    def risk_3(self):

        WebDriverWait(self.driver1,10,1).until(lambda x:self.driver1.find_element_by_xpath(self.lists[39]))
        self.driver1.find_element_by_xpath(self.lists[39]).click()#返回首页

        tem = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]').text)#获取所有tab标签位置信息
        tem = str(tem).replace('查看详情','').split('\n')#['0交易对手风险', '1关联交易风险', '2指标风险', '3财务异常', '4智能预警风险', '5法律风险', '6舆情风险', '7披露合规分析', '8结构风险', '']
        if self.lists[52] == tem[4]:
            self.driver1.find_element_by_xpath(self.lists[53]).click()#进入智能预警风险
            name3 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name3 == self.lists[9]:
                    print('智能预警风险 旧名称为：%s'%(name3))
                elif name3 == self.lists[8]:
                    print('智能预警风险 新名称为：%s'%(name3))
                else:
                    print('智能预警风险 未定位到：%s'%(name3))

            except:
                print('智能预警风险 未定位到：%s'%(name3))
        else:
            self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[8]/a').click()#进入智能预警风险
            name3 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题
            try:
                if name3 == self.lists[9]:
                    print('智能预警风险 旧名称为：%s'%(name3))
                elif name3 == self.lists[8]:
                    print('智能预警风险 新名称为：%s'%(name3))
                else:
                    print('智能预警风险 未定位到：%s'%(name3))

            except:
                print('智能预警风险 未定位到：%s'%(name3))
        return [name3]
        #time.sleep(10)


if __name__ == '__main__':
    Overall_3().risk_3()