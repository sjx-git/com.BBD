#coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Csrc_tobelist import All_list

class Open(object):
    url = 'http://10.28.200.165/csrc_pe/#/riskMap'
    driver = webdriver.Chrome()
    #lists = All_list.All_list().lists()
    def open_url(self):
        desired_capabilities = DesiredCapabilities.CHROME  # 修改页面加载策略
        desired_capabilities["pageLoadStrategy"] = "none"  # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
        self.driver.maximize_window()
        self.driver.get(self.url)
        title = self.driver.find_element_by_xpath('//*[@id="rigthContent"]/div/div/div[2]/div/div[1]/span').text
        print(title)

        if title == '总体风险统计':
            print('当前模块为:%s'%(title))
        else:
            print('未进入指定模块中...')
        #time.sleep(20)
        #self.driver.close()


if __name__ == '__main__':
    Open().open_url()
