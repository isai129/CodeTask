 

1. 将圆括号中的内容打印到屏幕
```bash
print("Hello Python World!")
```

#变量名命名规则:
	1.变量名只能包含字母、数字和下划线,
	2.能以字母或下划线打头，但不能以数字打头
	3.变量名不能包含空格
	4.不要将 Python 关键字和函数名用作变量名
	5.变量名应既简短又具有描述性
	6.慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0。
	7.应使用小写的 Python 变量名
		`Python没有内置的常量类型,通常使用小写字母和下划线表示变量,全大写来表示常量
		变量是可以赋给值的标签，也可以说变量指向特定的值。

2.操纵字符串

```bash
name = 'irene'
print(f"首字母大写\t{name.title()}") # 首字母大写
print(f"全部大写\t{name.upper()}")  # 全部大写
print(f"全部小写\t{name.lower()}")  # 全部小写
print(f"清除前面空格\n'{name.lstrip()}'") # 清除前面空格
print(f"清除后面空格\n'{name.rstrip()}'") # 清除后面空格
print(f"清除前后空格\n'{name.strip()}'")  # 清除前后空格
# f字符串,f 是 format（设置格式）的简写，通过把花括号内的变量替换为其值来设置字符串的格式
#将消息 
message = f"\tHello {name.strip()},\n\tlet`s go to see move!"
print(message)
#在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组织输
#出，让用户阅读起来更容易。
# /n:换行符;/t:制表符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

```

3.组织列表
```bash
avengers = ['iron man','captain america','hulk','thor','black widow','hawkeye']

print(f"1.{avengers[0]}")
print(f"2.{avengers[1]}")
print(f"3.{avengers[2]}")
print(f"4.{avengers[3]}")
print(f"5.{avengers[4]}")
print(f"6.{avengers[-1]}"

# 大多数列表将是动态的，这意味着列表创建后，将随着程序的运行增删元素

avengers[5] = 'jarvis'
print(avengers)

# insert()可在列表的任何位置添加新元素

avengers.insert(0,'nick fury')
print(avengers)

# 使用 del 语句删除元素，条件是知道其索引

del avengers[0]
print(avengers)

# 使用方法 pop()删除末尾的元素,让你能够接着使用它。
# 术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。

poped_avengers = avengers.pop()  # 从avengers中弹出'vision'并赋值给变量poped_avengers.
print(avengers)
print(poped_avengers)


# 弹出列表中任何位置处的元素,只需在圆括号中指定要删除元素的索引

first_avengers = avengers.pop(0)
print(f"the first avengers is :{first_avengers.title()}")

# 如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用 del 语句；
# 如果你要在删除元素后还能继续使用它，就使用方法 pop()。
# 如果只知道要删除的元素的值，可使用方法 remove()

print(avengers)
avengers.remove('hawkeys')
print(avengers)

to_old = 'thor'
avengers.remove(to_old)
print(f"\n{to_old.title()} is too old.")

# 方法 remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都删除。
print(avengers)



```