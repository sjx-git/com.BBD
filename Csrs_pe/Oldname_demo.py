import  xlrd

class old_name(object):
    def My_oldname(self):
        book = xlrd.open_workbook("../data/Csrc_pe.xlsx")
        xl = book.sheet_by_name('Sheet2')
        #print(xl.nrows)
        old_post_name = xl.col_values(0)[1:]
        old_id = xl.col_values(3)[1:]
        #print(old_post_name)
        return old_post_name,old_id

if __name__ == '__main__':
    old_name().My_oldname()