# Reto n°1

""" Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.
Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente. """

# Funtion with a list of random numbers
def ordered_gifs(gifs) :

    """ list_gifs = list(dict.fromkeys(gifs))
    list_gifs.sort() """

    gifs.sort()
    without_duplicates = list(dict.fromkeys(gifs))
    return without_duplicates

    """ print (f"The sorted list without duplicates is {without_duplicates}") """

gifs_1 = ordered_gifs([20, 20, 7, 6, 20, 30, 20, 15, 30, 33])
print(gifs_1)

gifs_2 = ordered_gifs([])
print(gifs_2)











