
#DoubleString and Len of the added string
def double_word(word):
    newstr=word+word
    return newstr+str(len(newstr))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0