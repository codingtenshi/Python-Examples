# napisać funkcję, która przyjmuje jakiegokolwiek stringa ale są te trzy parametry
# zadaniem jest zwrócić te trzy parametry jako jeden argument

def any_string(str1, str2, str3):
    return f"{str1} {str2} {str3}"

str1111 = "Hello"
str2222 = "Karina"
dupa = "Górnicka"

print(any_string(str1111, str1111, "2"))
print(any_string(str1111, str2222, dupa))
