# write a function that takes a list of numbers as a parameter and returns string 
# separated by comas
# the expected result input[3, 5, 7] output ("3", "5", "7")

def converted_list_to_a_string(collections):
    result = ""
    str_ex = len(collections)
    for index,number in enumerate(collections):
            result += str(number)
            if index == str_ex - 1:
                return result
            result += ","            

my_ex = converted_list_to_a_string([3, 5, 7])
print(my_ex)
print(type(my_ex))