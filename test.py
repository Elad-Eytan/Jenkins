import sys
import os

file_path = sys.argv[0]
word_to_find = sys.argv[1]

with open(file_path, "r") as file:
    content = file.read()

    if word_to_find in content:
        print(f"{word_to_find} is in the file!!!")
    else:
        print(f"{word_to_find} is not in the file!!!")