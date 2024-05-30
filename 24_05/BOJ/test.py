import sys

num = 123
num_size = sys.getsizeof(num)

text = "123"
text_size = sys.getsizeof(text)

print(num_size)
print(text_size)