# 上海大学 工具开发
======================
## 这是一个pyside2的尝试界面
### 8月12日的需求
=================================

1. 动态增加输入框，这部分有两个思路
    1. 隐藏起来，根据数据 打开；
    2. 真正实现动态增加，目前看来有困难（实现了基本原型）。主要通过动态调用完成。
        1. 自定义组件
            <br> def \_\_init__(self, name):
            <br> def show(self):
            <br> def hide(self):
            <br> def update_button_state(self):