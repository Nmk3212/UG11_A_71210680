print("======== Calculator Sederhana ========")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("5. Pangkat")
menu = int(input("Masukkan pilihan: "))
num1 = int(input("Masukkan bilangan 1: "))
num2 = int(input("Masukkan bilangan 2: "))

def calculator(menu):   
   if menu == 1:
      print("Hasilnya:", tambah(num1,num2))
   elif menu == 2:
      print("Hasilnya:", kurang(num1,num2))
   elif menu == 3:
      print("Hasilnya:", kali(num1,num2))
   elif menu == 4:
    print("Hasilnya:", bagi(num1,num2))
   elif menu == 5:
      print("Hasilnya:", pangkat(num1,num2))
   else:
      print("Hasilnya: Maaf input operasi antara 1-5")
def tambah(num1, num2):
   return num1 + num2
def kurang(num1, num2):
   return num1 - num2
def bagi(num1, num2):
   return num1 / num2
def kali(num1, num2):
   return num1 * num2
def pangkat(num1, num2):
   return num1 ** num2  
   
calculator(menu)