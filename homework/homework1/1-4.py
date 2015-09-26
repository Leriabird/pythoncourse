data = (input().split(' '))
spisok = [int(i) for i in data]
spisok1 = spisok[0:len(spisok):2]
spisok1.sort()
spisok2 = spisok[1:len(spisok):2]
spisok2.sort(reverse=True)
fin = []
for i in range(len(spisok1)):
    print(spisok1[i], spisok2[i], end = ' ')