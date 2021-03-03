a = 10
b = 20

# 1
temp = a
a = b
b = temp
print(a, b)

a = 10
b = 20

# 2
a, b = b, a
print(a, b)

# ----------------

a = 10
b = 20
c = 30
d = 40
e = 50

a,b,c,d,e = d,e,c,a,b
print(a,b,c,d,e)

# ----------------

a = 24
b = 41

'''

24 = 011000
41 = 101001
     110001 -> MASK

XOR

'''

a = a ^ b
b = b ^ a
a = a ^ b
print(a, b)
