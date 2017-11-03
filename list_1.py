def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
            
print_lol(movies)

movies = ["肖申克的救赎",  1994 ,  "弗兰克·德拉邦特", 142, ["蒂姆·罗宾斯", ["摩根·弗里曼", "鲍勃·冈顿", "威廉姆·赛德勒" , "克兰西·布朗 & 吉尔·贝罗斯"]]]
