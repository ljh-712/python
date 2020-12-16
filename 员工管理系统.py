# 显示系统欢迎信息
print('-' * 20, '欢迎使用员工管理系统', '-' * 20)
# 创建列表保存员工
emps=['\t悟空\t男\t\t28\t\t花果山',]
while True:
    # 显示用户选项
    print('请选择所要做的操作')
    print('\t1、显示员工列表')
    print('\t2、添加员工列表')
    print('\t3、删除员工列表')
    print('\t4、退出系统')
    user_choose = input('请选择[1-4]:')
    print('-' * 62)
    # 根据用户选择做操作
    if user_choose == '1':
        # 打印表头
        print('序号\t姓名\t性别\t年龄\t住址')
        n =1
        #显示员工信息
        for e in emps:
            print(f'{n}\t{e}')
            n+=1
    elif user_choose == '2':

        print('\t请输入员工姓名：')
        name = input()
        print('\t请输入员工性别：')
        sex = input('\t')
        print('\t请输入员工年龄：')
        age = input()
        print('\t请输入员工住址：')
        address = input()
        emp=f'\t{name}\t{sex}\t\t{age}\t\t{address}'
        print('确定添加该员工吗？,请输入y或n')
        check = input()

        if check=='y':
            emps.append(emp)
            print('添加成功')
        else:
            print('已取消')

    elif user_choose == '3':
        del_num=int(input('请输入要删除的员工的序号：'))
        if del_num<0 | del_num>len(emps) :
            print('输入不合法')
        else:
            i=del_num-1
            emps.pop(i)
    elif user_choose == '4':
        print("已退出")
        break
    else:
        print('输入有误，重新输入')
    print('-'*62)