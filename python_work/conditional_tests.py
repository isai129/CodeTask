# 练习 5-1：条件测试
avengers = ['iron man', 'captain america', 'hulk', 'thor', 'black widow', 'Hawkeye']
vip = ' Hulk '
if vip in avengers and vip.lower().strip() != 'hulk':
    print(f'hello {vip.title()},\n welcome to my house!')
else:
    print(f'please,\n\t{vip.upper().strip()},go home!')

abc = 123
