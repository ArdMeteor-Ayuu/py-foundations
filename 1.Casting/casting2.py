lst = [1, 2, 3, 3]
t = tuple(lst)
s = set(lst)
lst2 = list(s)
print(type(t))
name = "Ayuu"
chars = list(name)
print(type(chars))
print(type(lst2))
print(type(s))
# list(10)  # TypeError 
# tuple(5.5)  # TypeError
# set(True)  # TypeError