# napisać funkcję, w której string zaisany zostaje w odwrotnej kolejności, mozna go czytać od tyłu

def str_read_backwards(sentence):
    lenght_counter = len(sentence)
    reverted = ("")
    counter = 1
    for i in sentence:
        reverted += sentence[lenght_counter - counter]
        counter += 1
    return reverted


inscription = str_read_backwards("Hello world")
inscription_2 = str_read_backwards("Chyba mi się udało!!!")
print(inscription)
print(inscription_2)


