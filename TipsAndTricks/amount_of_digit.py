num = 192354534354534

digit_amount = len(str(num))
print(digit_amount)

# ------------------------

import math

num = 0

if num > 0:
    print(int(math.log10(num)) + 1)
elif num < 0:
    print(int(math.log10(-num)) + 1)
else:
    print(1)

# ------------------------

num = 999999999999999997
counter = 1
while abs(num) >= (10 ** counter):
    counter += 1

print(counter)
