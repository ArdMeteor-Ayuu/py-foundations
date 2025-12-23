t = (10, 20, 30)

x = (5)
y = (5,)
x → int
y → tuple

a = 10, 20, 30     # packing
x, y, z = a        # unpacking

t = (1, 2, [3,4])
t[2].append(5)
print(t)

t1 = (1,2)
t2 = (3,4)
print(t1 + t2)    # (1,2,3,4)
print(t1 * 3)     # (1,2,1,2,1,2)


t = (1,2,3,4,5)
print(t[1:4])      # (2,3,4)
print(t[::-1])     # reverse

points = {(1,2): "A", (3,4): "B"}
