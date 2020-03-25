import xlrd

class New_name(object):
    def my_name(self):
        book = xlrd.open_workbook("../data/Csrc_pe.xlsx")
        xl = book.sheet_by_name('Sheet1')
        #print(xl.nrows)
        post_name = xl.col_values(3)[1:]
        #print(post_name)
        get_name =xl.col_values(5)[1:]
        #print(get_name)
        #print(len(get_name))
        '''
          for temp,tem in zip(post_name,get_name):
            par = {"account":"admin","deptName":"default",
                              "feedbackIndex":tem,"content":temp,"operation":0}
            print(par)
        '''
        return post_name,get_name
        #print(len(xl.col_values(3)[1:]))

if __name__ == '__main__':
    New_name().my_name()