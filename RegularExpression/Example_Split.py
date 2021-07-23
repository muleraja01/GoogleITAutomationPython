import re

print(re.split(r"[.?!]","One sentence. Another one ? And the last one!"))
print(re.split(r"([.?!])","One sentence. Another one ? And the last one!"))

print(re.sub(r"^([\w .-]*), ([\w .-]*)$",r"\2 \1","Lovelace, Ada"))

print(re.split(r"the|a", "One sentence. Another one? And the last one!"))