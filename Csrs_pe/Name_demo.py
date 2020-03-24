import xlrd

class New_name(object):
    def my_name(self):
        book = xlrd.open_workbook("../data/Csrc_pe.xlsx")
        xl = book.sheet_by_name('Sheet2')
        #print(xl.nrows)
        col_num = xl.col_values(3)[1:]
        #print(col_num)
        return col_num
        #print(len(xl.col_values(3)[1:]))

if __name__ == '__main__':
    New_name().my_name()