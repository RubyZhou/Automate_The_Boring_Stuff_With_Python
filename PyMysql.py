#!/usr/bin/python3
import pymysql

def sel():
# sel
    my_conn= pymysql.connect(host="192.168.92.128",
                         user='sa',
                         passwd='zhouyf',
                         db='cbs')
    my_cur=my_conn.cursor()

    my_cur.execute("select * from products")
    print()
    for row in my_cur:
        print(row)
    my_cur.close()
    my_conn.close()

def del(): #demo
    my_conn= pymysql.connect(host="192.168.92.128",
                         user='sa',
                         passwd='zhouyf',
                         db='cbs')
    my_cur=my_conn.cursor()
    sql = "delete from products where name = '%s' limit %d"
    datas = ('Sara', 2)
    my_cur.execute(sql % datas)
    my_conn.commit()
    print('成功删除姓名为', datas[0], '的', my_cur.rowcount, '条数据')

    my_cur.close()
    my_conn.close()

def ins(): #demo
    my_conn = pymysql.connect(host="192.168.92.128",
                              user='sa',
                              passwd='zhouyf',
                              db='cbs')
    my_cur = my_conn.cursor()

    sql = "insert into py_tab(name) values ('%s')"
    names = input("请输入要插入的人名:")
    my_cur.execute(sql % names)
    my_conn.commit()
    print(names, '已成功插入')

    my_cur.close()
    my_conn.close()

def upd():
    my_conn = pymysql.connect(host="192.168.92.128",
                              user='sa',
                              passwd='zhouyf',
                              db='cbs')
    my_cur = my_conn.cursor()

    sql = "update python.py_tab set name = '%s' where name = '%s'"
    datas = ('Lily', 'Chuck')
    my_cur.execute(sql % datas)
    my_conn.commit()
    print('成功匹配并修改了', my_cur.rowcount, '条数据')
    my_cur.close()
    my_conn.close()


sel()