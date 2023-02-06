# write a function that returnes quantity of vowels in sentence
     
    
def quanity_of_vowels(sentence):
    vovels = ["a", "e", "i", "o", "u"]
    counter = 0
    for char in sentence:
        if char in vovels:
            counter += 1
    return counter


my_ex = quanity_of_vowels("What is going on?")
my_ex2 = quanity_of_vowels("hahcbjiuhqiiweeahnwuoq")
print(my_ex)
print(my_ex2)



