# napisać funkcję, która policzy ile razy występuje litera a w zdaniu

def count_letter_a_in_sentence(str):
    counter = 0
    for char in str:
        if char == "A" or char == "a":
            counter += 1
    return counter
  