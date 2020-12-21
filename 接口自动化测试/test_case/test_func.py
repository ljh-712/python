import pytest

# #封装函数
# def test_001():
#     # 断言
#     assert 1 + 2 == 3
# def test_002():
#     # 断言
#     assert 1 + 2 == 0
#
# #封装类
# class Test_login:
#     def test_003(self):
#         assert 1+2==4
## 数据驱动
@pytest.mark.parametrize('inData',[10,20])
def test_001(inData):
    # 断言
    assert inData == 3
if __name__ == '__main__':
    pytest.main(['test_func.py','--html=../report/xt.html'])
