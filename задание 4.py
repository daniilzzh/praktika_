import random
import string

# “KРWЯ-282, Лотлориэн, 11 69,-5 -2” → “ KРWЯ-282;Лотлориэн;30 -51;-2 8, ИЭНWPТОЛ ”
def create_password(korabl, planet):
    tri_posled = korabl[1:4]
    centerb1 = korabl[5:7]
    centrb2 = korabl[6:8]
    tri_planeta1 = planet[0:3]
    tri_planeta1 = tri_planeta1[::-1]
    flag = False
    while flag != True:
        charachters = string.ascii_letters + string.digits
        password = ' '.join(random.choice(charachters))
        if tri_posled in password and centerb1 in password and tri_planeta1 in password:
            flag = True
    return password



with open('space.txt', encoding='utf8') as file:
    reader = file.readlines()
    a = list(reader)[1:]

for i in range(0, 3):
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
    password = create_password(korabl, planet)
    print(password)
