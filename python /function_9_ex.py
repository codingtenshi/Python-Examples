# napisać funkcję, w której string zaisany zostaje w odwrotnej kolejności, mozna go czytać od tyłu

def str_read_backwards(sentence):
    for i in sentence:
        return sentence[::-1]


inscription = str_read_backwards("Hello world")
inscription_2 = str_read_backwards("Chyba mi się udało!!!")
print(inscription)
print(inscription_2)


