#coding：utf8
import os
"""
原文件：
2:22,3.01,3.01,3.02,3.02,3.02,3.22,2.49,2:38
2.34,3:21,2.34,2.45,3.01,2:01,2:01,3:10,2-22
2:58,2.58,2:39,2-25,2-55,2:54,2.18,2:55,2:55
2.59,2.11,2:11,2:23,3-10,2-23,3:10,3.21,3-21

先从各个文件将数据读入各自的列表。编写一个小程序，
处理每个文件，为每个选手的数据创建一个列表，并在屏幕上显示这些列表
"""
os.chdir('C:\\Users\\wangxue2\\Desktop\\python思维导图')
"""
def unique_list(unique_l):

    列表去重，可用set解释器
    :return:

    unique_li = []
    for each_t  in unique_l:
        if each_t not in unique_li:
            unique_li.append(each_t)
    return unique_li
"""
def clean_file(some_string):
    """
    清晰数据函数，列表内容都以.的形式显示
    :param some_string:
    :return:
    """
    if '-' in some_string:
        splitter = '-'
    elif ':' in some_string:
        splitter = ':'
    else:
        return some_string
    (pre, later) = some_string.split(splitter)
    return(pre + '.' + later)

def list_file(the_file):
    """
    文件内容读入列表
    """
    the_list = []
    sec_list = []
    try:
        with open(the_file) as f1:
            """
            文件内容读入列表，去除特殊符号，升序排序,去重，列表推导
            """
            file = f1.readline()
            the_list = file.strip().split(',')
            sec_list = [sorted(set(clean_file(each_t) for each_t in the_list))]
            return sec_list
            """
            for each_t in the_list:
                sec_list.append(clean_file(each_t))
            """
            """
            return unique_list(sorted(sec_list))
            return set(sorted(sec_list))
            """
    except IOError as e:
        print('File error：' + str(e))
        return None

print('man1: ', list_file('data1.txt'))
print('man2: ', list_file('data2.txt'))
print('man3: ', list_file('data3.txt'))
print('man4: ', list_file('data4.txt'))
