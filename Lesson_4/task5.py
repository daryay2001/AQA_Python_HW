# 5- The list of names is given: names = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Using the continue statement, print only the correct names to the console.

names_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names_list:
    if isinstance(name, str):
        print(name)
    else:
        continue
# v2

for name in names_list:
    if not isinstance(name, str):
        continue
    print(name)