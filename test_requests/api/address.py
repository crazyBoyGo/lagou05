from test_requests.api.base import Base


class Address(Base):
    def add_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?"
        body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        body.update(kwargs)
        return self.send('post', url, json=body)

    def get_member(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send('get', url)

    def update_member(self, userid: str, name: str, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?"
        body = {
            "userid": userid,
            "name": name
        }
        body.update(kwargs)
        return self.send('post', url, json=body)

    def delete_member(self, userid: str):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send('get', url)


