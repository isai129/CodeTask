# 导入sys模块
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\npython路径为', sys.path)

print('------------------------------------------')

# 导入 sys 模块的 argv,path 成员
from sys import path  # 导入特定成员
print('================python from import===============')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

