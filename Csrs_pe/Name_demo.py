import xlrd

class New_name(object):
    def my_name(self):
        book = xlrd.open_workbook("../data/Csrc_pe.xlsx")
        xl = book.sheet_by_index('Sheet1')
        print(xl.nrows)

if __name__ == '__main__':
    New_name().my_name()