# ad = "Dogukan Surucu"
# print(ad[2.5]) #typerror

# ad2 = int(input("değer: "))
# deger: 5.5   #valuerror


# print("a"+5) --> TypeError
# print("ali"e) --> SyntaxError
# print(5/0) --> ZeroDivisonError
# print(int('k')) --> ValueError
# print(k) --> NameError

"""
Blok try, hatalar için bir kod bloğunu test etmenizi sağlar.

Blok except, hatayı işlemenizi sağlar.

Blok else, hata olmadığında kod yürütmenizi sağlar.

Blok finally, try- ve hariç tutma bloklarının sonucundan bağımsız olarak kod yürütmenizi sağlar.
"""

a = {'a':1, 'b':2}
try:
    print(a['c'])

    print(5+'c')

    # Throws error since there are only 3 elements in array

except TypeError:
    print("A")
except KeyError :
    print("B")
else:
    print("Hata oluşmadan try bloğu çalıştı.")
finally:
    print("İşlem sona ermiştir.")



def fun(a):
    if a < 4:
        b = a / (a - 3)

    print("Value of b = ", b)

try:
    fun(5)
    fun(3)

except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")



try:
    x= int(input("sayi 1: "))
    y= int(input("sayi 2: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e: #birden fazla istisnayı işlemek için parantez içine alman gerekiyor.
    print("yanlış bilgi girdiniz.",e)



def example2():

    try:
        print(5/0)
    except ZeroDivisionError as e:  # as diyerek istinanın nedenini bir e aracısına göndermiş oluyoruz.
        print("Couldn't parse:", e)


example2()


"""
Yaygın İstisna Hatalarından bazıları şunlardır: 
 

IOError: dosya açılamıyorsa
KeyboardInterrupt: kullanıcı tarafından gereksiz bir tuşa basıldığında
ValueError: Yerleşik işlev yanlış bir bağımsız değişken aldığında
EOFError: Dosya Sonu herhangi bir veri okumadan vurulursa
ImportError: modülü bulamazsa
IndexError: Bir liste/string uzunluğunun dışında bir index araması yapıldığında.
AssertionError:	Assert deyimi başarısız olduğunda oluşur
AttributeError:	Bir class nesnesinin öznitelik ataması başarısız olduğunda oluşur.
FileNotFoundError: dosya bulunamadığında oluşur.	
KeyError: Sözlüğün anahtarı bulunamadığında oluşur.
NameError: Değişken tanımlanmadığında ortaya çıkar.
MemoryError: Bir programın belleği dolduğunda oluşur.
TypeError: Bir işlev ve işlem yanlış tipte uygulandığında oluşur.

vs vs

https://docs.python.org/2/library/exceptions.html#exception-hierarchy
https://www.geeksforgeeks.org/built-exceptions-python/

"""


"""
TypeError Exception
"""
"""

geeky_list = ["geek", "GeeksforGeeks", "geeky", "geekgod"]
index = "1"
print(geeky_list[index])

output: TypeError: list indices must be integers or slices, not str

"""

geeky_list = ["Geeky", "GeeksforGeeks", "SuperGeek", "Geek"]
indices = [0, 1, "2", 3]
for i in range(len(indices)):
    try:
        print(geeky_list[indices[i]])
    except TypeError:
        print("TypeError: Check list of indices")




"""
KeyboardInterrupt Except

bizden input değeri istediğinde değeri girmeden kodu durdurursak
KeyboardInterrupt Except istisnasıyla karşı karşıya kalıyoruz.
"""
try:
    var = input()
    print ('Use KeyboardInterrupt')
except KeyboardInterrupt:
    print('KeyboardInterrupt exception is caught')
else:
    print('No exceptions thrown')



"""
AssertionError
"""
try:
    x = 10
    y = int(input("sayıyı giriniz: "))
    assert y%2== 0, "Girilen sayı çift sayı değildir."
    print(x/y)

except (AssertionError,ZeroDivisionError) as e:
    print(e)




def KelvinToFahrenheit(Temp):
    try:
        assert (Temp >= 0), "girilen sıcaklık değeri 0 dan küçüktür."
        return ((Temp - 273) * 1.8) + 32
    except AssertionError as ex:
        print(ex)

print(KelvinToFahrenheit(270))
print(int(KelvinToFahrenheit(510.78)))
KelvinToFahrenheit(-10)

"""
üstteki fonksiyonun daha kullanışlı hali
"""
i=0
while i<3:
    try:
        a = float(input(f"{i+1}.sayı: "))
        assert (a >= 0),"Given temperature is colder than absolute zero"
        print((a - float(273) * 1.8) + float(32))
    except AssertionError as ex:
        print(ex)
    i += 1




"""
AttributeError except(istisna) türü


class a():
    def c(self):
        print(5)


k = a()
k.b


output: 'a' object has no attribute 'b'

"""









"""
create error object: Raise

ÖNEMLİ: Mesela bir While döngüsünde döngü koşulu sağladıkça yani döndükçe,try-excep ile hata yakalasa bile program sonlanmaz.
Oysaki bir döngü veya başka bir yerde "raise Exception(".....")" bloğu olursa, döngü isterse sürekli dönsün eğer bu blokla karşılaşırsak
hata mesajı fırlatır ve program(kod) çalışmayı durdurur.
"""


"""
x = -1

if x < 0:
  raise Exception("x değeri minimum 0 olmalıdır.")
  

output: 

Exception: x değeri minimum 0 olmalıdır.

"""


"""
y = "hello"

if not type(y) is int:        # operatör önceliğine dikkat edersen is ile başlayacağını bilirsin yoksa yanlış yol izlersin.
  raise TypeError("Only integers are allowed")
  
output: 

TypeError: Only integers are allowed
"""



try:
    amount = 1999
    if amount < 2999:

        # raise the ValueError
        raise ValueError("please add money in your account")
    else:
        print("You are eligible to purchase DSA Self Paced course")

# if false then raise the value error
except ValueError as e:
    print(e)


"""
NZEC hatası:

Adından da anlaşılacağı gibi NZEC (sıfır olmayan çıkış kodu), kodunuz 0 döndüremediğinde oluşur. 
Bir kod 0 döndürdüğünde, başarılı bir şekilde yürütüldüğü anlamına gelir, 
aksi takdirde hatanın türüne bağlı olarak başka bir sayı döndürür.
"""