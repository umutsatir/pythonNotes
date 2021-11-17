## METOTLAR ##

list.append() # .append() bir metottur.

## FONKSİYONLAR ##

def sayHello(name): # Fonksiyonun içine yazılanlar fonksiyon çağırıldığı zaman kullanılır.
    print("Hello " + name)

sayHello("Umut") # Fonksiyonu boş çağırırsak hata verir. Bunun çözümü aşağıdaki örnekte:


def sayHello2(name2 = "user"): # Eğer defaultta user yazarsak:
    print("Hello " + name2)

sayHello2() # Fonksiyonu boş çağırırsak Hello user yazar ve hata vermez.



def total(num1, num2):# return ile değeri değiştirme
    '''
    DOCSTRING: iki sayıyı toplamanıza yarar.
    INPUT: num1
    OUTPUT: num2
    '''
    return num1+num2
result = total(10,20)
print(result)
help(total) # Açıklama metni olan fonksiyonun açıklamasını yazdırır.




## FONKSİYON PARAMETRELERİ ##

def changeName(n):
    n = "ada"

name = "yiğit"
changeName(name)
print(name) # n ile name farklı adreslerde olduğu için fonksiyon name değişkenini değiştirmedi.



def change(m):
    m[0] = "istanbul"

sehirler = ["ankara", "izmir"]
l = sehirler # Aynı adrese kaydoldular.
#l = sehirler[:] # sehirler listesinin kopyası oluşturulur. Farklı adrese kaydolurlar.
change(l)
print(l, sehirler) # Orijinal listenin adresi fonksiyona gönderildiği için fonksiyon listeyi değiştirir.



def add(*params): # Tuple listesi oluşturur.
    return sum(params) # sum komutu toplamaya yarar.
print(add(10,20,30))
print(add(10,20,30,40))
# NOT: FONKSİYON TANIMLAMA SATIRINDA TEK YILDIZ KOYUNCA TUPLE,
# İKİ YILDIZ KOYUNCA DICTIONARY LİSTE AÇAR.



def displayUser(**args): # iki yıldız dictionary list oluşturur.
    for key, value in args.items(): # args listesi içindeki key ve value değişkenlerini döndürecek.
        print(f"{key} is {value}")
displayUser(name = "Umut", age = 18, city = "Kocaeli", phone = "1231245")
displayUser(name = "Ahmet", age = 19, city = "İstanbul")



## LAMBDA EXPRESSIONS ##

#def square(num): return num ** 2
square = lambda numara: numara **2 # fonksiyon yerine bu kullanılabilir.
sayilar = [1,3,4,5,9,10]
result = list(map(square, sayilar)) # Listenin içindeki sayıların her birini fonksiyona gönderir.
print(result)
# veya
for item in map(lambda num: num ** 2, sayilar): # isimsiz bir değişken için lambda kullanılır.
    print(item)

def check_even(num): return num%2==0
sonuc = list(filter(check_even, sayilar)) # çift sayıları filtreler ve sadece onları bırakır.
# sonuc = list(filter(lambda num: num%2==0, sayilar)) # üst satırdaki kod ile aynı işi yapar.



## GLOBAL VE LOCAL DEĞİŞKENLER ##

x = "global x"

def function(): # Fonksiyonların içindeki tanımlamalar dıştaki tanımlamaları değiştiremez.
    # değiştirmek için global komutunu kullanmamız gerekir.
    # Eğer fonksiyon içerisinde x tanımlanmamışsa dıştaki x'i kullanır.
    x = "local x"
function()
print(x)







isim = "umut"
#global

def changeName(new_name):
    #local
    isim = new_name
    print(isim)
changeName("Mehmet") # içeri giren umut stringini değiştirip mehmet olarak printler.
print(isim) # fonksiyon çalışıp değişkeni farklı tanımlasa bile sadece fonksiyon içinde değiştirir bu yüzden
# en dıştaki umut stringini değiştiremez.



isim2 = "global string"
def greeting():
    isim2 = "umut"

    def hello():
        print("hello" + isim2) # buradaki isim2 değeri bir üsttekinden gelir yani hello umut printi gelir.
    hello()
greeting()



x = 50
def test():
    global x # global olarak tanımlarsak en dıştaki x değerini de değiştirir yani bütün kod satırlarında değişmiş olur.
    print(f"x: {x}")
    x = 100
    print(f"x changed to: {x}")
test(x)
print(x)