from asyncio.windows_events import NULL
import pandas as pd
import numpy as np

numbers = [1,2,3,4]
sozluk = {"a":10, "b":20, "c":30, "d":40}

pandas_series = pd.Series(5, ["a","b","c","d"]) # 5 rakamını sağdaki a,b,c,d key bilgileriyle eşleştirir.
pandas_series = pd.Series(numbers, ["a","b","c","d"]) # aynı şekilde skaler bilgi yerine dizi de kullanabiliriz.
# Çıktıda a,b,c,d index olur 5 ise indexlere bağlanan bilgi olur.

pandas_series = pd.Series(sozluk) # Direk Dictionary liste de verebiliriz.



## DATAFRAMES ## 

# iki tane Series'i birleştirince dataframe oluşur. Excel dosyası olarak düşünürsek:
# Series bir sütunu belirtirse dataframe birkaç Series'in birleşimi olan bir tablodur.

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)



## FARKLI DOSYA TİPLERİNDEN VERİ OKUMA ##

# df = pd.read_csv("") ile csv dosyalarını okuyabiliriz.

# df = pd.read_json("", encoding="UTF-8") ile json dosyalarını okuyabiliriz. 
# (encoding bölümünü yazmazsak türkçe karakterleri göstermez.)

# df = pd.read_excel("") ile Excel dosyalarını okuyabiliriz. 
# DİKKAT : Excel dosyası okumak için bir modül yüklememiz gerekli. (pip install xlrd)

# import sqlite3 # MODÜL İNDİRMEMİZ GEREKLİ! (pip install pysqlite3)
# connection = sqlite3.connect("dosyaadi.db")
# df = pd.read_sql_query("SELECT * FROM tabloadi") 
# Bu kodlar ile veritabanı dosyalarını okuyabiliriz. 



## DATAFRAMELERDE SATIR, SÜTUN VE HÜCRE SEÇME ##

df = pd.DataFrame(np.random.randn(3,3), index=["A", "B", "C"], columns=["Column1","Column2","Column3"])

result = df["Column1"] # sütun seçimi
result = df.loc[:,"Column1"] # farklı bir sütun seçimi
result = df[["Column1", "Column2"]] # birden fazla sütun seçimi
result = df.loc[:,["Column1","Column2"]] # farklı bir birden fazla sütun seçimi
result = df.loc[:,"Column1":"Column3"] # farklı bir birden fazla sütun seçimi 
# (Column1 ile Column3 arasındaki bütün sütunları getirir, Column1 ve Column3 de dahil.)

result = df.loc["A"] # satır seçimi (loc, location'un kısaltmasıdır.)
result = df.loc["A":"C"] # birden fazla satır seçimi (A,B ve C satırlarını çağırır.)
result = df.loc[:"C"] # üstteki satırın bir farklı yazımı (en baştan C sütünuna kadar çağırır. C dahil)
result = df.iloc[0] # index ile de çağırabiliriz. iloc index ile çağırmamızı sağlar.

result = df.loc["A", "Column2"] # belirli bir satır ve sütundaki veriyi getirir.

df.drop("Column3", axis=1, inplace=True) # 3. sütunu siler. Dataframe üzerinde değişiklik yapılması için inplace=True olmalıdır.
# Eğer Dataframe değişmesin, silinmiş halinin kopyasını alsın dersek:
sonuc = df.drop("Column3", axis=1, inplace=False) # bu durumda sonuc üzerine silinmiş olan halinin kopyası gönderilir, df'de değişiklik yapılmaz.

df["Column4"] = df["Column1"] + df["Column2"] # yeni sütun ekleme
df["Column5"] = pd.Series(np.random.randn(3), ["A","B","C"]) # yeni 3 tane random sayıyla yeni bir sütun oluşturur.



## DATAFRAME FİLTRELEME ##

data1 = np.random.randint(10,100,75).reshape(15,5) # 15 satır 5 sütunlu dataframe oluşturduk.
df2 = pd.DataFrame(data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])

sonuc2 = df.columns # sütun isimlerini verir
sonuc2 = df.head() # ilk 5 satır gelir.
sonuc2 = df.head(10) # ilk 10 satır gelir.
sonuc2 = df.tail() # son 5 satır gelir.
sonuc2 = df.tail(10) # son 10 satır gelir.
sonuc2 = df["Column1"].head() # ilk beş satırın sadece 1. sütunlarını getirir.
sonuc2 = df[["Column1", "Column2"]].head() # ilk beş satırın 1. ve 2. sütunlarını getirir.
sonuc2 = df[df > 50] # 50'den büyük olanları getirir, küçük olanları NaN olarak getirir.
sonuc2 = df[df["Column1"] > 50]["Column1"] # 1. sütundaki 50'den büyük olan sayıları getirir.

sonuc2 = df[5:15][["Column1", "Column2"]].head() 
# 5 ile 15. satır arasındaki ilk 5 satırın (yani 5,6,7,8 ve 9. satırın) 1. ve 2. sütunlarını getirir.

sonuc2 = df.query("Column1 >= 50 & Column1 % 2 == 0")["Column1"] # sütun 1'deki 50'den büyük ve çift sayıları getirir.



## DATAFRAMELERDE GROUPBY KULLANIMI ##

df = pd.read_csv("imdb_top_1000.csv")

sonuc3 = df.groupby("IMDB_Rating") # IMDB puanına göre filmleri grupladık. Aynı puandakiler aynı gruba düştü.
for name in sonuc3:
    print(name)

sonuc3 = df.groupby("IMDB_Rating").get_group(9.0) # IMDB puanı 9.0 olan filmleri getirir.

sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].mean() # aynı yıllarda çıkan filmlerin yıllarına göre IMDB puan ortalamasını bulur.
sonuc3 = df.groupby("Released_Year")["Released_Year"].count() # hangi yılda kaç film çıktığını gösterir.
sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].min() # her yılın en düşük IMDB puanını gösterir.
sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].max() # her yılın en yüksek IMDB puanını gösterir.
sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].max()["1999"] # 1999 yılındaki maksimum IMDB puanını gösterir.

sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].agg([np.mean,np.min,np.max]) 
# numpy kullanarak maksimum, minimum ve ortalamayı tek bir tablo olarak alabiliriz.

sonuc3 = df.groupby("Released_Year")["IMDB_Rating"].agg([np.mean,np.min,np.max]).loc["1999"]
# sadece 1999 yılının minimum, maksimum ve ortalama IMDB puanlarını tek tabloda alabiliriz.



## PANDAS İLE KAYIP VE BOZUK VERİ ANALİZİ ##

data2 = np.random.randint(10,100,15).reshape(5,3)

df3 = pd.DataFrame(data, index=["a","c","e","f","h"], columns=["column1","column2","column3"])
df3 = df3.reindex[["a","b","c","d","e","f","h"]] # indexleri yeniden yazmamızı sağlar. Boş yerleri NaN yapar.

# df3.isnull() NaN olan yerleri True, diğerlerini False döndürür.
# df3.notnull() NaN olan yerleri False, diğerlerini True döndürür.

sonuc4 = df3.dropna() # NaN değeri olan satır varsa satırı düşürür. (default axis=0 olduğu için satıra göre siler.)
# eğer axis=1 dersek sütunlarda bir tane bile NaN olursa o sütunu siler.

sonuc4 = df3.dropna(how="all") # tüm satır NaN ise siler, değilse silmez.
sonuc4 = df3.dropna(subset=["column1","column2"]) # NaN için sadece yazdığımız sütunlara bakar.
sonuc4 = df3.dropna(thresh=2) # en az 2 tane veri (NaN olmayan) olan kayıtları silmez.
sonuc4 = df3.fillna(value="no input") # NaN olan yerlere no input yazar. int değer de girilebilir.

def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum() # df3.size eleman sayısını verir.
    return toplam / adet

sonuc4 = df3.fillna(value = ortalama(df3)) # NaN olan yerleri tablodaki bütün değerlerin ortalaması ile doldurur.



## PANDAS İLE STRİNG FONKSİYONLARI ##

veri = pd.read_csv("imdb_top_1000.csv")

veri.dropna(inplace=True)
veri["Series_Title"] = veri["Series_Title"].str.upper() # bütün dizi isimlerini büyük harf yapar.
veri["Series_Title"] = veri["Series_Title"].str.find("a") # a harfi geçen dizi isimlerini arar.
veri["Series_Title"] = veri["Series_Title"].str.contains("Shawshank") # Shawshank kelimesini içeren kayıtları çeker.
veri = veri.Series_Title.str.replace(" ","-").str.replace("*", "") # aynı yerden devam edip bir işlem daha yapmak istersek böyle kullanabiliriz.
# Burada bütün str komutlarını kullanabiliriz.



## PANDAS İLE JOIN VE MERGE ##

customers = {
    "customerID": [1,2,3,4],
    "firstName": ["ahmet","ali","hasan","canan"],
    "lastName": ["yılmaz","korkmaz","çelik","toprak"]
}

orders = {
    "orderID": [10,11,12,13],
    "customerID": [1,2,5,7],
    "orderDate": ["2010-07-04","2010-08-04","2010-07-07","2012-07-04"]
}

df_customers = pd.DataFrame(customers, columns=["customerID", "firstName", "lastName"])
df_orders = pd.DataFrame(orders, columns=["orderID","customerID","orderDate"])

# df_customers'a A kümesi ve df_orders'a B kümesi dersek:
result2 = pd.merge(df_customers,df_orders, how="inner") # AnB (kesişim)
result2 = pd.merge(df_customers,df_orders, how="left") # A
result2 = pd.merge(df_customers,df_orders, how="right") # B
result2 = pd.merge(df_customers,df_orders, how="outer") # AuB (birleşim)


customersA = {
    "customerID": [1,2,3,4],
    "firstName": ["ahmet","ali","hasan","canan"],
    "lastName": ["yılmaz","korkmaz","çelik","toprak"]
}

customersB = {
    "customerID": [5,6,7,8],
    "firstName": ["veli","can","hüseyin","baran"],
    "lastName": ["şatır","cihangir","çelikoğlu","turan"]
}

result3 = pd.concat(customersA,customersB) # iki dataframe'yi alt alta birleştirir.
result3 = pd.concat(customersA,customersB, axis=1) # iki dataframe'yi yan yana birleştirir.



## PANDAS İLE DATAFRAME METOTLARI ##

data3 = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,45,25],
    "Column3": ["abc","bca","ade","cba","dea"]
}

df4 = pd.DataFrame(data3)

result4 = df["Column2"].unique() # verilen satırdaki tekrarlamayan bilgilerin hepsini verir.
result4 = df["Column2"].nunique() # verilen satırdaki tekrarlamayan bilgilerin sayısını verir.
result4 = df["Column2"].value_counts() # sütundaki hangi değerden kaç tane olduğunu gösterir. Ör: 25'ten 2 tane var vs.

def kareal(x):
    return x*x

kareal2 = lambda x: x*x # kareal fonksiyonu ile aynı işi görür.

result4 = df["Column2"].apply(kareal) # apply ile sütundaki değerleri vererek fonksiyon çalıştırabiliriz.
result4 = df["Column3"].apply(len) # aynı şekilde uzunluk metodunu kullandık.
result4 = df.sort_values("Column2") # küçükten büyüğe sıralar. str ise z-a sıralar.
result4 = df.sort_values("Column2", ascending=False) # büyükten küçüğe sıralar. str ise a-z sıralar.

data4 = {
    "Ay": ["Mayıs", "Haziran","Nisan","Mayıs", "Haziran","Nisan","Mayıs", "Haziran"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

result4 = df.pivot_table(index="Ay", columns="Kategori", values="Gelir") 
# indexleri Nisan,Mayıs,Haziran; sütunları Elektronik,Kitap,Giyim yapar.