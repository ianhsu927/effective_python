# 最好阅读一遍 PEP8
# https://www.python.org/dev/peps/pep-0008/

"""
    about blank
    1. use space instead of tab
    2. use 4 spaces instead of 2 spaces
    3. less than 79 characters per line
    4. 多行表达式, 除首行外, 其余行缩进 4 个空格
    5. 同一个文件, function 和 class 之间用两个空行隔开
    6. 同一个 class 中, function 之间用一个空行隔开
    7. in dictionary, key: value
    8. 变量赋值, 赋值符号两边各一个空格
    9. in annotation, variable: type
    
    about name
    1. 函数、变量、属性用小写字母和下划线
    2. _protected
    3. __private
    4. class 用驼峰命名法, ClassName
    5. 模块级别变量, 全大写, MY_VAR
    6. 类的实例方法, 第一个参数用 self
    7. 类方法第一个参数用 cls
    
    about expression
    1. 行内否定, if a is not b 而不是 if not a is b
    2. 不要用 if len(somelist) == 0, 而是 if not somelist
    3. 同理, if somelist 而不是 if len(somelist) != 0
    4. 不要把复合语句挤在一行
    5. 表达式一行写不下, 用括号括起来, 拆成多行
    7. 多行表达式用括号括起来, 拆成多行, 括号内的行尾不用加 '\'
    
    about import
    1. import 语句放在文件开头
    2. import module 时, 不要用相对路径, 用绝对路径
    3. 一定要是用相对路径时使用 from . import module
    4. import 语句分成三组,
        1. 标准库
        2. 第三方库
        3. 自定义库
"""