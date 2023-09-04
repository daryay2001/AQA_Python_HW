# 6 -
#
# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example: If the following string is given as input to the program:
#
# abcdefgabc
#
# Then, the output of the program should be:
#
# a,2 c,2 b,2 e,1 d,1 g,1 f,1
#
# Hints: Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.
#
# Use str.join() method and dict comprehension for print result.

user_string = input("Enter your string: ").strip()
values_dict = {}

for val in user_string:
    values_dict[val] = values_dict.get(val, 0) + 1 # замість count

values_list = [f"{val},{numb}" for val, numb in values_dict.items()]

result = " ".join(values_list)

print(result)


