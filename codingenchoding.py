# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

s = input("Enter the message: ").upper()
i = int(input("For coding (1): \nFor decoding (2): \n"))
size = len(s)


if i == 1:
    # Coding:
    random_char1 = random.choice(s)
    #random_char2 = random.choice(s)
    if size >=3:
        s = s[1:] + s[0]
        s = random_char1 + s + random_char1

    else:
        s = s[::-1]
    
    print(f"The Message sent is: {s}")

# Decoding:
elif i == 2:
    if size < 3:
        s = s[::-1]
    else:
        start_removed = s[3:-3]
        last_letter = start_removed[-1]
        s = last_letter + start_removed

    print(f"The Message sent is: {s}")

else:
    print("INVALID INPUT!!!") 