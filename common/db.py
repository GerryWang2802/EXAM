"""
读取数据库文件
链接数据库
"""
import pymysql,os
from log import log

class Db:
    def __init__(self):
        pass
    def read_db_conf(self,*sqlfiles):
        """
        读取数据库文件初始化使用的语句
        :param sqlfiles: 要读取的数据库文件
        :return: sqls列表返回读取后的sql语句
        """
        try:
            if not sqlfiles:
                sqlfiles = tuple([i for i in os.listdir('../initsqls/') if i.endswith('.sql')])
                # print(sqlfiles)
                sqls =[]
                for sqlfile in sqlfiles:
                    file_path = f'../initsqls/{sqlfile}'
                    with open(file_path,'r') as files:
                        for file in files:
                            if file.strip() and not file.startswith('--'):
                                sqls.append(file.strip())
                log().info(f'读取数据库{sqlfile}语句成功')
                return sqls
        except BaseException as e:
            log().error(f'读取数据库执行语句失败{type.__name__},错误提示为{e}')
            exit()
    def link_db(self):
        """
        连接数据库
        :return:
        """


if __name__=='__main__':
    a = Db()
    print(a.read_db_conf())