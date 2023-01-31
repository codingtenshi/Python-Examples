# napisać funkcję, która jako parametr przyjmuje listę liczb i zwraca sumę tych liczb

def sum_of_list_numbers(numbers):
    counter = 0
    for i in numbers:
        counter += i
    return counter
    
        
sum_numbers = sum_of_list_numbers([1,2,3,4])
sum_of_numbers =sum_of_list_numbers([33, 55, 77])
print(sum_of_numbers)
print(sum_numbers)