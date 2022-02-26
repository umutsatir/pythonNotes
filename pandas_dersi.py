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

