import pymysql
from pymysql.cursors import DictCursor

def main():
    con = pymysql.connect(host='localhost', port=3306, database='hrs', charset='utf8', user='yannan786', password='muwei626934', autocommit=True)
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t\t')
                print(dept['loc'])
    finally:
        con.close()

if __name__ == '__main__':
    main()