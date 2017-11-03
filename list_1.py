#列表中的递归迭代

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(movies)

movies = ["肖申克的救赎",  1994 ,  "弗兰克·德拉邦特", 142, ["蒂姆·罗宾斯", ["摩根·弗里曼", "鲍勃·冈顿", "威廉姆·赛德勒" , "克兰西·布朗 & 吉尔·贝罗斯"]]]


##列表和列表b  b=a=[] 这样的a、b是指向一个值
##要指向不同的值的方法：1、copy
##                    2、list
##                    3、分片[:]

## number <= 256 时：  number1 = 1, number2 = 1 , number1 is number2 == True
## number > 256 时:   number1= 278, number2 = 278, number1 is number2 == False
