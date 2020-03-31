#coding:utf-8
from Csrc_tobelist import New_rename
from selenium.webdriver.support.wait import WebDriverWait
import time

class Overall_2(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action

    def risk_2(self):
        WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/ul/li/ul/li[2]/a').click())
        # WebDriverWait(self.driver1,30,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[3]'))
        # tx = self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[3]').text#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        # tx1 = re.match(r'.+',tx)
        #print(tx1.group())
        self.driver1.find_element_by_xpath('//*[@id="anchor-classifyOverview"]/div[2]/button[3]/a').click()
        name2 = WebDriverWait(self.driver1,50,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/span').text)#当前所在模块标题

        try:
            if name2 == '风险指标体系':
                print('当前的模块 旧名称为：%s'%(name2))
            elif name2 == '指标风险':
                print('当前的模块 新名称为：%s'%('指标风险'))

        except:
            print('未定位到 %s 模块...' %(name2))

        #time.sleep(10)#仅做调试中暂停使用，不可用在程序中
        self.action.move_to_element(WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[1]/i'))).perform()#这里要注意，必须要讲？中的内容展开，才能定位到下面的内容
        txt2 = WebDriverWait(self.driver1,70,1).until(lambda x:self.driver1.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div').text)#暂时不明白如何取出text()中的内容，只能全部取出后，用正则提取
        #print(txt2)
        #print(type(tx))
        try:
            if txt2 == ('指标风险值的评价规则是:\n'
                        '若拟上市公司报告期内三年的毛利率存在异常，则指标风险值为100*权重；\n'
                        '若拟上市公司报告期内二年的毛利率存在异常，则指标风险值为80*权重；\n'
                        '若拟上市公司报告期内一年的毛利率存在异常，则指标风险值为60*权重；'):
                print('风险指标体系的 旧文案为：%s'%(txt2))
            elif txt2 == '利用业务经验整理的指标体系评价公司，触发阈值的指标越多，风险值越高。':
                print('风险指标体系的 新文案为：%s'%('利用业务经验整理的指标体系评价公司，触发阈值的指标越多，风险值越高。'))
            else:
                print('风险指标体系的修改文案不正确：%s'%(txt2))

        except:
            print('风险指标体系的修改文案不正确：%s'%(txt2))

        #time.sleep(10)


if __name__ == '__main__':
    Overall_2().risk_2()