

file_Count={"jpg":10,"txt":35,"csv":2,"pdf":10}

for ext in file_Count:
    print(ext)

for ext, amount in file_Count.items():
    print("There are {} files with .{} extension".format(amount,ext))
print(file_Count.keys())
print(file_Count.values())