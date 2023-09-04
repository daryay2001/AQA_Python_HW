# 4 - You have 3 groups of people casino_blacklist, poker_blacklist, alcohol_blacklist.
# Names of people in the format "John Dow" first and second name.
# Find those who are on all blacklists.

casino_blacklist = ["John Dow", "Laura Wheeler", "Kate Pirson", "Patric Rang", "Jessey Pedro"]
poker_blacklist = ["Susan Harris", "Gary Cooper", "John Dow", "Laura Wheeler", "Patric Rang"]
alcohol_blacklists = ["Anna Smith", "John Dow", "Ralph Terry", "Patric Rang", "Gary Cooper"]

set_casino = set(casino_blacklist)
set_poker = set(poker_blacklist)
set_alcohol = set(alcohol_blacklists)

print(f"People in all blacklists:\n{set_casino.intersection(set_poker, set_alcohol)}")