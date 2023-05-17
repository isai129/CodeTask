name = " irene "
print(f"首字母大写\t{name.title()}")
print(f"全部大写\t{name.upper()}")
print(f"全部小写\t{name.lower()}")
print(f"清除前面空格\n'{name.lstrip()}'")
print(f"清除后面空格\n'{name.rstrip()}'")
print(f"清除前后空格\n'{name.strip()}'")
print (f" Hello {name.title().strip()}, let`s go to see move!")
message = f"\tHello {name.strip()},\n\tlet`s go to see move!"
print(message)