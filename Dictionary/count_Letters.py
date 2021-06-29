

def count_Letters(text):
    result={}
    for letter in text:
        if letter not in result:
            result[letter]=0
        result[letter]+=1
    return result

print(count_Letters("Raja"))
print(count_Letters("Automation Testing"))

