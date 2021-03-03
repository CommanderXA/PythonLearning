# 1
values = [1,2,3,4,5,6,7,8,9]
revlist = []

for index in range(len(values)):
    revlist.append(values[len(values) - index - 1])

print(revlist)

# 2
values = [1,2,3,4,5,6,7,8,9]
values.reverse()
print(values)

# 3
values = [1,2,3,4,5,6,7,8,9]
values_reversed = list(reversed(values))
print(values_reversed)

# 4
values = [1,2,3,4,5,6,7,8,9]
values = values[::-1]
print(values)