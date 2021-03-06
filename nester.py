#encoding: utf-8
import sys
"""
这是名为print_lol模块，作用是打印列表，其中有可能包含嵌套列表
"""

def print_lol(the_list, indent=False, level=0, fn=sys.stdout):
    """
    这个函数取一个位置参数，名为the_list，这个可以是任何一个参数列表（也可以是包含嵌套的参数列表）
    所指定的列表中的每个数据项（递归地）输出到屏幕上，各数据项各占一个行
    第二个参数（level）用来在遇到嵌套列表时，插入制表符
    """
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fn)
        else:
            if indent:
                for tab_srop in range(level):
                    print("\t", end='', file=fn)
        print(each_item, file=fn)
