import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost", # localhost dışında IP de girebiliriz.
    user = "root",
    password = "**********",
    database = "mydatabase",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor(buffered=True)

def createNote(a,b,c):
    sql = "INSERT INTO notetaking(title,note,time) VALUES(%s,%s,%s)"
    values = (a,b,c)
    mycursor.execute(sql, values)
    print("\nKayıt tamamlandı.")
    mydb.commit()

def editNote(a,b,c):
    sql = "UPDATE notetaking SET title = %s, note = %s WHERE id = %s"
    values = a,b,c
    mycursor.execute(sql, values)
    mydb.commit()
    print("\nKayıt düzenlendi.")

def deleteNote(a):
    sql = "DELETE FROM notetaking WHERE id = %s"
    values = (a,)
    mycursor.execute(sql, values)
    mydb.commit()
    print("\nKayıt silindi.")


def showNotes():
    mycursor.execute("SELECT * FROM notetaking")
    result1 = mycursor.fetchall()
    print("\nROWS: id, title, note, time")
    for x in result1:
        print(x, "\n")

while True:
    a = int(input("\nNot Defteri\n Lütfen menüden seçim yapınız.\n 1- Not Al\n 2- Not Düzenle\n 3- Not Sil\n 4- Notları Görüntüle\n 5- Çıkış: "))
    if a == 1:
        b = str(input("Lütfen not başlığı giriniz: "))
        c = str(input("Lütfen not giriniz: "))
        d = datetime.datetime.now()
        time = f"{d.day}.{d.month}.{d.year} {d.hour}:{d.minute}"
        createNote(b,c,time)
    elif a == 2:
        showNotes()
        idx = int(input("Lütfen yukarıdan düzenlemek istediğiniz satırın ID numarasını giriniz: "))
        rowx = input("Lütfen yeni title verisini giriniz: ")
        notex = input("Lütfen yeni note verisini giriniz: ")
        editNote(rowx,notex,idx)
    elif a == 3:
        showNotes()
        xyz = int(input("Lütfen yukarıdan silmek istediğiniz satırın ID'sini giriniz: "))
        deleteNote(xyz)
    elif a == 4:
        showNotes()
    elif a == 5:
        mydb.close()
        break
    else:
        print("Yanlış giriş yaptınız.")