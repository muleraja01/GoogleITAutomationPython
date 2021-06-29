toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["starts"]=39 # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if "Chapter 5 " in toc: # Is there a Chapter 5?
    print("Key Exists")
else:
    print("Key not exists")