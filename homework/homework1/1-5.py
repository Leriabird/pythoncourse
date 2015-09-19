alpha = 'abcdefghijklmnopqrstuvwxyz'
item = input()

counts = [(char, item.count(char)) for char in alpha if char in set(item)]
for char, count in counts:
    print(char, count)