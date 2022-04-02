def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)

while True:
    y = int(input("Lütfen 1. sayıyı giriniz: "))
    z = int(input("Lütfen 2. sayıyı giriniz: "))
    x = int(input("Hesap Makinesi\n Lütfen yapmak istediğiniz işlemi seçiniz:\n 1- Toplama\n 2- Çıkarma\n 3- Çarpma\n 4- Bölme\n 5- Çıkış: "))
    if x == 1:
        sum(y,z)
    elif x == 2:
        sub(y,z)
    elif x == 3:
        mul(y,z)
    elif x == 4:
        div(y,z)    
    elif x == 5:
        break