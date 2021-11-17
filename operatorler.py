## ATAMALAR ##

liste = [1, 2, 3, 4, 5]

x, y, *z = liste # listedeki ilk 2 eleman tek tek x ve y'ye gider, kalan bütün elemanlar z'ye gider.
# z bir tuple listedir. Değişken isminin başına tek yıldız koyarsak tuple liste oluşturur.
print(x, y, z)



## KARŞILAŞTIRMA OPERATÖRLERİ ##

a, b, c, d = 5, 5, 10, 4

result = a == b
print(result) # True bilgisi gelir.

result = a == c
print(result) # False bilgisi gelir.



## MANTIKSAL OPERATÖRLER ##

x = 5
cikti = x > 5 and x < 10
print(cikti) # False bilgisi gelir.

cikti = not(x > 0) # Normalde değer True olur ama eğer NOT yazarsak False gelir.
print(cikti)


## IDENTITY (IS) VE MEMBERSHIP (IN) OPERATÖRLERİ ##

x = y = [1, 2, 3]
z = [1, 2, 3]

print(x == y) # True çıktısı verir.
print(x == z) # True çıktısı verir. Objeler aynı değerde mi diye bakar.

print(x is y) # True çıktısı verir.
print(x is z) # False çıktısı verir. Objeler aynı adreste mi diye bakar.

x = ["apple", "banana"]
print("banana" in x) # True çıktısı verir.
isim = "umut"
print("u" in isim) # True çıktısı verir.
