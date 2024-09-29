name = "ada lovelace"
print(name.title()) # 首字母大写
print(name.upper()) # 全部大写
print(name.lower()) # 全部小写

# ff 是 format（设置格式）的简写，因为 Python 通过把花括号内的变量替换为其值来设置字符串的格式。

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello,{full_name.title()}")

# /n:换行符;/t:制表符

message = f"Hello.{full_name.title()}"
print(message)
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# rstrip(),能够找出字符串末尾多余的空白
# lstrip(),能够找出字符串开头多余的空白
# strip() ,能够同时剔除字符串两边的空白
# 在实际程序中，这些剥除函数最常用于在存储用户输入前对其进行清理。
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language)
favorite_language = favorite_language.strip()
print(favorite_language)
