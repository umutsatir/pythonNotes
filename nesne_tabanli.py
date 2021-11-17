## class
# Taslak gibi düşünebiliriz. Class, kopyaları oluşturularak kullanılıyor.
# Örn. list class'ı halihazırda bulunan bir classtır.

## instance (object)
# Class'ın kopyasıdır.

class Person:
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # class attributes
        address = "no information" # constructor içerisinde sabit olarak kalır, isteyince değiştirebiliriz.
        
        # object attributes
        self.name = name
        self.year = year
        print("init metodu çalıştı.") # init metodu name ve year değerleri girildiği gibi direk çalışır.

        # instance methods (oluşturduğumuz objelere hizmet eder)
    def intro(self):
        print("Hello there, I am " + self.name)
        
    def calculateAge(self):
        return 2021 - self.year

p1 = Person("umut", 2003)
p1.address = "information"
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")

p1.intro() # Hello there, I am umut çıktısı alırız.

# update etme
p1.name = "ahmet"







class Circle:
    # class attribute
    pi = 3.14

    def __init__(self, yaricap = 1) -> None:
        self.yaricap = yaricap
    
    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap
    
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1 = Circle() # yaricap = 1 kabul eder.
c2 = Circle(5) # yarıçap 5 alınır.
print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")








## Inheritence (Kalıtım): Miras alma ##

# Mesela Person diye bir classımız varsa ve bu classın metotlarının aynısının başka classta da olmasını istersek
# kalıtımı kullanabiliriz.

class Insan():
    def __init__(self, fname, lname) -> None:
        self.firstname = fname
        self.lastname = lname
        print("Person created!")

    def who_am_i(self):
        print("I am a person.")


class Student(Insan):
    def __init__(self, fname, lname) -> None:
        Insan.__init__(self, fname, lname) # Normalde Studentteki init diğerini ezer ancak insan classındaki initin de çalışmasını istersek
        # üstteki satırı kullanmalıyız.
        print("Student created!")
    # eğer bu classta da who_am_i metodu açarsak diğerini ezer ve studentte farklı çalıştırır. Buna
    # override denir.
    def who_am_i(self):
        print("I am a student.")


class Teacher(Insan):
    def __init__(self, fname, lname, branch) -> None:
        super().__init__(fname, lname) # Insan.__init__(self) ile aynı manaya gelir.
        self.branch = branch

    def who_am_i(self):
        print("I am a teacher.")


insan1 = Insan()
s1 = Student() # hem student hem insan classındaki initi çalıştırır.
t1 = Teacher("Serkan", "Yılmaz", "Math")

print(insan1.firstname + " " + insan1.lastname)
print(s1.firstname + " " + s1.lastname)

insan1.who_am_i()
s1.who_am_i() # override ile insan classındaki who_am_i metodunu ezer.
t1.who_am_i() # override






## Özel Metotlar ##

class Movie():
    def __init__(self, title, director, duration) -> None:
        self.title = title
        self.director = director
        self.duration = duration
        print("movie objesi oluşturuldu.")
     
    def __str__(self) -> str:
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("film objesi silindi.")

m = Movie("film adı", "yönetmen adı", 120)
print(str(m)) # str metoduyla yazdırırsak tanımladığımız metot çalıştırılır.
print(len(m)) # normalde len metodu m ile çalışmıyordu fakat tanımladığımız için çalıştı.
del m # objeyi silmeden önce del metodunu çalıştırır.
