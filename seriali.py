#encoding: utf-8

import os
from nester import *

os.chdir('C:\\Users\\name\\Desktop\\python')
man = []
other = []
try:
    """对文件进行分离处理"""
    data = open("sketch.txt")
    for each_line in data:
        try:
            """
            将文件以冒号分为:冒号前，冒号后  。
            根据冒号前的关键字进行匹配，将文件内容分离存入两个列表中
            """
            (role, line_spoken) = each_line.split(":", 1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    """列表的内容写入文件，并且调用print_lol方法格式化列表输出到文件"""
    with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
        print_lol(man, fn=man_file)
        print_lol(other, fn=other_file)
except IOError:
    print('File error')
    
"""
print("man: ", man)
print("other: ", other)
"""

"""
cat sketch.txt

Man: You did not!
Other Man: Oh I`m sorry, is this a five minute, or the full half our?
Man: Ah! Just the five minutes.
Other Man: Anyway, Idid.
Man: You most certainly did not!
"""
