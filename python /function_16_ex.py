# write a function that takes a list of numbers as a parameter and returns string
# the expected result input[3, 5, 7] output ("357")

def get_list_of_strings_from_list_of_intigers(numbers):
    result = ""
    for number in numbers:
        number = str(number)
        result  += number
        
    return result


my_ex = get_list_of_strings_from_list_of_intigers([3, 5, 7])
print(my_ex)
