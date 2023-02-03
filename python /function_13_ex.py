# napisać funkcję, która za parametr przyjmuje stringa a zwraca listę, w której przechowane są wszystkie litery ze stringa

def get_list_from_string(sentence):
    converted = []
    for i in sentence:
        converted.append(i)
       
    return converted


sentence = get_list_from_string("Let it succeed")
print(sentence)
