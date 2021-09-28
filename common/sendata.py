"""
测试用例参数化，传参执行测试用例
"""
import requests
from log import log

def send_request(method,url,args):
    """
    请求接口返回响应结果
    :param method: 请求方法
    :param url: 请求接口地址
    :param args: 请求body上传参数
    :return: 返回响应结果，响应格式
    """
    try:
        request_url =f'requests.{method}("http://{url}",{args})'
        res = eval(request_url)
        # print(res.headers['Content-Type'])
        if 'text' in res.headers['Content-Type']:
            # print(f'输出text格式为：{res.text}')
            res_type = 'text'
            actual = res.text
            log().info(f'输出text格式为：{res.text}，成功将{args}参数信息提交给接口')
        elif 'json' in res.headers['Content-Type']:
            res_type = 'json'
            actual = res.json()
            # print(f'输出json格式为：{res.json()}')
            log().info(f'输出json格式为：{res.json()}，成功将{args}参数信息提交给接口')
            return res_type,actual
        else:
            log().info(f'输出格式为：{res.json()}')
    except BaseException as e:
        log().error(f'提交失败：{type(e).__name__},失败信息：{e}')

def check_result(case_info,res_type,actual,expect):
    """
    对比实际返回响应结果和预期结果
    :param case_info: 测试信息
    :param res_type: 请求响应返回的格式
    :param actual: 请求实际返回的内容
    :param expect: 预期返回的内容
    :return: 返回passed布尔类型
    """
    try:
        passed = False
        if res_type =='text':
            if actual in expect:
                passed = True
        elif res_type =='json':
            if actual in expect:
                passed = True
        else:
            pass
        if passed ==True:
            msg = ''
            log().info(f'{case_info}响应结果通过')
        else:
            log().info(f'{case_info}响应结果对比失败==不通过')
            msg = '结果检查失败'
    except BaseException as e:
        log().info(f'响应结果错误：{type(e).__name__},错误信息：{e}')
    return msg,passed


if __name__=='__main__':
    # send_request('post','192.168.238.129/exam/signup/',"{'username': 'admin02', 'password': '123456','confirm':'123456','name':'管理员02'}")
    check_result('测试01','json','w','r')
