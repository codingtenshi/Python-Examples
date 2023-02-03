# napisa funkcję, która wypisuje listę od tyłu

def list_read_backwards(elements):
    lenght_counter = len(elements) # policzy elementy w liście (5 pierwszym przypadku, 4 w drugim)
    reverted = [] # powstanie pusta lista, w której umieszczone zostaną odwrócone elementy
    # counter = 0 # 
    for i in elements: # i = pojedynczy element w parametrze sth
        reverted.insert(0,i)
    return reverted # przy pierwszym odpaleniu pętli da 1, przy drugim 2 itd az do 5 a powinna zrobić




list_1 = list_read_backwards([1, 2, 3, 4, 5])
list_2 = list_read_backwards(["Anna", "Iwona", "Natalia", "Zuzanna"])
print(list_1)
print(list_2)