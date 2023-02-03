# napisać funkcję, która zwraca sumę liczb ze stringa

# def return_sum_of_char_in_str(str):
#     counter = 0
#     for i in str:
#         counter += 1
#     return counter

# sentence = return_sum_of_char_in_str("Bla, bla, bla")
# print(sentence)
# print(type(sentence))
# print(len("Bla, bla7git status, bla"))


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
