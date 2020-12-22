def my_reverse():
    '''
    输入10个整数，要求按输入时的逆序把这10个数打印出来。逆序输出，
    就是按照输入相反的顺序打印这10个数。
    '''
    s=input().split(' ')
    my_list = list(s)
    my_list.reverse()
    for i in my_list:
        print(i,end=' ')


help(print())