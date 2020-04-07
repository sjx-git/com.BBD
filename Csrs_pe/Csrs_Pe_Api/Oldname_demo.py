import  xlrd,random

class old_name(object):
    def My_oldname(self):
        book = xlrd.open_workbook("../data/Csrc_pe.xlsx")
        xl = book.sheet_by_name('可发送指标')
        '''
        #此类方法，是用获取列的方式，得到想要得id，但是不能同时获取到id和name，所以用下面的方法
        #print(xl.nrows)
        old_post_name = xl.col_values(0)[1:]#指标列表
        old_id = xl.col_values(3)[1:]#管理人id
        #old_name = xl.col_values(4)[1:]#管理人名称
        #print(old_post_name)
        return old_post_name,old_id
        '''
        old_post_name = xl.col_values(0)[1:]#指标列表
        s = random.randint(0,xl.nrows)#用ranint，获取一个数；random.randrange(1,10,2))   #随机一个大于等于1且小于等于10之间的奇数，其中2表示递增基数
        #print(s)
        #print(xl.row_values(s))
        old_post_name = xl.col_values(0)[1:32]#指标列表
        old_id = xl.row_values(s)[3]#管理人id
        old_name1 =xl.row_values(s)[4]#管理人名称
        #print(type(list(old_id)))
        #print(old_post_name,old_id,old_name1)
        return old_post_name,old_name1,old_id
if __name__ == '__main__':
    old_name().My_oldname()