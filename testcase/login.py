import pytest
from common.conf import Conf
from common.casedata import read_cases
from common.db import Db
from common.sendata import send_request,check_result
# from common.log import log

@pytest.fixture(autouse=True)
def get_url():
    global url_host
    a = Conf()
    url_host = a.host

@pytest.fixture()
def init():
    a = Db()
    a.link_db('../initsqls/login.sql')

cases = read_cases('../excelcase/login.xlsx','arg_', 4)
@pytest.mark.parametrize('case_id,case_name,api_path,method,args,expect', cases)
def test_login(case_id,case_name,api_path,method,args,expect):
    print(f'测试编号：{case_id}==测试名称：{case_name}==请求地址：{api_path}==请求方法：{method}==检查数据：{args}==期望结果：{expect}')
    case_info=f'{case_id}:{case_name}'
    test_login.__doc__=case_info
    url=url_host + api_path
    print(f'请求的地址：{url}')
    res_type, actual=send_request(method, url, args)
    res,msg=check_result(case_info, res_type, actual, expect)
    assert res, msg

if __name__=='__main__':
    pytest.main(['-v','--tb=short','--html=../report/login.html','login.py'])