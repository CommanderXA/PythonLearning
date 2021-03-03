words = ['Hey,', 'how', 'are', 'you?']

# 1
sentence = ""
for word in words:
    sentence += word + " "

print(sentence)

# 2
sentence = " ".join(words)
print(sentence)