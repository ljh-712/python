n = input()
s = input().split(' ')
num=input()
my_list = list(s)
cnt = my_list.count(num)
for i in range(cnt):
    my_list.remove(num)
for i in my_list:
    print(i,end=' ')