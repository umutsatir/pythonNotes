import datetime

simdi = datetime.datetime.now()
result = simdi.year # sadece yıl bilgisini alır.

result2 = datetime.datetime.ctime(simdi) # ay ve günü yazı şeklinde verir.
result2 = datetime.datetime.strftime(simdi, "%Y") # %y yılı temsil eder. Hangi harfin hangi bilgiyi verdiğini bulmak için:
# google'da datetime python diye aratıp python.org sitesinden öğrenebiliriz.

t = "21 April 2019 hour 10:12:30"
dt = datetime.datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)
dt = dt.year

birthday = datetime.datetime(2003,9,3) # saati 00:00:00 yazar.
print(birthday)
dt = datetime.datetime.timestamp(birthday) # saniye bilgisi verir.
dt = datetime.datetime.fromtimestamp(dt) # tekrardan tarih bilgisine (datetime) çevirir.

sonuc = birthday - dt # timedelta objesi getirir.
sonuc = sonuc.seconds # saniye bilgisi karşımıza gelir.

birthday = birthday + datetime.timedelta(days=10, seconds=20) # süreye ekleme yapma
# Eksi kullanarak tarihten çıkarma da yapabiliriz.




## OS Module

import os

print(os.name) # işletim sisteminin ismini yazdırır.
print(os.getcwd) # dosyanın hangi dizinde olduğunu yazdırır.
os.mkdir("newdirectory") # aynı dizin içerisinde newdirectory isminde klasör oluşturur.
os.chdir("C:\\") # dizini c diski olarak değiştirir. tırnak içine ../.. yazarsak aynı şeyi yapar.
# Eğer iki üstteki satırı üstteki satırın altına alırsak dosyayı c dizinine açar.
# chdir("..") bir üst dizine geçer. chdir("../..") iki üst dizine geçer.
os.makedirs("newdirectory/yeniklasör") # klasör içine klasör açar.

print(os.listdir()) # dizini listeler.
os.listdir("C:\\") # c diski içindeki bütün dosyaları listeler.


for dosya in os.listdir(): # sadece sonu .py olan dosyaları yazdırır.
    if dosya.endswith(".py"):
        print(dosya)


sonuc1 = os.stat("_ileri_seviye_modul.py")
sonuc1 = datetime.datetime.fromtimestamp(sonuc1.st_ctime) # dosyanın oluşturulma tarihini datetime modülüyle düzenliyoruz.
# ctime = creating time   atime = accessing time   mtime = modifying time

os.system("notepad.exe") # not defteri uygulamasını açar.

os.rename("newdirectory", "1") # newdirectory ismindeki klasörün ismini yeniklasör olarak değiştirir.
os.rmdir("yeniklasör") # yeniklasör ismindeki klasörü siler.
os.removedirs("1") # alt klasörü de varsa bu komut kullanılır. 1 ve içindeki yeniklasör klasörlerini siler.

# path
sonuc2 = os.path.abspath("deneme.py") # deneme dosyasının konumunu verir.
sonuc2 = os.path.dirname("C:\python\advanced-modules\deneme.py") # tam konumu verilen dosyanın dizinini verir.
sonuc2 = os.path.dirname(os.path.abspath("deneme.py")) # konumunu bilmediğimiz dosyanın dizinini bulur.
sonuc2 = os.path.exists("deneme.py") # bu isimde bir dosya var mı diye bakar ve varsa True döndürür.
# Üstteki satırı kullanarak klasörleri de arayabiliriz.

sonuc2 = os.path.isdir("C:\python\advanced-modules\deneme.py") # dizin mi yoksa klasör mü diye bakar. False değeri döndürür.
sonuc2 = os.path.isfile("C:\python\advanced-modules") #True döndürür.
sonuc2 = os.path.join("C:\\", "deneme", "deneme1") # dosya açmaz fakat böyle bir dizin oluşturur.
sonuc2 = os.path.split("C:\\deneme") # C ve deneme olarak iki dizini ayırır.
sonuc2 = os.path.splitext("deneme.py") # dosyanın ismiyle dosya adını ayırır.




## RE Module (Regular Expression)

import re

str = "Python Kursu: Python Programlama Rehberiniz | 40 Saat"
re.findall("Python", str) # Python ifadelerini bulur ve liste şeklinde geri döndürür.
re.split(" ", str) # her boşluktan itibaren ifadeyi böler.
re.sub("\s", "-") # bütün boşluk karakterlerini çizgi ile değiştirir. \s ile boşluk karakteri aynı şeydir.
a = re.search("Python", str) # ilk Python ifadesini arar ve match objesine dönüştürür. (span ifadesinde kaçıncı indexler arası olduğunu verir.)
print(a.span()) # Python ifadesinin hangi indexler arası olduğunu bulur. (span, match objesinin metodudur.)
a.start() # hangi karakterden başladığını söyler.
a.end() # hangi karakterde bittiğini verir.
a.group() # bulduğu ifadeyi gönderir.
a.string() # aradığı ifadeyi gönderir yani str'yi gönderir.
re.findall("[a-e]", str) # a'dan e'ye kadar bütün harfleri str içinde arar.
re.findall("[abc]", str) # a, b ve c'yi str içinde arar.
# [0-39] ile [01239] aynıdır.
# [^abc] dersek abc dışındaki bütün karakterleri arar. (^ = shift+3)
# [..] dersek iki karakter arar. Mesela 4 karakterli bir string verirsek 2 eşleşme döndürür.
# [Py..on] dersek iki nokta yerine her türlü 2 karakter gelebilir.
# [^P] dersek string belirtilen karakterle ya da karakterlerle BAŞLIYOR MU diye bakar.
# [saat$] dersek string belirtilen karakterle ya da karakterlerle BİTİYOR MU diye bakar.
# [ma*n] dersek a'dan sıfır veya daha fazla olmasını kontrol eder. Ör: main = False, maaan = True
# [ma+n] dersek a'dan bir veya daha fazla olmasını kontrol eder.
# [0,9]{2,4} dersek en az iki en fazla dört basamaklı sayıları kontrol eder.
# [0,9]{2} dersek iki basamaklı sayıları kontrol eder.
# a|b dersek a ya da b olmasını kontrol eder.
# (a|b|c)xz dersek a,b,c karakterlerinin arkasına xz gelmelidir. Ör: axz = True, bxz = True
# \ koyarsak özel karakterleri arayabiliriz. Ör: \$a dersek $ karakterini aramaya katar.
# \A - Belirtilen karakter stringin başında mı?
# \Z - Belirtilen karakter stringin sonunda mı?
# \b - Belirtilen karakter kelimenin başında ya da sonunda mı? Ör: \bthe başında, the\b sonunda
# \B - Belirtilen karakter kelimenin başında ya da sonunda değil mi? Ör: \Bthe başında, the\B sonunda
# \d = [0-9]
# \D = [^0-9]
# \s - Boşluk karakterlerini arar.
# \S - Boşluk karakterlerinin dışındakileri arar.
# \w Alfabetik karakterler, rakamlar ve alt çizgi karakterini arar.
# \W Alfabetik karakterler, rakamlar ve alt çizgi karakterinin dışındakileri arar.

# Bunların devamını python.org'da da bulabiliriz.