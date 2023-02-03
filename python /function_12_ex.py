# napisać funkcję, która za parametr przyjmuje listę liczb a zwraca sumę co drugiego elementu z listy
# zaczynając od indeksu 1

def add_every_second_number_from_list(numbers):
    counter = 0
    for index, number in enumerate(numbers):
        if index % 2 == 1:
            counter += number
    
    return counter
list_numbers = add_every_second_number_from_list([1, 2, 3, 4, 5, 6, 7])
list_numbers2 = add_every_second_number_from_list([22, 3, 4, 15])
print(list_numbers)
print(list_numbers2)