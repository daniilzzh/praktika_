with open('space.txt', encoding='utf8') as file:
    reader = file.readlines()
    a = list(reader)[1:]

slovo = input()
while slovo != 'stop':
    slovo = str(slovo)
    flag = False
    for i in range(0, len(a)):
        s = a[i].split('*')
        planet = s[1]
        korabl = s[0]
        direction = s[3]
        if slovo == korabl:
            print(f"Корабль {korabl} был отправлен с планеты: {planet} и его направление движения было: {direction}")
            flag = True
    if flag == False:
        print('error.. er.. ror..')
    slovo = input()