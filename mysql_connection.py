import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", # localhost dışında IP de girebiliriz.
    user = "root",
    password = "******",
    database = "mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") 
# name ve adress sütunları olan bir tablo oluşturur.

# bu işlemleri IDE üzerinden zaten yapabiliyoruz, bu örneğin amacı databaseye giriş yapmak.



def insertProduct(a,b,c,d):
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()
    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" # %s yer tutucudur. Değişkenle değer vereceğiz.
    values = a,b,c,d
    cursor.execute(sql,values)
    try:
        connection.commit() # sorgunun çalışmasını sağlar. Sorgu DB'ye gönderilir.
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kaydın ID'si: {cursor.lastrowid}")
    except mysql.connector.Error as err: # hata verirse hatayı görmek için try except yaptık.
        print("hata:", err)
    finally: # finally her durumda çalıştırılır.
        connection.close()
        print("database bağlantısı kapandı.")

def insertProducts(liste):
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()
    sql = "INSERT INTO products(name,price,imageUrl,description) VALUES (%s,%s,%s,%s)" # %s yer tutucudur. Değişkenle değer vereceğiz.
    cursor.executemany(sql,liste)
    try:
        connection.commit() # sorgunun çalışmasını sağlar. Sorgu DB'ye gönderilir.
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"son eklenen kaydın ID'si: {cursor.lastrowid}")
    except mysql.connector.Error as err: # hata verirse hatayı görmek için try except yaptık.
        print("hata:", err)
    finally: # finally her durumda çalıştırılır.
        connection.close()
        print("database bağlantısı kapandı.")

list = []
while True:
    name = input("ürün adı: ")
    price = float(input("ürün fiyatı: "))
    imageUrl = input("ürün resim adı: ")
    description = input("ürün açıklaması: ")

    list.append((name,price,imageUrl,description))
    result = input("devam etmek istiyor musunuz?(e/h): ")
   
    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor...")
        insertProducts(list)
        break



## VERİLERİ GETİRME ##

def getProducts():
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products") # yıldız işareti bütün kolonları çağırmak için kullanılır.
    # SELECT name,price FROM products yazsaydık sadece name ve price kolonlarını getirirdi.
    result = cursor.fetchall() # birden fazla kayıt aldığımızda commit yerine bunu kullanıyoruz.
    result = cursor.fetchone() # sadece en baştaki kaydı getirir.
    print(result)



## KAYIT FİLTRELEME ##

def getProductsWhere():
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products WHERE id=1") # sadece id'si 1 olan satırları çağırır.
    cursor.execute("SELECT * FROM products WHERE name='Samsung S6' AND price=3000") # ismi samsung S6 olan ve fiyatı 3000 olan kayıtları çağırır.
    cursor.execute("SELECT * FROM products WHERE name='Samsung S6' OR price=3000") # ismi samsung S6 olan veya fiyatı 3000 olan kayıtları çağırır.
    cursor.execute("SELECT * FROM products WHERE name LIKE '%Samsung%'") #name sütununda Samsung kelimesini içeren kayıtları çağırır.
    cursor.execute("SELECT * FROM products WHERE name LIKE 'Samsung%'") #name sütununda başında Samsung kelimesi bulunan kayıtları çağırır.
    cursor.execute("SELECT * FROM products WHERE name LIKE '%S6'") #name sütununda sonu S6 ile biten kayıtları çağırır.

    result = cursor.fetchall()
    print(result)



## KAYIT SIRALAMA ##

def getProductsOrderBy():
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products ORDER BY name") # name kolonuna göre sıralama yapar.
    cursor.execute("SELECT * FROM products ORDER BY name DESC") # name kolonuna göre sıralama yapar ama ters sıralar. (descending = DESC, ascending= ASC)

    result = cursor.fetchall()



## AGGREGATE (HESAPLAMA) FONKSİYONLARI ##

def getProductsAgg():
    connection = mysql.connector.connect(host="localhost", user="root", password="******", database="node-app")
    cursor = connection.cursor()

    sql = "SELECT COUNT(*) FROM products" # satır sayısını sayar.
    sql = "SELECT AVG(price) FROM products" # fiyat alanının ortalamasını bulur.
    sql = "SELECT SUM(price) FROM products" # fiyat alanının toplamını bulur.
    sql = "SELECT MIN(price) FROM products" # minimum fiyatı bulur.
    sql = "SELECT MAX(price) FROM products" # maksimum fiyatı bulur.
    sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)" # maksimum fiyatın sahibi olan satırın ismini verir.

    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)