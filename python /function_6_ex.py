# napisać funkcję, która za parametr ma listę liczb a zwraca sumę liczb parzystych
# even number - liczba parzysta

def sum_of_list_even_numbers(numbers):
    counter = 0 
    for i in numbers:
        if i % 2 == 0:
            counter += i
    return counter