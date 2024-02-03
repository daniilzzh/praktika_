import csv


def ispravlenie(n, m, xd, yd, t):
    x, y = 0, 0
    if n > 5:
        x = n + xd
    elif n <= 5:
        x = -(n + xd) * 4 + t
    if m > 3:
        y = m + t + yd
    elif m <= 3:
        y = -(n + yd) * m
    return x, y


with open('space.txt', encoding='utf8') as file:
    reader = file.readlines()
    a = list(reader)[1:]


with open('space_new.txt', 'w', encoding='utf8') as file:
    w = csv.writer(file)
    w.writerow(['ShipName', 'planet', 'coord_place', 'direction'])
    for i in range(0, len(a)):
        s = a[i].split('*')
        korabl = s[0]
        n = int(korabl[5])
        m = int(korabl[6])
        planet = s[1]
        t = len(planet)
        koord = s[2]
        x, y = koord.split()
        x = int(x)
        y = int(y)
        vektor = s[3]
        dx, dy = vektor.split()
        dx = int(dx)
        dy = int(dy)
        vektor = str(dx) + ' ' + str(dy)
        if x == 0 and y == 0:
            x, y = ispravlenie(n, m, dx, dy, t)
            koord = f"{x} {y}"
        korabl = s[0]
        w.writerow([korabl, planet, koord, vektor])


