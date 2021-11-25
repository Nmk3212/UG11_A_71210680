def ambil_tengah(string, t = 0):
    count = len(string)
    b = (count // 2)
    if(t):
        return (string[b+t])
    else:
        return (string[b])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))