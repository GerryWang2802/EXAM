"""
读取数据库文件
链接数据库
"""
import pymysql, os
from log import log
from common.conf import Conf


def read_db_conf( *sqlfiles):
    """
    读取数据库文件初始化使用的语句
    :param sqlfiles: 要读取的数据库文件
    :return: sqls列表返回读取后的sql语句
    """
    try:
        if not sqlfiles:
            sqlfiles = tuple([i for i in os.listdir('../initsqls/') if i.endswith('.sql')])
            sqls = []
            for sqlfile in sqlfiles:
                file_path = f'../initsqls/{sqlfile}'
                with open(file_path, 'r') as files:
                    for file in files:
                        if file.strip() and not file.startswith('--'):
                            sqls.append(file.strip())
                log().info(f'读取数据库{sqlfile}语句成功')
            return sqls
    except BaseException as e:
        log().error(f'读取数据库执行语句失败{type(e).__name__},错误提示为{e}')
        exit()


class Db:
    def __init__(self):
        args = Conf().args
        try:
            self.con = pymysql.connect(**args)
            log().info('数据库连接成功')
            self.cursor = self.con.cursor()
        except BaseException as e:
            log.error(f'数据库连接失败：{type(e).__name__},错误信息：{e}')
            exit()

    def link_db(self):
        """
        连接数据库
        :return:
        """
        conn, cursor = self.con, self.cursor
        try:
            for sql in read_db_conf():
                cursor.execute(sql)
            conn.commit()
            conn.close()
            log().info(f'sql执行成功')
        except BaseException as e:
            log().error(f'sql执行失败{type(e).__name__},错误码：{e}')
            exit()

    def check_db(self, case_info, args, check_sql, expect_rows):
        """
        数据库落库校验检查
        :param case_info: 要测试的信息
        :param args: 测试内容
        :param check_sql: 检查的sql语句
        :param expect_rows: 受影响的行数
        :return:
        """
        conn, cursor = self.con, self.cursor
        try:
            cursor.execute(check_sql)
            db_actual_rows = cursor.fetchone()[0]
            # print(db_actual_rows)
            if expect_rows ==db_actual_rows:
                log().info('落库检查成功')
                conn.commit()
                conn.close()
            else:
                log().warning(f'落库检查失败，实际影响行数{db_actual_rows},预期影响行数：{expect_rows}')
        except BaseException as e:
                log().error(f'落库检查失败：{type(e).__name__}==测试信息：{case_info}==测试内容：{args},错误信息:{e}')


if __name__ == '__main__':
    a = Db()
    # print(a.read_db_conf())
    a.link_db()
    # a.check_db('rest', 'rukujiancha', 'select * from user',1)