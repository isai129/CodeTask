# 4.1 遍历整个列表
# for循环
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    # 使用单数和复数式名称，可帮助你判断代码段处理的是单个列表元素还是整个列表
    print(f'{magician.title()}, that was a great trick!')
    print(f"I can`t wait to see your next trick,{magician.title()}.\n")
print("Thank you, everyone. That Was a great magic show!")

# 4.2 test

animals = ['dog', 'cat', 'tiger', 'pig']
for animal in animals:
    print(animal.title())
    print(f'i like {animal.title()}.\n')
    print(f" \t That`s a {animal.title()}")
print("That`s all")




