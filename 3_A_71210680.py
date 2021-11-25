kalimat = input("Masukkan Kalimat: ")
start = int(input("Index Start: "))
stop = int(input("Index Stop: "))

def hitung_hapus(kalimat, start, stop):
    count = len(kalimat)
    hapus = len(kalimat[start-1:stop])
    present = (hapus / count) * 100
    return present

print(hitung_hapus(kalimat, start, stop))