# napisa funkcję, która qypisuje listę od tyłu

def list_read_backwards(sth)-> None:
    for i in sth:
        return sth[::-1]



list_1 = (list_read_backwards([1, 2, 3, 4, 5]))
list_2 = (list_read_backwards(["Anna", "Iwona", "Natalia", "Zuzanna"]))
print(list_1)
print(list_2)