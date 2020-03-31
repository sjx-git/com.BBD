import xlrd

class All_list(object):
    def lists(self):
        book = xlrd.open_workbook('./data/Csrc_tobelist.xlsx')
        res = book.sheet_by_name('Sheet1')

        risk = res.row_values(2)[4]
        risk_old = res.row_values(2)[5]

        risk1 = res.row_values(4)[4]
        risk1_old = res.row_values(4)[5]

        risk2 = res.row_values(5)[4]
        risk2_old = res.row_values(5)[5]

        risk2_1 = res.row_values(6)[4]
        risk2_1_old = res.row_values(6)[5]

        risk3 = res.row_values(7)[4]
        risk3_old = res.row_values(7)[5]

        risk4 = res.row_values(8)[4]
        risk4_old = res.row_values(8)[5]

        risk4_1 = res.row_values(9)[4]
        risk4_1_old = res.row_values(9)[5]

        return risk,risk_old,risk1,risk1_old,risk2,risk2_old,risk2_1,risk2_1_old,risk3,risk3_old,risk4,risk4_old,risk4_1,risk4_1_old






if __name__ == '__main__':
    All_list().lists()