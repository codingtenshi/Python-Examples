# Napisać funkcję, która przyjmuje dwa parametry, muszą to być liczby. Ma zwrócić sumę tych liczb.

def sum_of_numb(a: int, b: int):
   if not isinstance(a, int) and not isinstance(b, int): 
    return print("Both parameters sholud be int")
   if not isinstance(a, int):
    return print("First parameter sholud be int")
   if not isinstance(b, int):
    return print("Second parameter sholud be int")

   return (a + b) 


print(sum_of_numb(5, 10))
print(sum_of_numb(9,4))
print(sum_of_numb(4,8))
print(sum_of_numb("4", "8"))
print(sum_of_numb(["4"], "8"))
print(sum_of_numb(4, "8"))
print(sum_of_numb("4", 8))