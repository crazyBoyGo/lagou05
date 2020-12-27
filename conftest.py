import pytest
import yaml
import os

# 通过 os.path.dirname 获取当前文件所在目录的路径
from pythoncode.calculator import Calculator

yaml_file_path = os.path.dirname(__file__) + "/data.yml"

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)
    print(datas)
    add_datas = datas["datas"]
    add_ids = datas["myids"]
    sub_datas = datas["sub"]
    sub_ids = datas["myids"]
    mul_datas = datas["mul"]
    mul_ids = datas["myids"]
    div_datas = datas["div"]
    div_ids = datas["myids"]


@pytest.fixture(params=add_datas, ids=add_ids)
def get_datas(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=sub_datas,ids=sub_ids)
def get_sub(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(params=mul_datas, ids=mul_ids)
def get_mul(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")


@pytest.fixture(params=div_datas, ids=div_ids)
def get_div(request):
    print("开始计算")
    data = request.param
    print(f"request.param的测试数据是：{data}")
    yield data
    print("结束计算")

@pytest.fixture(scope="session")
def connectDB():
    print("连接数据库操作")
    yield
    print("断开数据库连接")

@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc