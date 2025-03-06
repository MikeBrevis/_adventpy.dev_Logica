# Reto n°1

""" Santa Claus 🎅 ha recibido una lista de números mágicos que representan regalos 🎁, pero algunos de ellos están duplicados y deben ser eliminados para evitar confusiones. Además, los regalos deben ser ordenados en orden ascendente antes de entregárselos a los elfos.
Tu tarea es escribir una función que reciba una lista de números enteros (que pueden incluir duplicados) y devuelva una nueva lista sin duplicados, ordenada en orden ascendente. """

# Define funtion, gifts_list, parameter gifts
    #Var with a list, fixed_gifts_list
    
    #For x in range of len of gifts:
        #If position x of gifts is not in fixed_gifts_list
        # add position x of gifts in var fixed_gifts_list

#Return fixed fixed_gifts_list sirted

def gifts_list(gifts):

    fixed_gifts_list = []

    for gift in range(len(gifts)):
        if gifts[gift] not in fixed_gifts_list:
            fixed_gifts_list.append(gifts[gift])

    return sorted(fixed_gifts_list)

gifts_1 = gifts_list ([20, 20, 7, 6, 20, 30, 20])
print (gifts_1)












