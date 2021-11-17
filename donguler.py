## FOR DÖNGÜSÜ ##

sayilar = [1, 2, 3, 4, 5]

for abc in sayilar: # Listenin içerisinden tek tek elemanları alıp abc içerisine atar ve yazdırır.
    print(abc)



names = ["çınar", "sadık", "sena"]

for name in names: # İsimlerin hepsini tek tek cümle içine koyup yazar.
    print(f"my name is {name}")


isim = "umut"

for u in isim: # Harflerin hepsini tek tek yazar.
    print(u)


tuple = [(1,2), (1,3), (3,5), (5,7)]

for k,l in tuple: # tuple içindeki elemanların içindeki 2 rakamı ayrı ayrı değişkene atar ve tek tek yazdırır.
    print(k, " ", l)


d = {"k1":1, "k2":2, "k3":3} # Dictionary

for item in d: # Sadece key bilgileri gelir.
    print(item)

for deger in d.items(): # Hem key hem value bilgilerini verir.
    print(deger)





## WHILE DÖNGÜSÜ ##

x = 0
while x < 100: # 1'den 100'e kadar yazdırır.
    print(x)
    x += 1


myname = "" # False döndürür.
while not myname.strip(): # not name True döndürür. Strip ise kullanıcının boşluk girmesini engeller.
    myname = input("İsminizi giriniz: ") # İsim girince not myname False döner bu yüzden while kırılır.
print(f"Merhaba, {myname}")


## BREAK VE CONTINUE İFADELERİ ##

ismim = "Umut Satır"
for letter in ismim:
    if letter == "a":
        break # Burada a harfini görünce for döngüsünü kırar. Saddece Umut S yazdırır.
    print(letter)


ismim2 = "Umut Satır"
for letter2 in ismim2:
    if letter2 == "a":
        continue # Burada a harfini görünce for döngüsünü kırmaz,
        # sadece o anki döngü turunu kırar. Yani sadece bir tane for döngüsünü kırmış oldu. Umut Stır yazdırır.
    print(letter2)



## DÖNGÜ METOTLARI ##

for item in range(2,10): # İkiden dokuza kadar yazdırır.
    print(item)

print(list(range(50,100,20))) # 50 ile 100 arasında 20 fark olan sayıları yazdırır. 50,70,90



greeting = "Hello there"
for index, harf in enumerate(greeting): # enumerate ile hem index hem harfi yazdırabiliyoruz.
    print(index, harf)


list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
print(list(zip(list1, list2))) #  Dictionary listteki gibi iki liste birebir birleştirilir.

for a,b in zip(list1,list2):
    print(a) # sadece listenin 1,2,3,4,5 değerleri gelir.


## COMPREHENSIONS ##
# Comprehensionlar for döngülerini tek satırda yazmaya yarıyor.

sayilar2 = [x**2 for x in range(10)] # Bu comprehension ile yapılan versiyon
print(sayilar2)

sayilar3 = [] # Bu ise for döngüsü ile yapılan versiyonu
for x in range(10):
    sayilar3.append(x**2)
print(sayilar3)

sayilar4 = [z**2 for z in range(10) if z%3==0] # comprehensionlarda if de kullanılabiliyor.
print(sayilar4)

results = [c if c%2==0 else "tek" for c in range(1,10)] # if satır sonunda da değişkenden sonra da kullanılabiliyor.
# 1 ile 10 arasındaki sayılarda çiftleri yazdırır teklerin yerine ise "tek" yazdırır.
print(results)