import pytest

from test_requests.api.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
    @pytest.mark.parametrize("userid,mobile", [("wangqi", "13800000001"),
                                               ("wangqi2", "13800000002"),
                                               ("wangqi3", "13800000003")])
    def test_add_member(self, userid, mobile):
        name = "王琦"
        department = [1]
        #数据清理
        self.address.delete_member(userid)
        #创建成员
        r = self.address.add_member(userid=userid, name=name, mobile=mobile, department=department)
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "created"
        # 查询成员
        r = self.address.get_member(userid)
        assert r.get("name", "userid 添加失败") == name
