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

        risk5 = res.row_values(10)[4]
        risk5_old = res.row_values(10)[5]

        risk6 = res.row_values(11)[4]
        risk6_old = res.row_values(11)[5]

        risk7 = res.row_values(12)[4]
        risk7_old = res.row_values(12)[5]

        risk8 = res.row_values(3)[4]
        risk8_old = res.row_values(3)[5]

        risk9 = res.row_values(17)[4]
        risk9_old = res.row_values(17)[5]

        risk10 = res.row_values(19)[4]
        risk10_old = res.row_values(19)[5]

        risk11 = res.row_values(20)[4]
        risk11_old = res.row_values(20)[5]

        risk11_1 = res.row_values(21)[4]
        risk11_1_old = res.row_values(21)[5]

        risk12 = res.row_values(14)[4]
        risk12_old = res.row_values(14)[5]

        risk13 = res.row_values(27)[4]
        risk13_old = res.row_values(27)[5]

        risk14 = res.row_values(13)[4]
        risk14_old = res.row_values(13)[5]

        risk15 = res.row_values(29)[4]
        risk15_value = res.row_values(29)[5]

        risk16 = res.row_values(38)[4]
        risk16_value = res.row_values(38)[5]

        risk17 = res.row_values(30)[4]
        risk17_value = res.row_values(30)[5]

        risk18 = res.row_values(31)[4]
        risk18_value = res.row_values(31)[5]

        risk19 = res.row_values(32)[4]
        risk19_value = res.row_values(32)[5]

        risk20 = res.row_values(33)[4]
        risk20_value = res.row_values(33)[5]

        risk21 = res.row_values(34)[4]
        risk21_value = res.row_values(34)[5]

        risk22 = res.row_values(35)[4]
        risk22_value = res.row_values(35)[5]

        risk23 = res.row_values(36)[4]
        risk23_value = res.row_values(36)[5]

        risk24 = res.row_values(37)[4]
        risk24_value = res.row_values(37)[5]





        return [risk,risk_old,risk1,risk1_old,risk2,risk2_old,risk2_1,risk2_1_old,risk3,risk3_old,risk4,risk4_old,risk4_1,risk4_1_old,risk5,risk5_old,risk6,risk6_old
        ,risk7,risk7_old,risk8,risk8_old,risk9,risk9_old,risk10,risk10_old,risk11,risk11_old,risk11_1,risk11_1_old,risk12,risk12_old,risk13,risk13_old,risk14,risk14_old,
        risk15,risk15_value,risk16,risk16_value,risk17,risk17_value,risk18,risk18_value,risk19,risk19_value,risk20,risk20_value,risk21,risk21_value,risk22,risk22_value,risk23,risk23_value,
        risk24,risk24_value

        ]





if __name__ == '__main__':
    pass
    #All_list().lists()