# napisać funkcję, która zwraca sumę liczb ze stringa

def return_sum_of_char_in_str(str):
    counter = 0
    for i in str:
        counter += 1
    return counter

sentence = return_sum_of_char_in_str("Bla, bla, bla")
print(sentence)
print(type(sentence))
print(len("Bla, bla, bla"))