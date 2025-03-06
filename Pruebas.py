""" x = range (6)
for n in x:
    print(n) """

""" numbers = [20, 20, 7, 6, 20, 30, 20]
numbers_2 = []

for number in range(len(numbers)): # Position range
    if numbers[number] not in numbers_2:
        numbers_2.append(numbers[number])

numbers_2.sort()
print (numbers_2)
regalo
numbers = [20, 20, 7, 6, 20, 30, 20]
numbers_2 = [] """

def gifts_list(gifts):

    fixed_gifts_list = []

    for gift in range(len(gifts)):
        if gifts[gift] not in fixed_gifts_list:
            fixed_gifts_list.append(gifts[gift])

    return sorted(fixed_gifts_list)

gifts_1 = gifts_list ([20, 20, 7, 6, 20, 30, 20])
print (gifts_1)














