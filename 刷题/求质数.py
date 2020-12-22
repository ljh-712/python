
def prime():
    '''
    这是一个求三位数中有多少个质数的函数
    '''
    cnt=0
    for i in range(100,999):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            cnt+=1
    print(cnt)

def isPrime(num):
    '''
    判断一个数是否为质数
    '''
    flag = True
    for i in range(2,num):
        if num%i==0:
            flag=False
    if flag:
        print(f'{num}{"是质数"}')
    else:
        print(f'{num}{"不是是质数"}')
isPrime(8)