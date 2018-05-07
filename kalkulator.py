input = input()
tablica = []

# pierwszy komenatarz
for i in range(0, int(input)):
    if i == 0:
        tablica.append(0)
    else:
        if i < 3:
            tablica.append(1)
        else:
            tablica.append(tablica[i-2] + tablica[i-1])

# program pesel
pesel = input()

wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
my_sum = 0

for i in range(0, len(wagi)):
    my_sum += int(pesel[i]) * wagi[i]

result = 10 - (my_sum % 10)
if int(pesel[10]) == result:
    print(1)
else:
    print(0)


print(tablica)