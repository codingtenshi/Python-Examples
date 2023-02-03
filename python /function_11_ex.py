# napisać funkcję, która za parametr przyjmuje listę liczb a zwraca sumę liczb nieparzystych

def sum_of_odd_numbers(numbers):
    counter = 0
    for number in numbers:
        if number % 2 == 1:
            counter += number
    return counter


list_numbers = sum_of_odd_numbers([1, 2, 3, 4, 5, 6, 7])
print(list_numbers)

