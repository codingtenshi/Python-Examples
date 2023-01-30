# f, która zwraca True jeśli string zaczyna się lit a
# f, która dubluje cyfrę (jak dam np 4 to da 8)
# f, która mi mówi, która jest godzina

def string_starts_with_a(word):
    if word.startswith("a") or word.startswith("A"):
        return True
    else:
        return False


print(string_starts_with_a("mama"))
print(string_starts_with_a("apple"))
print(string_starts_with_a("Anna"))


def double_number(a): 
    return a * 2


print(double_number(2))
print(double_number(8))
print(double_number(33))

# import datetime
from datetime import datetime


def what_time_is_it():
    return datetime.now()

print(what_time_is_it())




