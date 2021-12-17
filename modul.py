## Modules ##
# Farklı py dosyalarını bir py dosyasında çalıştırma

# hazır 3. parti modül indirmek için: pip install package-name


## Hazır Modül Kullanımı

# import math
import math as islem # math yerine islem ismiyle modülü çağırabiliriz.

value = dir(islem) # math modülünün fonksiyonlarını gösterir.
value = help(islem) # math modülünü açıklar.
value = help(islem.factorial) # faktöriyel fonksiyonunu açıklar.

value = islem.factorial(5) # 5'in faktöriyelini alır.

# from math import * 
# # math modülünden hepsini import eder.

# from math import factorial,sqrt
# sadece factorial ve sqrt fonskiyonlarını import eder.

# ismi aynı olan 2 farklı fonksiyon olursa en sondaki fonksiyonu kabul eder.



## Random Modülü

import random

result = int(random.uniform(0,100)) # 0 ile 100 arasından rastgele bir sayı seçer.
result = random.randint(0,100) # üstteki satır ile aynıdır fakat int yazmamıza gerek kalmaz.



names = ["ali", "yağmur", "deniz", "cenk"]
result = names[random.randint(0,(len(names) - 1))] # listeden rastgele bir eleman seçer.
print(result)

result = random.choice(names) # üstteki olayı direkt yapar. Liste içinden bir eleman seçer.


liste1 = list(range(10))
random.shuffle(liste1) # listenin elemanlarını rastgele ekler.


liste2 = range(100)
result2 = random.sample(liste2, 3) # liste2 içinden rastgele 3 eleman seçer.



## Modül Oluşturma

import modul_olusturma as umut

print(umut.number)
p1 = umut.Person
p1.speak()