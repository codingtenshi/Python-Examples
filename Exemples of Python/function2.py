# Napisz funkcję, która przyjmuje jakiegokolwiek stringa (muszą być dwa parametry). Zadanie to zwrócić jeden argument

def joinString(str1, str2):
   return f"{str1} {str2}"

###############

name1 = "Karina"
username = "Górnicka"

joinResult = joinString(name1, username)

print(joinString(name1, username))
print(joinResult)
print(joinString('aaa', username))