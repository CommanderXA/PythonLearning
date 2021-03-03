mylist = [1,2,3,4,3,5,6,9,3,5,7,5,4,3,4,6,5]
current_max = 0
current_val = None
for x in mylist:
    if mylist.count(x) > current_max:
        current_max = mylist.count(x)
        current_val = x

print(f"Value: {current_val}, Occurrences: {current_max}")

# --------------------------

from collections import Counter

counter = Counter(mylist)

# Gives an array of tuples. 
# The first element is the most frequent num and the second is how many times it occurres
print(counter.most_common(3)) 

print(counter.most_common(3)[0][0]) 

# --------------------------

print(set(mylist))
print(max(mylist, key=mylist.count))
most_frequent = max(set(mylist), key=mylist.count)
frequency = mylist.count(most_frequent)

print(most_frequent, frequency)
