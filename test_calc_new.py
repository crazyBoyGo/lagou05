import pytest

class TestCalc:
    # 加法
    @pytest.mark.run(order=1)
    def test_add1(self, get_calc, get_datas):
        result = get_calc.add(get_datas[0], get_datas[1])
        assert result == get_datas[2]

    # 除法
    @pytest.mark.run(order=4)
    def test_div1(self, get_calc, get_div):
        result = get_calc.div(get_div[0], get_div[1])
        assert result == get_div[2]

    # 减法
    @pytest.mark.run(order=2)
    def test_sub1(self, get_calc, get_sub):
        result = get_calc.sub(get_sub[0], get_sub[1])
        assert result == get_sub[2]

    # 乘法
    @pytest.mark.run(order=3)
    def test_mul1(self, get_calc, get_mul):
        result = get_calc.mul(get_mul[0], get_mul[1])
        assert result == get_mul[2]

