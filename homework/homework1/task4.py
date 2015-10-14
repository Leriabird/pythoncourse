data = (input().split(' '))
lst = [int(i) for i in data]
lst1 = lst[0:len(lst):2]
lst1.sort()
lst2 = spisok[1:len(lst):2]
lst2.sort(reverse=True)
fin = []
for i in range(len(lst1)):
    print(lst1[i], lst2[i], end = ' ')