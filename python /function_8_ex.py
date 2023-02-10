# napisać funkcję, która zwraca informację ile liczb łącznie znajduje się w stringu

def return_sum_of_int_in_char(sentence):
    counter = 0
    for i in sentence:
        if i.isnumeric(): 
            counter += 1
    return counter


sentence = return_sum_of_int_in_char(("Bl5a, bla7git status, bla"))
sentence2 = return_sum_of_int_in_char("223hga552")
print(sentence2)
print(sentence)
