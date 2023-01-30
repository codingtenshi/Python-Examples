# f, która zwraca True jeśli string zaczyna się lit a

def string_starts_with_a(word):
    if word.startswith("a") or word.startswith("A"):
        return True
    else:
        return False


print(string_starts_with_a("mama"))
print(string_starts_with_a("apple"))
print(string_starts_with_a("Anna"))