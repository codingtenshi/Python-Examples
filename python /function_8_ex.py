# napisać funkcję, która zwraca informację ile liczb łącznie znajduje się w stringu

def return_sum_of_int_in_char(sentence):
    counter = 0
    for i in sentence:
        if i.isnumeric(): 
            counter += 1
    return counter



