"""
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')

"""

"""
Inheritance konusu..
"""
class Person(object):


    def __init__(self, name, id):
        self.name = name
        self.id = id
        print("person classına hoş geldiniz.")

    def Display(self):
        print(self.name, self.id)

class Emp(Person):

    def Print(self):
        print("Emp class called")


Emp_details = Emp("Manyak", 103)

Emp_details.Display()

Emp_details.Print()



print("\n")



class Person(object):


    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


class Employee(Person):


    def isEmployee(self):
        return True

emp = Person("Geek1")
print(emp.getName(), emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(), emp.isEmployee())


print("\n")


"""

işte OVERRİDİNG olayı, b classındaki init üstteki a classındaki init yapıcı metodunu GEÇERSİZ KILIYOR.Ama unutulmaması
gereken şey, b classın yapıcı metodu a classın yapıcı metodunu geçersiz kılsa da b classını bir nesneye atayarak ve 
o nesneyle a CLASSINDAKİ METODLARA ULAŞABİLİRİZ.  

"""

class a():
    def __init__(self):
        print("Dogukan")

    def a(self):
        x=1
        y=2
        print(x/y)


class b(a):
    def __init__(self):
        print("batu")
    def c(self):
        print(9)
x = b()
x.a()


print("\n")



"""
Super.__init__ (veya üssteki class)__init__ metodlarını kullanarak overridingi iptal etme olayı. Yani alttaki yapıcı metod üstteki yapıcı metodu
geçersiz kılamıcak üstte yapıcı metod alttaki yapıcı metoda miras bırakmış olacak.d

"""
class Kullanici:
    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara

    def giris(self):
        print("Giriş Yapıldı")

    def cikis(self):
        print("Çıkış yapıldı")



class Akademisyen(Kullanici):
    def __init__(self,adi,soyadi,numara,dogum_tarihi):
        print("Akademisyen sınıfı fonksiyonu")
        super().__init__(adi,soyadi,numara)   #SUPER METODU KULLANIRKEN SELF EKLEMENE GEREK YOK AMA DİĞER YÖNTEMDE GEREK VAR.
        self.dugum_tarihi = dogum_tarihi


akademisyen = Akademisyen("Mustafa","Kaya",1236521,1997)

print("\n")



class Okul:
    def __init__(self,isim,soyisim,yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        print("Okul sınıfı çalıştı")

class Ogretmen(Okul):
    def __init__(self,isim,soyisim,yas,maas):
        Okul.__init__(self,isim,soyisim,yas)  # MUTLAKA SELF PARAMETRESİ KOYMALISIN.
        self.maas = maas
        print("öğretmen sınıfı çalıştı.")
    def info(self):
        print("{} {} {} yaşında bir öğretmendir".format(self.isim,self.soyisim,self.yas))

    def zam(self):
        print(self.maas)
a = Okul("dodo","src",22)
b = Ogretmen("ali","yılmaz",34,6500)
b.info()
b.zam()





"""
kapsülleme konusunu yazı ve örnekler açıkla.

"""




"""
Yani ebeveyn sınıftan çocuk sınıfına kalıtım (inheritance) yoluyla aktarılan ama çocuk sınıfında farklı bir şekilde kullanılan metotların yaptığı iş polimorfizmdir.
Kısaca çok biçimlilik adı üzerine aynı metodu kullanıp farklı çıktılar almak için kullanılır.
"""
class Personel:

    def zam(self):
        zam_oran = 0.1
        hesap = 100 + 100 * zam_oran
        print("Eleman: ", hesap, "TL")


class Doktor(Personel):

    def zam(self):
        zam_oran = 0.2
        hesap = 100 + 100 * zam_oran
        print("Doktor: ", hesap, "TL")

    def a(self):
        self.c = 8



class Hakim(Personel):

    def zam(self):
        zam_oran = 0.3
        hesap = 100 + 100 * zam_oran
        print("Hakim: ", hesap, "TL")


personel = Personel()

doktor_zam = Doktor()

hakim_zam = Hakim()

personel_listesi = [doktor_zam, hakim_zam]

for eleman in personel_listesi:
    eleman.zam()





