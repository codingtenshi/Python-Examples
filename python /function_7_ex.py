# napisać funkcję, której parametrem jes lista liczb i zwraca sumę liczb nieparzystych
# odd number - liczba nieparzysta

def add_odd_numbers_in_list(numbers):
    counter = 0
    for i in numbers:
        if i %2 == 1:
            counter += i
    return counter


result = add_odd_numbers_in_list([1, 2, 3, 6, 7])
result_2 = add_odd_numbers_in_list([11, 13, 2])
print(result)
print(result_2)