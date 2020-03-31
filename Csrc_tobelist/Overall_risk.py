#coding:utf-8
from Csrc_tobelist import New_rename


class Overall(object):
    driver1 = New_rename.Open.driver
    action = New_rename.Open.action

    def risk(self):
        try:
            name = self.driver1.find_element_by_class_name('activeItem__D3Lq8').text
            print('当前的模块为：%s'%(name))
        except:
            print('未定位到指定模块...')
        txt = self.driver1.find_element_by_class_name('secondTopBarTitle__1j4tQ').text
        try:
            if  txt == "风险分类分析":
                print('总体风险--风险分类分析的 旧名称为：%s'%(txt))
            elif txt == '分类风险情况':
                print('总体风险--风险分类分析的 新名称为：%s'%('分类风险情况'))
        except:
            print('总体风险--风险分类分析 所修改的名称不正确:%s'%(txt))
        #time.sleep(10)
if __name__ == '__main__':
    Overall().risk()