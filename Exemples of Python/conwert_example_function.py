# Napisz funkcję, która zwraca stringa: "Cześć Łukasz, widzę, ze masz 30 lat". Pierwszy parametr to string, drugi to intiger.
# Wynikiem ma być string.


def sentence(str1, int):
    return f"Cześć {str1}, widzę, ze masz {int} lat"

name = "Łukasz"
age = 30

name2 = "Igor"
age2 = 21


print(sentence(name, age))
print(sentence(name2, age2))

