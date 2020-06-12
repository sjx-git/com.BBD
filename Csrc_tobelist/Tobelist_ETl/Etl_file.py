import pandas as pd
import os
class Etl():
    def etl_get(self):
        pd_res = pd.read_excel('../../data/Csrc_tobelist.xlsx')
        print(pd_res.head(5))
        print(pd_res.info())


if __name__ == '__main__':
    Etl().etl_get()