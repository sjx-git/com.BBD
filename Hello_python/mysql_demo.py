#encoding = utf-8
#!/usr/bin/python3
from pymysql import connect,cursors

class mysql_demo(object):
    def mysql_open(self):
        db = connect(host='192.168.52.137', user='root', password="sjx@123A",database='test', port=3306, charset='utf8')
        cour = db.cursor()
        rr = cour.execute('select * from test1')
        print(rr)

if __name__ == '__main__':
    mysql_demo().mysql_open()