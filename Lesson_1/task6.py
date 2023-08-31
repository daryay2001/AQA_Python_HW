# 6. Create a list with people's names, some names should be repeated in it.
# Turn a list of duplicate names into a list of unique names using sets.

name_list = ["Dasha", "Angela", "Brandon", "Noel", "Angela", "Kristina", "Brandon"]
new_name_set = set(name_list)
new_name_list = list(new_name_set)
print(name_list)
print(new_name_set)
print(new_name_list)