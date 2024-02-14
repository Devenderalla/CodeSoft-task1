password generator

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=?><[]"
all_chars = lower + upper + numbers + symbols

length = int(input("Enter a length: "))
password = ''.join(random.choices(all_chars, k=length))
print("Generated password:", password)
