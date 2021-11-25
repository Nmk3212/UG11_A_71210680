def ambildanbalik(string, start, stop, balikkata):
    if(balikkata):
        balik = string[start-1:stop]
        return (balik[::-1])
    else:
        return (string[start-1:stop])

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))