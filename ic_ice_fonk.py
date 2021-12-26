def greeting(name):
    print("hello ", name)

sayHello = greeting # ikisi de aynı adrese kaydolur.
# Hiçbir farkı yok.

def outer(num1):
    print("outer")
    def inner_increment(num1):
        return num1 + 1

outer(10) # sadece outer fonksiyonu çalışır. 
#İçteki fonksiyon çağırılmadığı için çalışmaz.


# encapsulation
def outer2(num1):
    print("outer")
    def inner_increment2(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment2(num1)
    print(num1, num2)

outer2(10) # iki fonksiyon da çalışır.
#inner_increment2(10) # fonksiyon içinde olduğu için dışarıda çalıştırılamaz.



def factorial(number):
    if not isinstance(number, int): # değişkenin type'ını kontrol etmek için kullanılır.
        raise TypeError("number must be an integer")

    if not number >= 0:
        raise ValueError("number must be zero or positive")
    
    def inner_factorial(number):
        if number <= 1:
            return 1
        
        return number * inner_factorial(number - 1)
    return inner_factorial(number)

try:
    print(factorial("4"))
except Exception as ex:
    print(ex)



## Fonksiyondan Fonksiyon Döndürme

def usalma(number):
    def inner(power):
        return number ** power
    return inner

two = usalma(2)
print(two(3)) # 2 üssü 3 gelir.



def yetki_sorgula(page):
    def inner(role):
        if role == "Admin":
            return "{0} rolü {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ulaşamaz.".format(role, page)
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpma

toplama = islem("toplama")
toplama(10,20,30)
carpma = islem("carpma")
print(carpma(1,3,5,20))



## Fonksiyonları Parametre Olarak Gönderme

def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(3,4))
    elif islem_adi == "bolme":
        print(f4(10,2))
    else:
        print("geçersiz işlem")

islem(toplama, cikarma, carpma, bolme, "toplama")



## Decorator Fonksiyonlar

def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("hello")

@my_decorator # sayGreeting fonksiyonuna özellik eklemiş olduk.
def sayGreeting():
    print("greeting")

# ya da üstteki olayı aşağıdaki gibi de yapabiliriz:
sayHello = my_decorator(sayHello)
sayHello() # sayHello fonksiyonuna özellik eklemiş olduk.


import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1) # 1 saniye delay olduğu için sonuç 1 saniye fazla çıkar.
        func(*args, **kwargs)
        finish = time.time()
        print(f"Fonksiyon {finish - start} saniye sürdü.")
    return inner

@calculate_time
def us_alma(a,b):
    print(math.pow(a,b))

@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

