##冒泡排序（从大到小或者从小到大）

def sort_list(the_list, sort_reversed=False):
    for i in range(0, len(the_list)):
        for j in range(i+1, len(the_list)):
            if sort_reversed:
                if the_list[i] < the_list[j]:
                    the_list[i], the_list[j] = the_list[j], the_list[i]
            elif the_list[i] > the_list[j]:
                 the_list[i], the_list[j] = the_list[j], the_list[i]
          
   print(the_list)
   
 if __name__ == '__main__':
     sort_list([3, 2, 4, 8, 1], sort_reversed=True)
