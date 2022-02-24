import numpy as np

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

# Numpy array'leri daha az yer kaplar ve daha fazla fonksiyon içerir. Bu yüzden numpy kullanışlı bir modüldür.
py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # matris(çok boyutlu dizi) oluşturma

result = np.arange(1,10) # 1,2,3,4,5,6,7,8,9 elemanlarıyla dizi oluşturur.
result2 = np.arange(10,100,3) # 10'dan 100'e üçer üçer eleman alarak dizi oluşturur.
result3 = np.zeros(10) # 10 tane sıfır elemanı olan dizi oluşturur. Ayrıca her eleman float olarak oluşturulur.
result4 = np.linspace(0,100,5) # 5 elemanlı dizi oluşturur, dizinin elemanları 0 ile 100 arasında aynı farktadır.
# result4 çıktısı 0,25,50,75,100 olur.
result5 = np.random.randint(1,10,3) # rastgele üretilen 3 eleman ile dizi oluşturur.

np_array2 = np.arange(50)
np_multi2 = np_array2.reshape(5,10) # 5 satır 10 sütunluk bir çok boyutlu array oluşturur.
print(np_multi2.sum(axis=0)) # sütunların toplamlarını verir.
print(np_multi2.sum(axis=1)) # satırların toplamlarını verir.

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers.max()) # listedeki maksimum değeri yazdırır.
print(rnd_numbers.min()) # listedeki minimum değeri yazdırır.
print(rnd_numbers.mean()) # listedeki ortalama değeri yazdırır.
print(rnd_numbers.argmax()) # listedeki maksimum değerin indexini yazdırır.
print(rnd_numbers.argmin()) # listedeki minimum değerin indexini yazdırır.




## NUMPY DİZİLERİNİN İNDEXLENMESİ ##

numbers = np.array([[0,5,10],[15,20,25],[50,75,85]])

sonuc = numbers[0,1] # ilk satırın 1. indexteki değerini alır. 5 çıktısı verir.
sonuc2 = numbers[:,2] # bütün satırların son elemanını alır. İki nokta bütün satırları kapsar.

arr1 = np.arange(0,10)
arr2 = arr1 # referans kopyalaması
# arr1'in adresinin bir kopyasını arr2'ye verdik.
# arr2 değiştirilirse arr1 de değişir.

arr3 = arr1.copy() # arr1 ile arr3 aynı adreste olmaz ve arr3'de değişiklik yapılsa bile arr1'de gerçekleşmez.



## NUMPY DİZİ OPERASYONLARI ##

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
# iki diziyi toplarsak aynı indexteki sayıları toplar. 4 işlemde hep bu şekilde yapar.
# aynı şekilde numbers1 - 10 da yapabiliriz.
np.sin(numbers1) # dizilerin sinüs veya cosinüsünü alabiliriz. (sin veya cos metodu)
np.cos(numbers2)
np.sqrt(numbers1) # logaritma veya karekökünü de alabiliriz. (sqrt ile karekök; log ile de logaritma modülünü kullanabiliriz.)
np.log(numbers2)

mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

result6 = np.vstack(mnumbers1, mnumbers2) # vertical stack yani dikey olarak birleştirir.
# İlk matrisin altına ikinci matrisi ekler.
result7 = np.hstack(mnumbers1,mnumbers2) # horizontal stack yani yatay olarak birleştirir.
# İlk matrisin yanına ikinci matrisi ekler.

result8 = numbers1 >= 50 # numbers1 dizisinin her elemanı için bool değer döndürür.
# 50'den küçükse False, diğer durumlarda True döndürür.

print(numbers1[result8]) # True olan değerleri numbers1'den bulup gönderir.
# Bu sayede işimize yarayacak olan değerleri alabiliriz.