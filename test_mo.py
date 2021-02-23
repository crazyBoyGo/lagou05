import requests


def test_demo():
    # 获取token
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wweb356f4fbc4aa1d1&corpsecret=hd6AQEfbx6KfwQUfVcnSGuwANHptsjBiC5BHVNsNhV8"
    r = requests.get(url)
    token = r.json()["access_token"]
    # 读取成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=liliu2"
    r = requests.get(url)
    # print(r.json())

    # 更新成员信息
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body = {
        "userid": "liliu2",
        "name": "李四"}
    r = requests.post(url, json=body)
    # print(r.json())

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body = {
        "userid": "zhangsan",
        "name": "柯南123",
        "mobile": "+86 13800000000",
        "department": [1]}
    r = requests.post(url, json=body)
    # print(r .json())

    #删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=lilu3"
    r = requests.get(url)
    print(r.json())