## Dosya Açma

# "w" = write - ekleme yaptığımızda dosya içeriğini silip baştan yazar.
# "a" = append - var olan içeriğin sonuna ekler.
# "r" = read
# "x" = create - sadece dosyayı oluşturur.

file = open("c:/users/user/desktop/newfile.txt", "a", encoding="utf-8")
# eğer direk kendi konumuna dosya açmak istersek "newfile.txt" yazabiliriz.
file.write("Umut Satır")
file.close()


file2 = open("c:/users/user/desktop/newfile.txt", "r", encoding="utf-8") # "r" yazmasak bile otomatik olarak r atanır.

# for döngüsü ile okuma
for i in file2:
    print(i, end="") # boş satır bırakmamak için end komutunu yazdık.

# read() fonksiyonu ile okuma
content = file2.read() # read komutunu 2 kere çalıştırmak için hemen sonraki satırına close yapmamız lazım.
print(content)
# file2.read(5) dersek ilk 5 karakteri okur ve cursoru 5. karakterin sonuna koyar, ikinci okuma
# işleminde ise cursorun olduğu yerden devam eder. (eğer file2.close yapmadıysak)

content2 = file2.readline() # bir satırı okur ve cursoru 2. satırın başına koyar.
print(content2)

liste = file2.readlines() # her bir satırı liste elemanı haline getirir.
print(liste)



## Dosya Okuma Fonksiyonları

with open("newfilex.txt", "r", encoding="utf-8") as file3: 
    #with'te en sonda otomatik olarak close fonksiyonunu çağırır.
    content3 = file3.read()
    print(content3)
    print(file3.tell()) # cursorun kaçıncı karakterde olduğunu söyler.
    file3.seek(0) # cursoru sıfırıncı karaktere gönderir.



## Dosya Güncelleme

with open("yenidosya.txt", "r+", encoding="utf-8") as dosya: # r+ hem okuma hem de yazma oluyor.
    dosya.write("deneme") # sayfa başından insert modunda güncelleme yapar.

# append "a" ile dosyanın en sonunu güncelleyebiliyoruz.


with open("yenidosya.txt", "r+", encoding="utf-8") as dosya2:
    content4 = dosya2.read()
    content4 = "Umut Satır\n" + content4
    dosya2.seek(0)
    dosya2.write(content4)
    # sayfa başına yazı ekleme (insert modunda değil)


with open("yenidosya.txt", "r+", encoding="utf-8") as dosya3:
    liste2 = dosya3.readlines() # bütün içerik list şeklinde gelir.
    liste2.insert(1, "Ali Akgün") # 1. indexe Ali Akgün çıktısını ekler.
    dosya3.seek(0)
    dosya3.writelines(liste2)