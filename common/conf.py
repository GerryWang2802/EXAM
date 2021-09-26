import configparser
from log import log

class Conf:
    def __init__(self):
        self.read_entry()
        # self.read_db()
        pass
    def read_entry(self):
        """
        读取数据库名称和服务器名称
        :return:
        """
        try:
            conf = configparser.ConfigParser()
            conf.read('../conf/entry.ini')
            self.__which_db = conf.get('entry','which_db')
            self.__which_server = conf.get('entry','which_server')
            # print(self.__which_server,self.__which_db)
            # return self.__which_db,self.__which_server
            log().info(f'读取数据库信息成功,数据库名称：{self.__which_db}==服务器名称：{self.__which_server}')
        except BaseException as e:
            log().error(f'读数据库名称和服务器名称配置文件../conf/entry.ini出错==错误类型：{type(e).__name__}，错误内容：{e}')
            exit()

    def read_db(self):
        """
        初始化读取数据库配置信息
        :return: 字典格式连接数据库配置数据
        """
        try:
            conf = configparser.ConfigParser()
            conf.read('../conf/db.conf')
            host = conf.get(self.__which_db,'host')
            uname = conf.get(self.__which_db,'uname')
            password = conf.get(self.__which_db,'password')
            db = conf.get(self.__which_db,'db')
            self.args = {'host': host, 'uname': uname, 'password': password, 'db': db}
            log().info(f'数据库配置文件读取成功,数据库地址:{host}==数据库名称:{uname}==数据库表名称:{db}')
        except BaseException as e:
            log().error(f'读数据库入口配置文件../conf/db.conf出错==错误类型：{type(e).__name__}，错误内容：{e}')
            exit()

    def read_server(self):
        """
        读取服务器配置信息
        :return:
        """
        try:
            conf = configparser.ConfigParser()
            conf.read('../conf/server.conf')
            self.ip = conf.get(self.__which_server,'ip')
            self.port = conf.get(self.__which_server,'port')
            self.host = 'http://%s:%s:'%(self.ip,self.port)
            log().info(f'读取读取服务器配置信息成功,服务器地址:{self.host}')
        except BaseException as e:
            log().error(f'读取服务器配置信息../conf/server.conf出错==错误类型：{type(e).__name__},错误内容：{e}')
            exit()

    def update_entry(self):
        update_sure = input('修改连接的服务器名称和数据库名称(请按y/Y表示确认修改，其他则无效)')
        if update_sure in ('y','Y'):
            new_db_name = input('请输入新的要连接的数据库名称：')
            new_server_name = input('请输入新的要连接的服务器名称：')
            if (new_db_name,new_server_name) in ('debug','smoke','formal'):
                conf = configparser.ConfigParser()
                conf.read('../conf/entry.ini')
                conf.set()


if __name__=='__main__':
    a = Conf()
    # print(a.read_entry())
    a.read_db()
    # print(a.read_server())
    a.read_server()