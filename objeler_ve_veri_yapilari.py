result = 200/700
print("the result is {r:1.3}".format(r=result))
# r:1.3 olunca birler basamağına bir rakamlık yer bırakır
# virgülden sonraki bölüme de 3 satırlık yer bırakır.


name, surname = "Umut", "Satır"
print(f"My name is {name} {surname}")
# f kullanınca direk parantezler içine değişkenleri yazabiliyoruz.



a = "abcdefghijklmnoprsqxuvyz"
print(a[1:5])
# dizi sıfırdan başlar o yüzden 2. karakterden
# başlayıp 6. karaktere KADAR olan harfleri yazdırır.
print(a[1:5:2]) # 2 adımda bir karakter alır. mesela a alır b almaz c alır.
print(a[::-1]) # tersten yazdırır.

message = " Merhaba ben Umut"
message = message.split() # mesajın boşluk olan kısımlarından list elemanları olarak ayırır.
# message = message.split(".") # mesajı noktadan ayırır.
# message = message.strip() # baştaki ve sondaki boşlukları siler.
# Sadece sol için lstrip, sadece sağ için rstrip
# message = message.strip("/:pth") # baş ve sondaki h,t,p,/,: harf ve sembollerini siler.

message = " ".join(message) # listteki girdileri tırnak içindekileri araya koyarak birleştirir.
print(message)

index = message.find("Umut") # mesajda kelime bulmaya yarar.
print(index) # sonuç -1 gelirse kelime yok demektir.
# Sonuç örn. 10 gelirse o kelime cümle içinde 10. harften itibaren başlıyor demektir.

isfound = message.startswith("M") # String M ile mi başlıyor diye bakar.
isfound2 = message.endswith("U") # String U ile mi bitiyor diye bakar.
print(isfound, isfound2)

message = message.replace("Umut", "Hüseyin") # kelimeleri değiştirmeye yarar.
print(message)
# message = message.replace().replace() yapılabiliyor.

message = message.center(50, "*") # 50 karakterlik boşlukta stringi ortalar ve sağ ile solunu yıldız ile kaplar.
print(message)

sayidegeri = message.isdigit() # Alınan verinin sayılardan mı oluştuğuna bakar.
# Bir tane bile harf olursa False döndürür.
print(sayidegeri) # isalpha olursa harf mi diye bakar.


#####Listeler#####
arabalar = ["BMW", "Mercedes", "Opel", "Mazda"]
sonuc = "Mercedes" in arabalar # listelerin içindekileri görmek için bool döndürür
arabalar2 = arabalar + ["Audi", "Nissan"] # eski listeye girdi ekleyerek
# başka bir liste oluşturur.
print(sonuc, arabalar2)
arabalar.append("Fiat") # yeni liste oluşturmadan halihazırdaki listeye ekler.
arabalar.remove("Fiat") # listeden istenilen veriyi siler.
arabalar.insert(0,"Fiat") # sıfırıncı indexe Fiat verisini ekler. İstediğimiz indexe eklemeye yarar.
arabalar.pop(0) # sıfırıncı indexteki veriyi siler.
arabalar.sort() # sayı değeriyse küçükten büyüğe, yazı ise alfabetik olarak sıralar.
arabalar.reverse() # sıralamayı ters çevirir.
# Eğer sort komutundan sonra kullanılırsa tam tersini yapar. Ama tek başına kullanılırsa baştaki dizilimi ters çevirir.
print(arabalar.count("BMW")) # arabalar listesinde kaç tane BMW olduğunu yazar.
abc = arabalar.index("Opel") # BMWnin index numarasını alır.
print(abc) # BMWnin kaçıncı indexte olduğunu yazdırır.
arabalar[0] = "Pontiac" # listeden istediğimiz indexi değiştirebiliriz.

# indexlerde başta yazdığımız rakamdan başlar sondaki dahil değildir.
# Örn. [3:6] 3 dahil 6 dahil değildir.

arabalar.clear() # bütün elemanları siler.


## ÖRNEK ##
cars = ["BMW"]
gelendeger = input("Lütfen marka giriniz: ")
cars.append(gelendeger)
print(cars) # girilen değeri listeye ekleme örneği



#### TUPLE LİSTELER ####
liste = [1, 2, 3]
tupleliste = (1, "iki", 3)

# tuple listelerde elemanlar atandıktan sonra herhangi bir elemanı değiştiremeyiz.


#### DICTIONARY LİSTELER ####
# verilen değer başka bir değeri getiriyor. Örn. 34 yazınca istanbul değeri getirecek.

plakalar = {"kocaeli" : 41, "istanbul" : 34}
print(plakalar["kocaeli"])
plakalar["ankara"] = 6 # eleman ekleme veya güncelleme
print(plakalar)

# önemli bölüm
users = {
    "umutsatir" : 1,
    "huseyinsatir" : {
        "yaş" : 36,
        "email" : "umutstr54@gmail.com"
    }
}
print(users["huseyinsatir"])
print(users["huseyinsatir"]["yaş"])

users.update({  # bilgi güncelleme
    "yaş" : 18
})
print(users)




#### SETS ####
fruits = {"orange", "apple", "banana"}
# sets indexlenemez!

for x in fruits: # sadece böyle gösterilebilir, sıralanamıyor.
    print(x)

fruits.add("cherry") # tek tek ekleme
fruits.update(["mango", "grape"]) # birden fazla ekleme
print(fruits)

# bir set içerisinde aynı elemandan sadece bir tane olabilir. Örn:
mylist = [1,2,5,4,4,3,1]
print(set(mylist)) # listeyi sete dönüştürür, tekrar eden veriler gider.

fruits.remove("mango") # veri siler.
fruits.discard("apple") # veri siler.
# fruits.pop doğru çalışmaz çünkü index yok. Yanlış bir şeyi silebilir.
fruits.clear() # bütün elemanları siler.



#### VALUE VE REFERENCE TYPE ####
## VALUE
q = 5
w = 25
q = w
w = 10
print(q, w) # aynı olmazlar, veriler farklı yerlerde depolanıyor.

## REFERENCE
e = [5, 10, 15]
r = [25, 30, 35]
e = r
r[0] = 45
print(e, r)  # aynı olurlar çünkü veriler aynı adrese kaydoldu.
# liste bir adres taşır, veri taşımaz. Ondan dolayı listeleri eşitlersek adresler aynı olur.
# Adresteki veriler değiştikçe ikisinde de değişmiş olur.
