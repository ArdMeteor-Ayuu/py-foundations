A = "AyushRocks"

print(A[0:3])  # Ayu
print(A[2:])  # ushRocks
print(A[:4])  # Ayus
print(A[:])  # AyushRocks
print(A[-5:])  # Rocks
print(A[:-3])  # AyushRo
print(A[-7:-2])  # shRoc
print(A[::2])  # AuhOk
print(A[1::2])  # ysRcs
print(A[::-1])  # skcoRhsyA
print(A[2:9:3])  # uRk
rev1 = A[::-1]
rev2 = A[-1:-7:-1]
rev3 = "".join(reversed(A))

print(rev1, rev2, rev3)

