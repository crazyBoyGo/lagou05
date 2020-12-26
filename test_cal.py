import pytest
import yaml
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()
        print("\nsetup_class:所有计算开始")
    def setup_method(self):
        print("\nsetup_method:计算开始")
    def teardown_method(self):
        print("\nteardown_method:计算结束")
    def teardown_class(self):
        print("\nteardown_class:所有计算结束")

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["datas"])
    # 测试add函数
    def test_add(self,a,b,expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a,b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["sub"])
    def test_sub(self, a, b, expect):
        result1 = self.calc.sub(a, b)
        assert result1 == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["mul"])
    def test_mul(self, a, b, expect):
        result2 = self.calc.mul(a, b)
        assert result2 == expect

    @pytest.mark.parametrize("a,b,expect", yaml.safe_load(open("./data.yml"))["div"])
    def test_div(self, a, b, expect):
        result3 = self.calc.div(a, b)
        assert result3 == expect