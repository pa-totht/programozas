#A pyton lista

# a listák több elem tárplására szolgálnak egyetlen változóban
# a listákat szögletes zárójellel hozzák létre
# példa

lista= ["alma", "banán", "cseresznye", "alma", "banán"]
print(lista [0])
print(lista[3])
#......................................................................................................
lista= ["alma", "banán", "cseresznye",]
print(len(lista))
hossza= len(lista)
print(hossza)
#.......................................................................................................
# a listaelemek bármilyen tipusúak lehetnek
lista1= ["alma",  "banán", "cseresznye"] #string
lista2= [1, 5, 7, 9, 3] #int
lista3= [True, False, False] #bool

lista1= ["abc", 34, True, 40, "férfi"]
print(lista1)

lista5 = ["alma", "banán", "cseresznye"]
print(type(lista5))

lista = list(("alma", "banán", "csersznye")) #vegye figyelembe a dupla kerek zárójeleket
print(lista)

lista = ["alma",  "banán", "cseresznye"]
print(lista[1])

# irassuk mi a lista utolsó elemét

lista = ["alma",  "banán", "cseresznye"]
print(lista[-1])
print(lista[2])


lista = ["alma-0",  "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print( lista[2:5])
lista = ["alma-0",  "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print( lista[:4])


lista = ["alma-0",  "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print( lista[2:])
uj_lista = lista[2:]
print(uj_lista)
lista_10d_1csop=[]
 lista_10d_1csop=["F,B", "G,M", "H,K", "K,G", "M,M", "O,A", "P,J", "P,P", "S,P", "S,R", "S,M","T,B",  "T,S", "T,T"]
csop1=(lista_10d_1csop)[0:5]
print(csop1)
csop2=(lista_10d_1csop)[5:10]
print(csop2)
csop3= (lista_10d_1csop)[10:]
print(csop3)
#.........................................
lista = ["alma-0",  "banán-1", "cseresznye-2", "narancs-3", "kivi-4", "szőlő-5", "mangó-6"]
print( lista[-4:-2])
#....................................
megbukottak = csop3
print(csop3)




