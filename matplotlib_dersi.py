import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y, "or") # matplotlib sitesinden bakarak kodlandırmayı öğrenebiliriz. Ör: or=daireli kırmızı çizgi
plt.axis([0,6,0,20]) # x eksenini 0,6 arasında, y eksenini 0,20 arasında gösterir.
plt.title("Grafik Başlığı")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()


z = np.linspace(0,2,100)
plt.plot(z, z, label="linear")
plt.plot(z, z**2, label="quadratic")
plt.plot(z, z**3, label="cubic")
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("simple plot")
plt.legend() # tek grafik üzerinde 3 çizgiyi gösterdik.
plt.show()


fig, axs = plt.subplots(2,2) # aynı ekranda 2x2 yani 4 tane grafik göstermemize yarar.
axs[0,0].plot(z,z,color="red")
axs[1,0].plot(z,z**2,color="green")
axs[1,1].plot(z,z**3,color="blue")
axs[0,1].plot(z,z**4,color="yellow")
fig.suptitle("grafik başlığı")
plt.tight_layout() # grafikler arası yazıların karışmasını engeller. Aralarını açar.
plt.show()



## GRAFİK TÜRLERİ ##

yil = [2011,2012,2013,2014,2015]
oyuncu1 = [8,10,12,7,9]
oyuncu2 = [7,12,5,15,21]
oyuncu3 = [18,20,22,25,19]

# stack plot grafik türü
# bu grafik türünde çizginin altı taralı oluyor.
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")
plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
plt.title("Yıllara Göre Atılan Goller")
plt.legend()
plt.show()

# pasta grafiği
goal_types = "penaltı","kaleye atılan şut","serbest vuruş"

goals = [12,35,7]
colors = ["y","r","b"]
plt.pie(goals, labels=goal_types, colors=colors, shadow=True, explode=(0.05,0.05,0.05), autopct="%1.1f%%") 
# üstteki özelleştirmeleri matplotlib internet sayfasından bulabiliriz.
plt.show()

# bar grafiği
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW")
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi")
plt.legend()
plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")
plt.show()

# histogram grafiği
yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8) 
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.title("Histogram")
plt.show()