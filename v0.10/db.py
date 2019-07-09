import os

import pymysql
from pymysql.cursors import DictCursor

DB_CONF = {
    'host': os.getenv('MYSQL_HOST'),
    'port': int(os.getenv('MYSQL_PORT')),
    'db': os.getenv('MYSQL_DB'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PWD'),
    'charset': 'utf8',
    'autocommit': True
}


class DB(object):
    def __init__(self):
        # print("建立数据库连接")
        self.conn = pymysql.connect(**DB_CONF)
        self.cur = self.conn.cursor(DictCursor)  # 建立游标

    def execute(self, sql):
        # print(f"执行sql: {sql}")
        self.cur.execute(sql)
        result = self.cur.fetchall()
        # print(f"执行结果: {result}")
        return result

    def execute_file(self, file_path):
        with open(file_path) as f:
            sqls = f.readlines()

        return [self.execute(sql) for sql in sqls]

    def close(self):
        # print("关闭数据库连接")
        self.conn.close()


class LongTengServer(DB):
    """该项目数据库的常用业务操作封装"""
    def check_data_source_id(self, data_source_id):
        sql = f'SELECT dataSourceId FROM datasource WHERE dataSourceId="{data_source_id}"'
        result = self.execute(sql)
        return True if result else False

    def del_card_if_exist(self, card_number):
        if self.check_card(card_number):
            sql = f'DELETE FROM cardinfo WHERE cardNumber="{card_number}"'
            self.execute(sql)
            return True
        return False

    def check_card(self, card_number):
        sql = f'SELECT cardNumber FROM cardinfo WHERE cardNumber="{card_number}"'
        result = self.execute(sql)
        return True if result else False  # 如果result为真(非()),返回True, 否则返回False

    def add_card_if_not_exist(self, card_number):
        if not self.check_card(card_number):
            sql = f'INSERT INTO cardinfo (`cardNumber`) VALUES ("{card_number}")'
            self.execute(sql)
            return True
        return False

    def reset_card(self, card_number):
        if self.check_card(card_number):
            sql = f'UPDATE cardinfo SET cardstatus=0, userId=null WHERE cardNumber="{card_number}";'
            self.execute(sql)
            return True
        return self.add_card_if_not_exist(card_number)

    def bind_card(self, card_number, user_name):
        self.add_card_if_not_exist(card_number)
        sql = f'UPDATE cardinfo SET cardstatus=5010, userId=(SELECT userId FROM carduser WHERE userName="{user_name}" LIMIT 1) WHERE cardNumber="{card_number}";'
        self.execute(sql)
        return True

    def reset_user(self, user_name):  # todo check_user
        sql = f'UPDATE cardinfo SET cardstatus=0, userId=null WHERE userId in (SELECT userId FROM carduser WHERE userName="{user_name}");'
        self.execute(sql)
        return True

    def get_balance(self, card_number):
        sql = f'select cardBalance from cardinfo where cardNumber="{card_number}" '
        result, = self.execute(sql) or [{}]
        balance = result.get('cardBalance', None)
        return balance

    def get_recharge_details(self, card_number):
        sql = f'SELECT cardBalance, createTime FROM rechargedetails WHERE cardNumber="{card_number}" ORDER BY createTime DESC;'
        result = self.execute(sql)
        if not result:
            return []

        return [f"充值金额:{line['cardBalance']},时间:{line['createTime']}" for line in result]

    def get_consume_details(self, card_number):
        sql = f'SELECT cardBalance, createTime FROM consumptiondetails WHERE cardNumber="{card_number}" ORDER BY createTime DESC;'
        result = self.execute(sql)
        if not result:
            return []
        return [f"消费金额:{line['cardBalance']},时间:{line['createTime']}" for line in result]

    def get_user_id(self, user_name):
        sql = f'SELECT userId FROM carduser WHERE userName="{user_name}"'
        result, = self.execute(sql) or [{}]
        user_id = result.get('userId', None)
        return user_id


# 模块私有代码
if __name__ == '__main__':  # 一般用来调试当前模块, 只有从当前模块运行时才执行
    # db = DB()
    # # r = db.execute('select cardNumber from cardInfo where cardNumber="123456abc"')
    # # print(r)
    #
    # db.close()
    db = LongTengServer()
    with open('../data/setup.sql') as f:
        sqls = f.readlines()
    for sql in sqls:
        print(db.execute(sql))
    db.close()
