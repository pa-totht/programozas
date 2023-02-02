lista=[12, 5, 4, 8, 11, 13, 10, 6]
min=lista[0]
max=lista[0]
for szam in lista:
    if szam <min :
        min=szam
    if szam>max:
        max=szam
print('A legkisebb szám!' ,min)
print('A legnagyobb szám!' ,max)