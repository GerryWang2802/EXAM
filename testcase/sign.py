import pytest
from common.conf import Conf
from common.db import read_db_conf

@pytest.fixture(autouse=True)
def get_url():
    global host_url
    a = Conf()
    url_host = a.host


@pytest.fixture()
def init():
    """
    读取注册sql文件
    :return:
    """
    read_db_conf('../initsql/signup.sql')

cases = []
@pytest.mark.parametrize('a,b,expect',cases)
def test_sign():
    pass

if __name__=='__main__':
    pytest.main(['-v','--tb=short','--html=signup.html','sign.py'])