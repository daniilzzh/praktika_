with open('space.txt', encoding='utf8') as file:
    reader = file.readlines()
    a = list(reader)[1:]

kluch = input()
for i in range(0, len(a)):
        s = a[i].split('*')
        korabl = s[0]
        planet = s[1]
        if kluch == planet:
            print(f"{kluch}: {korabl}")
