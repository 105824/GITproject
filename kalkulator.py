input = input()
tablica = []


for i in range(0, int(input)):
    if i == 0:
        tablica.append(0)
    else:
        if i < 3:
            tablica.append(1)
        else:
            tablica.append(tablica[i-2] + tablica[i-1])


print(tablica)