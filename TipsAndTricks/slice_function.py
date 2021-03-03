nums = [10, 90, 20, 55, 65, 70, 5, 15, 85]

print(nums[3:6]) # The "6" not included
print(nums[:-2]) # Gives all until the second last element

LASTFOUR = slice(-4, None)
print(nums[LASTFOUR])

FIRSTFOUR = slice(4)
print(nums[FIRSTFOUR])

EVERY_OTHER = slice(0, None, 2)
print(nums[EVERY_OTHER])

SOMETHING = slice(2, 7, 2)
print(nums[SOMETHING])

text = "Hello, how are you?"
print(text[EVERY_OTHER])