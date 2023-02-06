# write a function that takes a string as a parameter and returns a list that contains the words from the string

def get_words_list_from_a_string(sentences):
    special_list = [] # tworzę listę, w której umieszczone zostaną stringi
    word = "" # definiuję stringi
    sentence_size = len(sentences)
    for index, char in enumerate(sentences): # iteruję kazdu znak w ciągu znaków (sentences)
        if char.isspace(): # jeśli i "trafi" na spację(True)
            special_list.append(word) 
            word = ""
        else: 
            word += char 
        if index == sentence_size - 1:
            special_list.append(word) 
    return special_list

                                            

sentence = get_words_list_from_a_string("I believe I can fly")
print(sentence)


