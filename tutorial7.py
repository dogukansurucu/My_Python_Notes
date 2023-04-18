liste = [1,2,3,4,5]
class a:
    x = "student"
    def __init__(self,liste):
        self.ad = 'Ali'
        self.ad1 = 805
        self.ad2 = liste
        print("Your'e welcome")
    def b(self):
        print(f'{self.ad} adlı {self.x}\'in numarası {self.c()}')
    def c(self):
        return self.ad1
    def e(self):
        i=0
        while i<5:
            i+=1
            if self.ad2[i-1]%2==1:
                print(f"{i} tek sayıdır.")
                continue
            else:
                print(f"{i} çift sayıdır.")
                continue
        print("İşlem sona erdi")

k = a(liste)
k.b()
print("\n")
print(k.x)
print(a.x)
print(k.__class__.x)
print("\n")
k.e()

print("\n")

class sinif:
    print("Hi")
    # Initializing
    def __init__(self):
        print('How are you')
    def a(self):
        print(5)
    print("I am fine!")

m = sinif()
m.a()

print("\n")
class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self,a):
        self.answer = self.first + self.second
        return f"{a}. İslem sonucu {self.answer} olmalı"

# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)
# creating second object of same class
obj2 = Addition(10, 20)
# perform Addition on obj1
print(obj1.calculate(1))
# perform Addition on obj2
print(obj2.calculate(2))
# display result of obj1
obj1.display()
# display result of obj2
obj2.display()

print("\n")

"""
Örnek : İşte yıkıcının basit bir örneği. del anahtar sözcüğünü kullanarak 'obj' nesnesinin tüm referanslarını sildik, 
bu nedenle yıkıcı otomatik olarak çağrılır.
 
Yani k = Employee() diyerek print('Employee crated.') ifadesini yazdırmış olduk.
Daha sonra del k diyerek Employee sınıfına ait tüm metod,attributes,instance'ları siliyor çünkü sınıfın referansını silmiş oluyoruz.
Böylelikte del k dedikten sonra k nesnesiyle hiçbir metod ve değişkeni çağıramayız. del k deyince de bize __del__ fonksiyonundaki
print ifadesini yazdırır. Bu arada __del__ fonksiyonundaki print() in yazdırılması için illa del komutuna gerek yoktur.
del komutuyla sınıfın referansını silmesek de sınıfı çağırdığımızda, class seviyesinde olmayan bir print ifadesi ve
yapıcı metoddaki print gibi sınıftaki tüm işlemler bittikten sonra çıktı olarak yazdırır.

"""
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')
    def a(self):
        print(5)

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted.')


k = Employee()
del k
"""
print(k.a()) 

output:  NameError: name 'k' is not defined
"""

print("\n")



"""
Aşağıdaki iki örneği inceleyecek olursak:

1.class örneği: Employee5 adında bir sınıfımız var. Ve bu sınıfta bir yapıcı metod bir normal bir metod bir tane de
 __del__(self) (yıkıcı metod) vardır. Şimdi biz bu sınıfı çağırdığımızda yapıcı metod ve class seviyesinde olmayan kısımdaki
 print ifadeleri yazdırılır. Daha sonra bir nesnenin metodu çağrıldıysa o fonksiyondaki işlemler yazdırılır. Ki bizim classımızda
 a fonksiyonu nesne tarafından çağrılmıyor. Daha sonra __del__(self) fonksiyonu yazdırılır.


2.class örneği: 1.örnekte anlattığım mantık bu örnekte de geçerli olduğundan tekrara düşmemek istiyorum.

"""

class Employee5:
    print("entrance")
    # Initializing
    def __init__(self):
        print('entrance2')
    def a(self):
        print(5)
    def __del__(self):
        print('entrance3')

Employee5()  # a=Employee5 de aynı sonucu verir.

print("\n")


# __del__(self) yıkıcı metodu, del ile nesnenin referansını silme işlemi olmasa bile nesne çağrıldığında yazdırılır.
class kemal:

    # Initializing
    def __init__(self):
        print('Employee created.')
    def e(self):
        print(5)
    def r(self):
        print(6)

    def __del__(self):
        print('dodo')


t = kemal()
t.e()
t.r()