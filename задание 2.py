with open('space.txt', encoding='utf8') as file:
    reader = file.readlines()
    a = list(reader)[1:]

m = []
for i in range(0, len(a)):
    s = a[i].split('*')
    korabl = s[0]
    chislo = korabl[5:8]
    chislo = int(chislo)
    m.append(chislo)
m.sort()

count = 1
for j in range(0, 10):
    for i in range(0, len(a)):
        s = a[i].split('*')
        korabl = s[0]
        chislo = korabl[5:8]
        chislo = int(chislo)
        if chislo == m[j]:
            print(korabl)
            break