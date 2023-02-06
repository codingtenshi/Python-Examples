# write a function that takes a list as a parameter. List can may consist of 
# various elements, but should only count intigers


def get_list_that_sum_only_int(collection):
    result = 0
    for number in collection:
        if type(number) is int:
            result += number
    
    return result







my_list = get_list_that_sum_only_int([5, "dupa", 3])
print(my_list)
