# x = int(input("x: "))
# y = int(input("y: "))
# print(x/y)

# üstteki işlemde oluşabilecek hataların yönetimi:

try:
    x = int(input("x: "))
    y = int(input("y: "))
except (ZeroDivisionError,ValueError): # ayrı ayrı except de yazılabilir.
    print("yanlış bilgi girdiniz.")

# ya da her hatayı engellemek istersek:
# while kullanarak hata olmayana kadar çalıştıralım.

while True:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
    except Exception as ex:
        print("yanlış bilgi girdiniz.")
        print(ex) # hata mesajını görmemizi sağlar.
    else:
        break



try:
    c = int(input("c: "))
    d = int(input("d: "))
except:
    print("yanlış bilgi girdiniz.")
finally: # bu blok her zaman çalışır (except çalışsa bile)
    print("try expect sonlandı.")



## Hata Türetme

x = 10
if x > 5:
    raise Exception("x 5ten büyük değer alamaz.")


def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception("parola en az 8 karakter olmalıdır.")
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")
    elif not re.search("[A-Z]", psw):
        raise Exception("parola büyük harf içermelidir.")
    elif not re.search("[0-9]", psw):
        raise Exception("parola rakam içermelidir.")
    elif not re.search("[_@$]", psw):
        raise Exception("parola alpha numeric karakter içermelidir.")
    elif not re.search("\s", psw):
        raise Exception("parola boşluk içermemelidir.")
    else:
        print("geçerli parola")

password = "123456"

try: # password parolasını kontrol etme
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("geçerli parola: else")
finally:
    print("validation tamamlandı")

