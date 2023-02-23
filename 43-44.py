lista1 = [3, 12, 3, 4, 7, 15, 1]
lista2 = [1,3,5,7]
lista3 = [1,55,9,67]


def osszeges_tetele(lista_oszegzes):
    osszesen = 0
    for szam in lista_oszegzes:
            osszesen = osszesen + szam

    print("A listában található összege: ", osszesen)

def eldontes_tetele(lista_eldontes):
    talalat = False
    index = 0
    while index < len(lista_eldontes) and not talalat:
        if lista_eldontes[index] % 3 == 0:
            talalat = True
        index = index + 1

    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')


osszeges_tetele(lista1)
osszeges_tetele(lista2)
osszeges_tetele([10,20,30])
eldontes_tetele(lista3)
