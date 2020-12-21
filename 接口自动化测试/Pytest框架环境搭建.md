# Pytest框架
## 框架搭建
### 框架简介：
> Pytest框架是Python的第三方单元测试框架，比自带的unittest更简洁高效，支持
>315种以上的插件，同时兼容unitest框架
###环境搭建：
首先使用pip安装pytest
```
pip install pytest
pip install pytest-html  原生态报告模板
```
##Pytest执行测试用例
### 执行测试用例遵循的规则:

- .py测试文件必须以test_开头或以_test结尾
- 测试类必须以Test开头，并且不能有init方法
- 测试方法必须以test_开头
- 断言必须使用assert

```python
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
    pytest.main(['test_func.py','--html=../report/xt.html'])# '--html=../report/xt.html'生成html报告a
```

### 注意
- 1、环境初始化与数据清除
- 2、定制化执行用例

