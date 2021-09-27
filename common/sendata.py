"""
测试用例参数化，传参执行测试用例
"""
import requests

def send_request():
    # try:
        # request_url =f'requests.{method}'
    request_url = requests.post('http://192.168.1.5/exam/signup/',{'username': 'admin', 'password': '123456','confirm':'123456','name':'管理员'})
    print(request_url)
if __name__=='__main__':
    send_request()