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
    values = liste
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
