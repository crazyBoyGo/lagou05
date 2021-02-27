import requests


class Base:
    def __init__(self):
        # 获取token
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wweb356f4fbc4aa1d1&corpsecret=hd6AQEfbx6KfwQUfVcnSGuwANHptsjBiC5BHVNsNhV8"
        r = requests.get(url).json()
        self.token = r["access_token"]
        self.request_session = requests.Session()
        self.request_session.params = {'access_token': self.token}

    def send(self, *args, **kwargs):
        r = self.request_session.request(*args, **kwargs)
        return r.json()
