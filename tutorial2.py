"""   DEĞİŞKEN TANIMLAMA VE KURALLARI
    -------------------------------------

Python programlama dilinde değişkenlere değer atamak için = (eşittir) ifadesi kullanılmaktadır. Python programlama dilinde değişken tanımlamak için
herhangi bir ifade kullanmaya gerek yoktur. Sadece değişken ismi verilmekte ve bu değişken ismine değer = ifadesi ile ataması yapılmaktadır. 
Python programlama dilinde değişkenleri tanımladıktan sonra ; (noktalı virgül) koymaya gerek yoktur. Diğer programlama dillerindeki gibi ; 
(noktalı virgül) eksikliğinden programımızın çalışmama durumu olmayacaktır.


Diğer programlama dillerinde olduğu gibi python programlama dilinde de değişken isimlendirme kuralları bulunmaktadır.
Bu kurallar :

- Python programlama dilinde değişken tanımlarkenn (ı, Ş,İ, Ğ, ğ, ş, ü, Ü, ö, Ö, ç, Ç ) Türkçe karakterleri kullanmamamız gerekmektedir.
- Değişkenler isimlendirilirken harfler veya _ (alt tire) ile başlamalıdır. Değişkenler rakam ile başlayamaz. Örneğin: _sayi veya sayi şeklinde tanımlanabilir.
- Değişken isimlendirilirken her programlama diline ait anahtar kelimeler bulunmaktadır. Bu anahtar kelimeler değişken isimlendirirken kullanılmamaktadır.
- Değişkenler tanımlanırken büyük küçük harfe dikkat edilmelidir. Örneğin: sayi ile Sayi değişkenleri birbirinden farklıdır.
- Değişken isimlendirirken değişkenler birbirinden farklı ve benzersiz olmaları gerekmektedir.
- Sabit tanımlarken büyük harfle yazın.
- Asla özel sembolleri kullanmayın !, @, #, $, %, vb.

"""

x = 10
y = 20
z = x + y

print(x)  # 10
print(y)  # 20
print(z)  # 30
# print(k)  # NameError: name 'k' is not defined


name = "Çınar"
surname = 'Turan'
sad = """Kemal"""
print(name,surname,sad)
print(type(name)==type(sad))

a = '50'           # sözel olarak 50 değeri tanımladık
b = "50"           # sözel (string) olarak 50 değeri tanımladık.
print(a + b)       # a + b' nin sonucu 5050 olur.

a = 50
b = 50
print(a + b)

x = 10   # x içinde 10 değeri var.
y = 20   # y içinde 20 değeri var.
x = 30   # x içinde bulunan 10 değeri silinir ve 30 değeri aktarılır.
x += 10  # x değişkeni üzerine 10 değerini eklemiş oluruz ve 40 olur.

print(x)


x = 1             # int
t = 2.3           # float
name = 'Çınar'    # string
isStudent = True  # bool

print(type(x))         # <class 'int'>
print(type(t))         # <class 'float'>
print(type(name))      # <class 'string'>
print(type(isStudent)) # <class 'bool'>

x, p, name, isStudent = 1, 2.3, 'Çınar', True





""" 

       PYTHON'da VERİ TİPİ DÖNÜŞÜMLLERİ 
      -------------------------------------  
                                          
"""

w = input('1.sayı: ')
e = input('2.sayı: ')
k = 5.47

toplam = w + e
print(toplam)

print(type(x))    # <class 'str'>
print(type(y))    # <class 'str'>

toplam1 = int(w) + int(e) + int(k)
print(toplam1)

toplam2 = float(x) + float(y)
print(toplam2)


o = 10
c = 20.5
isOnline = True


# int veri türünden float veri türüne,
o = float(o)     # int to float
print(o)         # 10.0
print(type(o))   # <class 'float'>

# float veri türünden int veri türüne,
r = int(c)     # float to int
print(r)       # 20
print(type(r)) # <class 'int'>

# int veri türünden string veri türüne,
result = str(o) + str(c)   # int to string
print(result)              # 1020.5
print(type(result))        # <class 'str'>

# bool veri türünden string veri türüne,
isOnline = str(isOnline)   # bool to str
print(isOnline)            # True (string bir kelime)
print(type(isOnline))      # <class 'str'>

isOnline1 = False
# bool veri türünden int veri türüne,
isOnline1 = int(isOnline1)   # bool to int
print(isOnline1)            # 1 (True için 1, False için 0)
print(type(isOnline1))      # <class 'int'>


"""
    STRİNG VERİ TİPİ
  ---------------------
Dize(string), harflerin, sayıların ve özel karakterlerin birleşimi olabilen bir karakter dizisidir. Python'da tek tırnak, çift tırnak ve hatta üçlü tırnak kullanılarak bildirilebilir. 
Bu alıntılar bir dizgenin parçası değildir, sadece dizgenin başlangıcını ve bitişini tanımlarlar. String'ler değişmezdir, yani değiştirilemezler. 
String'in her bir öğesine indeksleme veya dilimleme işlemleri kullanılarak erişilebilir.
  
"""
# Assigning string to a variable
a = 'This is a string'
print(a)
b = "This is a string"
print(b)
c = '''This is a string'''
print(c)

"""
  ----- Python String'deki karakterlere erişme ----

Python'da, bir Dizenin tek tek karakterlerine Dizin Oluşturma yöntemi kullanılarak erişilebilir. 
İndeksleme, negatif adres referanslarının Dizenin arkasındaki karakterlere erişmesine izin verir, örneğin -1 son karaktere, -2 ikinci son karaktere vb. Atıfta bulunur.

Aralığın dışındaki bir dizine erişirken bir IndexError'a neden olur. Yalnızca Tamsayıların dizin, kayan nokta veya TypeError'a neden olacak diğer türler olarak geçirilmesine izin verilir.
"""

String1 = "GeeksForGeeks"

print("First character of String is: ",String1[0])
print("Last character of String is: ",String1[-1])


"""
----- Bir Python String'ini Tersine Çevirmek ----

1.yol: Bir diziden Karakterlere Erişme ile onları tersine çevirebiliriz. [::-1] yazarak bir diziyi ters çevirebiliriz ve dizi tersine çevrilir.

2.yol: join() ve reversed() işlevi kullanarak bir dizeyi tersine çevirebiliriz .


"""


gfg = "geeksforgeeks"

#1

print(gfg[::-1])

#2

gfg = "".join(reversed(gfg))
print(gfg)

ad = "geeksforgeeks"
print("".join(list(reversed(ad))))



"""
----- String Dilimleme ----

String'deki bir dizi karaktere erişmek için dilimleme yöntemi kullanılır. Bir String dilimleme, bir Dilimleme operatörü (iki nokta üst üste) kullanılarak yapılır. 


"""


# Creating a String
String2 = "GeeksForGeeks"
print("Initial String: ")
print(String2)

# Printing 3rd to 12th character
print("\nSlicing characters from 3-12: ")
print(String2[3:12])

# Printing characters between
# 3rd and 2nd last character
print("\nSlicing characters between " + "3rd and 2nd last character: ")
print(String2[3:-2])


"""
----- Python String'de Silme ve Güncelleme----

Python'da bir String karakterlerin güncellenmesine veya silinmesine izin verilmez. Bu, öğe ataması veya bir Dizeden öğe silme desteklenmediğinden bir hataya neden olur. 
Yerleşik bir del anahtar sözcüğünün kullanılmasıyla tüm Dizenin silinmesi mümkün olsa da. Bunun nedeni, stringlerin değişmez olmasıdır, 
bu nedenle bir Stringin öğeleri atandıktan sonra değiştirilemez. Aynı ada yalnızca yeni stringler atanabilir.



Tüm String ifadenin Silinmesi:

Stringin tamamının silinmesi, del anahtar sözcüğünün kullanılmasıyla mümkündür. Ayrıca, dizeyi yazdırmaya çalışırsak, 
bu bir hata oluşturur çünkü Dize silinir ve yazdırılamaz.  


ifade  = "Hello, I'm a Geek"
print(ifade)

del ifade
print("\nDeleting entire String: ")
print(String1)

output: NameError: 'String1' adı tanımlı değil 
"""


# Python Program to Update
# character of a String

String3 = "Hello, I'm a Geek"

list1 = list(String3)
list1[2] = 'p'
String4 = ''.join(list1)
print("\nUpdating character at 2nd Index: ",String4)


"""
----- Python String'de String Formatlama----

format() yöntemi, belirtilen değerleri biçimlendirir ve bunları dizenin yer tutucusunun içine ekler.
Yer tutucu, süslü parantez kullanılarak tanımlanır: {}

"""

name1 = 'John'
age = 20

print("Hello I'm {}, my age is {}".format(name1, age))
print("Hello I'm {1}, my age is {0}".format(name1, age))

a = 5
b = 10
print(f'Five plus ten is {a + b} and not {2 * (a + b)}.')



# a.b olsun a dediğimiz sayının  kaplayacağı boşluk sayısını söyler.
# b dediğimiz ise sayının tam kısmı ile ondalık kısmı birlikte toplam kaç rakam olacağını söylüyor.
# yuvarlama olayı unutulmamalı.
# ' .f  'de . dan sonraki rakam kadar sayının ondalık kısmı kesilir.


sayi = 2245.7567

print("sayımız: {ad:9.7}".format(ad = sayi))


sayi_2 = 5.7567245

print("sayımız: {ad:1.4}".format(ad = sayi_2))


k = 3.1415926

print(f"{k:.2f}")
# '3.14'

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

sayi_3 = 8.7596

print("sayımız: {ad:1.2f}".format(ad = sayi_3))
# 1.2f deki f olunca b kuralının bir anlamı olmuyor.Ondalık kısmından 2 sayı al demek istiyor.

name2 = 'Pete'
print('Hello %s' % name)
# "Hello Pete"

num = 5
print('I have %d apples' % num)
# "I have 5 apples"


"""
string formatlama operatörleri hakkında daha fazla bilgi için;  

https://www.w3schools.com/python/ref_string_format.asp
"""


"""
----- String Metodları ----

   Yöntem                   Açıklaması

1) capitalize(): İlk karakteri büyük harfe dönüştürür

2) casefold(): Dizeyi küçük harfe dönüştürür

3) center(): Ortalanmış bir dize döndürür

4) count(): Bir dizede belirtilen bir değerin kaç kez oluştuğunu döndürür.

count(), yürütme için yalnızca tek bir parametre gerektirir. Ancak, isteğe bağlı iki parametresi de vardır:
substring - sayısı bulunacak dize.
start (İsteğe bağlı) - aramanın başladığı dize içinde başlangıç dizini.
end (İsteğe bağlı) - aramanın bittiği dize içindeki bitiş dizini.

5) encode(): Dizenin kodlanmış bir sürümünü döndürür

6) endswith():  belirtilen değerle biterse true değerini döndürür

7) expandtabs(): Dizenin sekme boyutunu ayarlar

8) find(): Dizeyi belirli bir değer için arar ve bulunduğu yerin konumunu döndürür.Aranan karakter dize içinde yoksa -1 değer döndürür.

9) format(): Bir dizede belirtilen değerleri biçimlendirir

10) format_map(): Bir dizede belirtilen değerleri biçimlendirir

11) ındex(): Dizeyi belirli bir değer için arar ve bulunduğu yerin konumunu döndürür. Eğer aranan karakter dizede yoksa ValueError hatas döndürür.

12) isalnum(): isalnum() yöntemi, tüm karakterler alfanümerik, yani alfabe harfi (a-z) ve sayılar (0-9) ise True değerini döndürür.
!!! Boşluk bir alfa sayısal(alfanümerik) karakter değildir.

isalpha(): dizedeki tüm karakterler alfabedeyse  True değerini döndürür

ısascii(): dizedeki tüm karakterler ascıı karakteriyse  True değerini döndürür

isdecimal(): dizedeki tüm karakterler ondalık ise True değerini döndürür

isdigit(): dizedeki tüm karakterler rakam ise  True değerini döndürür

isidentifier(): dize bir tanımlayıcı ise True değerini döndürür

islower(): dizedeki tüm karakterler küçük harfse True değerini döndürür

ısnumeric(): dizedeki tüm karakterler sayısalsa, True değerini döndürür

isprintable(): dizedeki tüm karakterler yazdırılabilirse  True değerini döndürür

isspace(): tüm karakterler boşluk ise isspace() True değerini döndürür

istitle(): bir başlığın kurallarına uyuyorsa istitle() True değerini döndürür

isupper(): tüm karakterler büyük harfse True değerini döndürür

join(): yinelenebilir bir öğenin öğelerini bir dizeye dönüştürür

ljust(): Dizenin sola yaslanmış bir sürümünü döndürür

lower(): Bir dizeyi küçük harfe dönüştürür

lstrip(): Dizenin sol trim sürümünü döndürür

maketrans(): Çevirilerde kullanılacak bir çeviri tablosu döndürür

partition(): dizenin üç bölüme ayrıldığı bir demet döndürür

replace(): Belirtilen değerin belirtilen değerle değiştirildiği bir dize döndürür

rfind(): Dizeyi belirli bir değer için arar ve bulunduğu yerin son konumunu döndürür

rindex(): Dizeyi belirli bir değer için arar ve bulunduğu yerin son konumunu döndürür

rjust(): Dizenin sağa yaslanmış bir sürümünü döndürür

rpartition():, dizenin üç bölüme ayrıldığı bir demet döndürür

rsplit(): Dizeyi belirtilen ayırıcıya böler ve bir liste döndürür

rstrip(): Dizenin sağ kırpma sürümünü döndürür

split(): Dizeyi belirtilen ayırıcıda böler ve bir liste döndürür

splitlines(): Dizeyi satır sonlarına böler ve bir liste döndürür

startswith(): dize belirtilen değerle başlarsa true değerini döndürür

strip(): dizenin kırpılmış bir sürümünü döndürür

swapcase(): Vakaları değiştirir, küçük harf büyük harf olur ve bunun tersi de geçerlidir

title(): kelimenin ilk karakterini büyük harfe dönüştürür

translate(): Çevrilmiş bir dize döndürür

upper(): Bir dizeyi büyük harfe dönüştürür

zfill(): Dizeyi başlangıçta belirtilen sayıda 0 değerle doldurur


Metodlarla ilgili daha fazla bilgi ve örnek için;   https://www.w3schools.com/python/python_ref_string.asp
                                                    https://www.programiz.com/python-programming/methods/string


"""


x = 'seißen'

print(x.lower())
print(x.casefold())


text = 'groß'

# convert text to lowercase using casefold()
print('Using casefold():', text.casefold())

# convert text to lowercase using lower()
print('Using lower():', text.lower())

str = "My salary is 7000"
print(str.isalnum())

# Alfabe dışı bir bir karakterden (rakam,sembol vs) sonraki ilk harfin büyük harfe dönüştürüldüğünü unutmayın.

k = 'd7odo d7k5 kemal '
print(k.title())

""" 

Yöntem find() , belirtilen değerin ilk geçtiği yeri bulur.

find() değer bulunamazsa yöntem -1 değerini döndürür .

Yöntem find(), index() ile hemen hemen aynıdır. Tek fark, index() değer bulunmazsa bir istisna oluşturmasıdır.


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))
print(txt.find("e"))


output: 
        -1

Traceback (most recent call last):
  File "demo_ref_string_find_vs_index.py", line 4 in <module>
    print(txt.index("q"))
ValueError: substring not found

         1

"""

txt = "H\te\tl\tl\to"

print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(6))
print(txt.expandtabs(10))





"""
      LİST VERİ TİPİ
    --------------------- 
      
Python Listeleri, diğer dillerde bildirilen dinamik olarak boyutlandırılmış diziler gibidir (C++'da vektör ve Java'da ArrayList). 
Basit bir dille, bir list, [] içine alınmış ve virgülle ayrılmış bir şeyler koleksiyonudur.       
      
Listeler, Python dilinin ayrılmaz bir parçası olan en basit kaplardır. Listelerin her zaman homojen olması gerekmez, 
bu da onu Python'daki en güçlü araç yapar. Tek bir liste, Tamsayılar, Dizeler ve Nesneler gibi DataType'ları içerebilir.

Liste öğeleri sıralıdır, değiştirilebilir ve yinelenen değerlere izin verir.
"""
Var = ["Geeks", "for", "Geeks"]
print(Var)



"""
    ----- Python'da Liste Oluşturma ----
    
Python'daki listeler, diziyi köşeli parantezler [] içine yerleştirerek oluşturulabilir. Setlerden farklı olarak , bir 
listenin oluşturulması için yerleşik bir işleve ihtiyacı yoktur. 

Not: sets(küme)'lerden farklı olarak, liste değiştirilebilir öğeler içerebilir.Sets'lerin kendisi değiştirilebilir.
Yani öge eklenip çıkarılabilir.Ama öge değişikliği olmaz.

Bir liste, farklı konumlarıyla yinelenen değerler içerebilir ve bu nedenle, liste oluşturma sırasında 
birden çok farklı veya yinelenen değer bir sıra olarak iletilebilir.
"""


List1 = []
print("Blank List: ")
print(List1)

List2 = [10, 20, 14]
print("\nList of numbers: ")
print(List2)

List3 = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List3[0])
print(List3[2])

List4 = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List4)

List5 = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List5)

"""
   ----- Listeden öğelere erişme  ----
   
Liste öğelerine erişmek için dizin numarasına bakın. Bir listedeki bir öğeye erişmek için indeks operatörünü [] kullanın. 
Dizin bir tamsayı olmalıdır. İç içe geçmiş listelere, iç içe indeksleme kullanılarak erişilir.  

Python'da negatif dizi indeksleri, dizinin sonundaki konumları temsil eder. Liste[len(Liste)-3]'deki gibi ofseti hesaplamak zorunda kalmak yerine,
sadece Liste[-3] yazmak yeterlidir.Negatif indeksleme sondan başlamak anlamına gelir, -1 son öğeyi ifade eder, -2 sondan ikinci öğeyi ifade eder, vb. 
   
"""


List6 = ["Geeks", "For", "Geeks"]

print("Accessing a element from the list")
print(List6[0])
print(List6[2])


List7 = [['Geeks', 'For'], ['Geeks']]

print("Accessing a element from a Multi-Dimensional list")
print(List7[0][1])
print(List7[1][0])


List8 = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

print(List8[-1])
print(List8[-3])

"""
  -----Python listesinin boyutunu alma----
  
  
Python len(), listenin uzunluğunu almak için kullanılır.


"""


List9 = []
print(len(List9))

List10 = [10, 20, 14]
print(len(List10))

l = [None] * 10
print(len(l))


l = ["A"] * 10
print(l)

"""
  -----Bir Python Listesinin Girdisini Alma----

Bir eleman listesinin girdisini string, integer, float, vs. olarak alabiliriz. Ancak varsayılan olan bir string'dir.

"""

# input size of the list
n = int(input("Enter the size of list : "))
# store integers in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst)

"""
  -----Bir Python Listesine Öğeler Ekleme----

Yöntem 1: append() yöntemini kullanma:
Öğeler, yerleşik append() işlevi kullanılarak Listeye eklenebilir. Append() yöntemi kullanılarak listeye tek seferde yalnızca bir öğe eklenebilir, 
append() yöntemi ile birden fazla öğe eklemek için döngüler kullanılır. Demetler değişmez olduklarından, append yöntemi kullanılarak listeye eklenebilirler. 
Kümelerden farklı olarak, append() yöntemi kullanılarak mevcut listeye Listeler de eklenebilir.


Yöntem 2: insert() yöntemini kullanma:
Append() yöntemi sadece listenin sonuna eleman eklenmesi için çalışır, istenilen konuma eleman eklenmesi için 
insert() metodu kullanılır. Yalnızca bir bağımsız değişken alan append() yönteminin aksine, insert() yöntemi iki 
bağımsız değişken (konum, değer) gerektirir.


Yöntem 3: Extend() yöntemini kullanma:
Append() ve insert () yöntemlerinin dışında, öğelerin eklenmesi için bir yöntem daha vardır , bu yöntem aynı anda 
birden çok öğeyi listenin sonuna eklemek için kullanılır.


Not: append() ve extension() yöntemleri yalnızca sonuna öğe ekleyebilir.

"""

# Creating a List
List11 = []
print("Initial blank List: ")
print(List11)

# Addition of Elements
# in the List
List11.append(1)
List11.append(2)
List11.append(4)
print("\nList after Addition of Three elements: ")
print(List11)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List11.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List11)

# Adding Tuples to the List
List11.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List11)

# Addition of List to a List
List12 = ['For', 'Geeks']
List11.append(List12)
print("\nList after Addition of a List: ")
print(List11)




# Creating a List
List13 = [1,2,3,4]
print("Initial List: ")
print(List13)

# Addition of Element at
# specific Position
# (using Insert Method)
List13.insert(3, 12)
List13.insert(0, 'Geeks')
print("\nList after performing Insert Operation: ")
print(List13)




# Creating a List
List14 = [1, 2, 3, 4]
print("Initial List: ")
print(List14)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List14.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List14)




"""
   -----Bir Listeyi Tersine Çevirmek----

Python'da reverse() yöntemi kullanılarak bir liste tersine çevrilebilir.

"""

# Reversing a list
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

"""
  -----Öğeleri Listeden Kaldırma----

Yöntem 1: remove() yöntemini kullanma:

Öğeler, yerleşik remove() işlevi kullanılarak Listeden kaldırılabilir, ancak öğe listede yoksa bir Hata oluşur. 
Remove() yöntemi, bir seferde yalnızca bir öğeyi kaldırır, bir dizi öğeyi kaldırmak için yineleyici kullanılır. remove() yöntemi, belirtilen öğeyi kaldırır.

Not: Listedeki Kaldır yöntemi, aranan öğenin yalnızca ilk geçtiği yeri kaldıracaktır.


Yöntem 2: pop() yöntemini kullanma:
pop() işlevi, listeden bir öğeyi kaldırmak ve döndürmek için de kullanılabilir, ancak varsayılan olarak listenin 
yalnızca son öğesini kaldırır, bir öğeyi Listenin belirli bir konumundan kaldırmak için öğenin dizini iletilir 
pop() yöntemine bir argüman olarak.


"""

# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List15 = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List15)

# Removing elements from List
# using Remove() method
List15.remove(5)
List15.remove(6)
print("\nList after Removal of two elements: ")
print(List15)




# Creating a List
List16 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List16.remove(i)
print("\nList after Removing a range of elements: ")
print(List16)



List17 = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List17.pop()
print("\nList after popping an element: ")
print(List17)

# Removing element at a
# specific location from the
# Set using the pop() method
List17.pop(2)
print("\nList after popping a specific element: ")
print(List17)

"""
  -----Bir Listenin Dilimlenmesi----

Bir dilim kullanarak alt dizeleri ve alt listeleri alabiliriz. Python Listesinde, tüm listeyi tüm öğelerle yazdırmanın birden çok yolu vardır, 
ancak listeden belirli bir öğe aralığını yazdırmak için Dilimleme işlemini kullanırız . Listelerde iki nokta üst üste(:) kullanılarak dilimleme işlemi gerçekleştirilir. 

"""



# Creating a List
List18 = ['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

print("Initial List: ")
print(List18)

Sliced_List1 = List18[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_List1)

Sliced_List2 = List18[5:]
print("\nElements sliced from 5th "
	"element till the end: ")
print(Sliced_List2)

Sliced_List3 = List18[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_List3)





# Creating a List
List19 = ['G', 'E', 'E', 'K', 'S', 'F',
		'O', 'R', 'G', 'E', 'E', 'K', 'S']
print("Initial List: ")
print(List19)

# Print elements from beginning
# to a pre-defined point using Slice
Sliced_List4 = List19[:-6]
print("\nElements sliced till 6th element from last: ")
print(Sliced_List4)

# Print elements of a range
# using negative index List slicing
Sliced_List5 = List19[-6:-1]
print("\nElements sliced from index -6 to -1")
print(Sliced_List5)

# Printing elements in reverse
# using Slice operation
Sliced_List6 = List19[::-1]
print("\nPrinting List in reverse: ")
print(Sliced_List6)


"""
  -----List Comprehension----

Python List comprehensions, demetler, dizeler, diziler, listeler vb. diğer yinelenebilirlerden yeni listeler oluşturmak için kullanılır. 
Bir liste kavrayışı, her öğe için her öğe üzerinde yineleme yapmak üzere for döngüsüyle birlikte yürütülen ifadeyi içeren köşeli parantezlerden oluşur. 


Syntax:  newList = [ expression(element) for element in oldList if condition ]
"""


odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)



odd_square1 = []

for x in range(1, 11):
    if x % 2 == 1:
        odd_square1.append(x**2)

print(odd_square1)


"""
 -----List Metodları----

append(): Listenin sonuna bir öğe ekler
clear(): Tüm öğeleri listeden kaldırır
copy(): Listenin bir kopyasını döndürür
count(): Belirtilen değere sahip öğe sayısını döndürür
extend(): Bir listenin öğelerini (veya yinelenebilir öğeleri) geçerli listenin sonuna ekleyin
index(): Belirtilen değere sahip ilk öğenin dizinini döndürür
ınsert(): Belirtilen konuma bir öğe ekler
pop(): Öğeyi belirtilen konumda kaldırır
remove(): Belirtilen değere sahip ilk öğeyi kaldırır
reverse(): Listenin sırasını tersine çevirir
sort(): Listeyi sıralar

"""




""" 
        Tuple VERİ TİPİ
      --------------------- 
    
Tuple, bir listeye çok benzeyen bir Python nesneleri koleksiyonudur. Bir tuple'a depolanan değer dizisi herhangi bir türde olabilir ve bunlar tamsayılarla dizine alınır. 
Bir tuple değerleri sözdizimsel olarak 'virgül' ile ayrılır. Gerekli olmamakla birlikte, parantez içindeki değer dizisini kapatarak bir demet tanımlamak daha yaygındır.
Bu, Python tuple'ların daha kolay anlaşılmasına yardımcı olur.    
    
Tuple, sıralı ve değiştirilemez bir koleksiyondur .    
"""


"""
   -----Tuple Oluşturma----

Python'da, tuple'lar, veri dizisini gruplamak için parantez kullanılarak veya kullanılmadan 'virgül' ile ayrılmış bir değer dizisi yerleştirilerek oluşturulur.


"""

Tuple1 = ()
print("Initial empty Tuple: ")
print(Tuple1)


Tuple2 = ('Geeks', 'For')
print("\nTuple with the use of String: ")
print(Tuple2)

# Creating a Tuple with
# the use of list
list20 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list20))

# Creating a Tuple
# with the use of built-in function
Tuple3 = tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple3)



Tuple4 = (0, 1, 2, 3)
Tuple5 = ('python', 'geek')
Tuple6 = (Tuple4, Tuple5)
print("\nTuple with nested tuples: ")
print(Tuple6)


"""
  -----Tuple(demet)'lara Erişim----

Demetler değişmezdir ve genellikle paketten çıkarma veya indeksleme yoluyla (hatta adlandırılmış demetler durumunda özniteliğe göre) 
erişilen bir dizi heterojen öğe içerirler . Listeler değişkendir ve öğeleri genellikle homojendir ve liste üzerinden yinelenerek erişilir.
"""


Tuple7 = tuple("Geeks")
print("\nFirst element of Tuple: ")
print(Tuple7[0])



Tuple8 = ("Geeks", "For", "Geeks")


a, b, c = Tuple8
print("\nValues after unpacking: ")
print(a)
print(b)
print(c)



"""
  -----Tuple'ların birleştirilmesi----

Demet birleştirme, iki veya daha fazla Demetin birleştirilmesi işlemidir. Birleştirme '+' operatörü kullanılarak yapılır. 
Demetlerin birleştirilmesi her zaman orijinal demetin sonundan itibaren yapılır. Diğer aritmetik işlemler Tuples üzerinde geçerli değildir.


Not- Birleştirme ile sadece aynı veri türleri birleştirilebilir(list ile list, tuple ile tuple toplanabilir yani.), liste ve tuple birleştirilirse hata oluşur. 
"""

# Concatenation of tuples
Tuple9 = (0, 1, 2, 3)
Tuple10 = ('Geeks', 'For', 'Geeks')

Tuple11 = Tuple9 + Tuple10

print("Tuple 9: ")
print(Tuple9)

print("\nTuple10: ")
print(Tuple10)

print("\nTuples after Concatenation: ")
print(Tuple11)


"""
  -----Tuple Dilimleme----

Bir Tuple'ın dilimlenmesi, bir Tuple'dan belirli bir alt öğe aralığını veya dilimini almak için yapılır. Dilimleme ayrıca listelere ve dizilere de
yapılabilir. Bir listede indeksleme, tek bir öğenin getirilmesiyle sonuçlanırken, Dilimleme, bir dizi öğenin getirilmesine izin verir. 


"""


Tuple12 = tuple('GEEKS')

print("\nTuple after sequence of Element is reversed: ")
print(Tuple12[::-1])

print("\nPrinting elements between Range 4-9: ")
print(Tuple12[4:9])


aTuple = (1, 'Jhon', 1+3j)
print(type(aTuple[2:3]))

"""
  -----Tuple Silme----

Demetler değişmezdir ve dolayısıyla bir kısmının silinmesine izin vermezler. Demetin tamamı del() yöntemi kullanılarak silinir. 

Not- Silme işleminden sonra Tuple'ın yazdırılması bir Hataya neden olur. 




Tuple1 = (0, 1, 2, 3, 4)
del Tuple1

print(Tuple1)

output: NameError: 'Tuple1' adı tanımlanmadı
"""


"""
   -----Tuple Metodları----


count(), Belirli bir değerin bir demette kaç kez oluştuğunu döndürür
ındex(), grubu belirli bir değer için arar ve bulunduğu yerin konumunu döndürür
"""



"""

         Sets(Kümeler) VERİ TİPİ
     --------------------------------- 

Python'da bir Sets , tekrarlanabilir, değiştirilebilir ve yinelenen öğeleri olmayan sırasız bir veri türleri koleksiyonudur. 
Bir sets'deki elemanların sırası, çeşitli elemanlardan oluşabilmesine rağmen tanımsızdır. List yerine sets kullanmanın en büyük avantajı, kümede belirli bir öğenin bulunup bulunmadığını kontrol etmek için oldukça optimize edilmiş bir yönteme sahip olmasıdır.


Bir küme yalnızca benzersiz öğeler içerir, ancak küme oluşturma sırasında birden çok yinelenen değer de iletilebilir. 
Bir kümedeki elemanların sırası tanımsızdır ve değiştirilir değildir.(bu yüzden list ve dict kümede olmaz). 
Bir kümedeki öğelerin türünün aynı olması gerekmez, 
kümeye çeşitli karışık veri türü değerleri de aktarılabilir. 



"""




set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)


set2 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print("\nSet with the use of Mixed Values")
print(set2)



my_set = {1, 2, 3}

print(my_set)


aSet = {1, 'PYnative', ('abc', 'xyz'), True}
print(aSet)
#Öğe 1 olarak değerlendirildiğinden kümede zaten 1 var . Bildiğiniz gibi set yinelenen öğeye izin vermiyor.


"""
 ----- Sets'e Öğeler Ekleme ----

add() yöntemini kullanma:  

Yerleşik add() işlevi kullanılarak Set'e öğeler eklenebilir. add() yöntemi kullanılarak kümeye her seferinde yalnızca bir öğe eklenebilir,
add() yöntemi kullanılarak bir seferde birden çok öğe eklemek için döngüler kullanılır.


Not: Listeler bir sets'e öğeler olarak eklenemez yoksa hata verir, çünkü Listeler hashable değildir, oysa Tuple'lar eklenebilir, çünkü demetler değişmez ve dolayısıyla Hashable'dır. 
Kümenin kendisinin değiştirilebilir (mutable) olduğu doğrudur, ancak liste ve sözlük gibi değiştirilebilir nesneleri içeremez.


update() yöntemini kullanma:  

İki veya daha fazla öğenin eklenmesi için Update() yöntemi kullanılır. update() yöntemi, bağımsız değişkenleri olarak listeleri, 
dizeleri, demetleri ve diğer kümeleri kabul eder. Tüm bu durumlarda, yinelenen öğelerden kaçınılır.


Set öğelerine bir dizine başvurarak erişilemez, çünkü kümeler sırasızdır, öğelerin dizini yoktur. 
Ancak bir for döngüsü kullanarak set öğeleri arasında dolaşabilir veya in anahtar kelimesini kullanarak bir sette belirtilen bir değerin olup olmadığını sorabilirsiniz.
"""


# Creating a Set
set3 = set()
print("Initial blank Set: ")
print(set1)

# Adding element and tuple to the Set
set3.add(8)
set3.add(9)
set3.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set3)

# Adding elements to the Set
# using Iterator
for i in range(1, 6):
    set3.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set3)





"""
----- Bir Sets'e Erişme ----

Set öğelerine bir dizine başvurarak erişilemez, çünkü kümeler sırasızdır, öğelerin dizini yoktur. 
Ancak bir for döngüsü kullanarak set öğeleri arasında dolaşabilir veya in anahtar kelimesini kullanarak
bir sette belirtilen bir değerin olup olmadığını sorabilirsiniz.



"""

# Creating a set
set5 = set(["Geeks", "For", "Geeks"])
print("\nInitial set")
print(set5)

# Accessing element using
# for loop
print("\nElements of set: ")
for i in set5:
	print(i, end=" ")

# Checking the element
# using in keyword
print("Geeks" in set5)



"""
----- Sets Birleştirme ----

# sets'e ögeler eklemenin 2 yolu vardır. Ya union metodunu kullanarak 2 kümedeki ögeleri (yinelebilir olmayacak şekilde)
# bir sets'de toplayabilirsin. Ya da update metodunu kullanarak bi sets'e ımmutable veri tiplerini ekleyebilirsin(mesela list ve dict ekleyemezsin).
# iki sets {}+{} veya diğer veri türleriyle toplama işlemi olmaz.

"""
set7 = {"a","b","c"}
print(set7.update({"A","B",5}))
print(set7)

set5 = {"a","b","c"}
print(set5.update("d","e"))
print(set5)

set4= set([4, 5, (6, 7)])
set4.update([10, 11,True])
print("\nSet after Addition of elements using Update: ")
print(set4)


"""
----- Bir Sets'den Öge kaldırma ----

remove() ya da discard() yöntemi: 

Öğeler, yerleşik remove() işlevi kullanılarak Küme'den kaldırılabilir, 
ancak öğe kümede yoksa bir KeyError ortaya çıkar. KeyError olmayan bir kümeden öğeleri kaldırmak için, discard() işlevini kullanın, öğe kümede yoksa, değişmeden kalır.


pop() yöntemini kullanarak:

Pop() işlevi, kümeden rastgele bir öğeyi kaldırmak ve döndürmek için de kullanılabilir.
Küme sırasızsa, pop() işlevini kullanarak hangi öğenin açılacağını belirlemenin böyle bir yolu yoktur. 

sets.pop()  derken;
eğer sets değişken türde ögeler içeriyorsa rastgele bir eleman silebilir.
eğer sets aynı tipte ögeler varsa ilk öge silinir.


clear() yöntemini kullanarak:

Kümenin tüm elemanlarını kaldırmak için clear() fonksiyonu kullanılır. 

"""

# Creating a Set
set6 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set6)

# Removing elements from Set
# using Remove() method
set6.remove(5)
set6.remove(6)
print("\nSet after Removal of two elements: ")
print(set6)

# Removing elements from Set
# using Discard() method
set6.discard(8)
set6.discard(9)
print("\nSet after Discarding two elements: ")
print(set6)

# Removing elements from Set
# using iterator method
for i in range(1, 5):
    set6.remove(i)

print("\nSet after Removing a range of elements: ")
print(set6)




set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Initial Set: ")
print(set1)

# Removing element from the
# Set using the pop() method
set1.pop()
print("\nSet after popping an element: ")
print(set1)




set1 = set([1,2,3,4,5])
print("\n Initial set: ")
print(set1)

set1.clear()
print("\nSet after clearing all the elements: ")
print(set1)


"""
----- Frozensets ----

Python'daki Frozensets, yalnızca uygulandıkları fronzenset veya sets'leri etkilemeden sonuç üreten yöntemleri ve işleçleri destekleyen değişmez nesnelerdir. 
Bir sets'in öğeleri herhangi bir zamanda değiştirilebilirken, frozensets'in öğeleri oluşturulduktan sonra aynı kalır. 

Hiçbir parametre iletilmezse, boş bir frozenset döndürür.  
"""

# Creating a Set
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')

Fset1 = frozenset(String)
print("The FrozenSet is: ")
print(Fset1)

# To print Empty Frozen Set
# No parameter is passed
print("\nEmpty FrozenSet: ")
print(frozenset())

"""
----- Sets Metodları ----

add(): Kümeye bir öğe ekler.
clear(): Kümeden tüm öğeleri kaldırır.
copy(): Kümenin bir kopyasını döndürür.
difference(): iki veya daha fazla küme arasındaki farkı içeren bir küme döndürür.
difference_update(): Bu kümede belirtilen başka bir kümede de bulunan öğeleri kaldırır.
discard(): Belirtilen öğeyi kaldır.
ıntersection(): iki veya daha fazla kümenin kesişimi olan bir küme döndürür.
ıntersection_update(): Bu kümede belirtilen diğer kümelerde bulunmayan öğeleri kaldırır.
ısdisjoint(): iki kümenin kesişme noktası olup olmadığını döndürür.
ıssubset(): başka bir kümenin bu kümeyi içerip içermediğini döndürür.
ıssuperset(): Bu kümenin başka bir küme içerip içermediğini döndürür.
pop(): Kümeden bir öğeyi kaldırır.
remove(): Belirtilen öğeyi kaldırır.
symmetric_difference(): iki kümenin simetrik farklılıklarına sahip bir küme döndürür.
symmetric_difference_update(): bu kümeden ve diğer kümeden simetrik farklılıkları ekler.
union(): Kümeler birliğini içeren bir küme döndürür.
update(): Kümeyi başka bir kümeyle veya yinelenebilen başka bir kümeyle güncelleyin.

"""

"""
    Dictionary(Sözlük) VERİ TİPİ
  --------------------------------- 

Python'daki sözlük , bir öğe olarak yalnızca tek bir değer tutan diğer veri türlerinin aksine, bir harita gibi veri 
değerlerini depolamak için kullanılan bir anahtar değerler koleksiyonudur.

Sözlük Key:Value çiftini tutar. Key:Value çifti, daha optimize hale getirmek için sözlükte sağlanır.

Python'da , 'virgül' ile ayrılmış süslü {} parantezler içine bir dizi öğe yerleştirilerek bir sözlük oluşturulabilir . 
Sözlük, değer çiftlerini tutar, biri Key ve diğeri karşılık gelen çift öğe, Key:value olur . Bir sözlükteki value'lar herhangi
bir veri türünde olabilir ve çoğaltılabilir, oysa key'ler yinelenemez ve değiştirilemez olmalıdır.

Sözlük, sıralı, değiştirilebilir ve yinelenen key'i olmayan bir koleksiyondur.

Sözlük, yerleşik dict() işlevi tarafından da oluşturulabilir. Küme parantezlerine {} yerleştirilerek boş bir sözlük oluşturulabilir.

"""


Dict1 = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict1)

Dict2 = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict2)



Dict3 = {}
print("Empty Dictionary: ")
print(Dict3)

Dict4 = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict4)


Dict5 = {1: 'Geeks', 2: 'For', 3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}
print(Dict5)




"""
----- Dictionary Öge Ekleme ----

Öğelerin eklenmesi çeşitli şekillerde yapılabilir. Dict[Key] = 'Value' gibi anahtarla birlikte değer tanımlanarak bir Sözlüğe her seferinde bir değer eklenebilir. 
Sözlükte var olan bir değeri güncellemek, yerleşik update() yöntemi kullanılarak yapılabilir. İç içe anahtar değerleri de mevcut bir Sözlüğe eklenebilir. 

Not- Bir değer eklenirken, eğer anahtar/değer çifti mevcutsa, değer güncellenir, aksi takdirde sözlüğe yeni bir anahtar değeri eklenir.

"""
# Creating an empty Dictionary
Dict6 = {}
print("Empty Dictionary: ")
print(Dict6)

# Adding elements one at a time
Dict6[0] = 'Geeks'
Dict6[2] = 'For'
Dict6[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict6)

# Adding set of values
# to a single Key
Dict6['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict6)

# Updating existing Key's Value
Dict6[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict6)

# Adding Nested Key value to Dictionary
Dict6[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict6)





"""
----- Dictionary Ögelere Erişme ----

Bir sözlüğün öğelerine erişmek için anahtar adına bakın. Anahtar köşeli parantez içinde kullanılabilir. 

Bir sözlükten öğeye erişmeye yardımcı olacak get() adlı bir yöntem de vardır. Bu yöntem, anahtarı bağımsız değişken 
olarak kabul eder ve değeri döndürür.




get() yöntemi, anahtarın bir değerini döndürür. Anahtar bulunamazsa, bir KeyError istisnası atmak yerine Yok döndürür.


dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.get("a")
print(temp)

output: None

temp1 = dict1["b"]
print(temp1)

output: KeyError: 'b'

"""

Dict7 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accessing a element using key:")
print(Dict7['name'])

print("Accessing a element using key:")
print(Dict7[1])


Dict8 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("Accessing a element using get:")
print(Dict8.get(3))


Dict9 = {'Dict1': {1: 'Geeks'},
		'Dict2': {'Name': 'For'}}


print(Dict9['Dict1'])
print(Dict9['Dict1'][1])
print(Dict9['Dict2']['Name'])

"""
----- Dictionary Güncelleme ----
"""

# iki dicts {}+{}  veya diğer veri türleriyle toplama işlemi olmaz.
# bir dict'e ögeler key value ekleme veya dict'de update yapmak için update yöntemini kullanırız.

dictUpdate = {"Yellow":5, "Orange":4, "Black":9}
dictUpdate.update({"Yellow":4,"Orange":7,"Black":6,"Red":10})
print(dictUpdate)


"""
----- Dictionary Metodları ----

clear(): Sözlükteki tüm öğeleri kaldırır
copy(): Sözlüğün bir kopyasını döndürür
fromkeys(): Belirtilen anahtarlara ve değere sahip bir sözlük döndürür
get(): Belirtilen anahtarın değerini döndürür
items(): Her anahtar değer çifti için bir demet içeren bir liste döndürür
keys(): Sözlüğün anahtarlarını içeren bir liste döndürür
pop(): Belirtilen anahtarla öğeyi kaldırır
popıtem(): Son eklenen anahtar-değer çiftini kaldırır
setdefault(): Belirtilen anahtarın değerini döndürür. Anahtar yoksa: belirtilen değere sahip anahtarı ekleyin
update(): Sözlüğü belirtilen anahtar-değer çiftleriyle günceller
values(): Sözlükteki tüm değerlerin bir listesini döndürür
"""

# demo for all dictionary methods
dict10 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict11 = dict10.copy()
print(dict11)

# clear() method
dict10.clear()
print(dict10)

# get() method
print(dict10.get(1))

# items() method
print(dict10.items())

# keys() method
print(dict10.keys())

# pop() method
dict10.pop(4)
print(dict10)

# popitem() method
dict10.popitem()
print(dict10)

# update() method
dict10.update({3: "Scala"})
print(dict10)

# values() method
print(dict10.values())



a = [1,2,3]
b = [3,2,1]
print(a==b)

a = (1,2)
b = (2,1)
print(a==b)

a = {"a":2,"b":1}
b = {"b":1,"a":2}
print(a==b)


c = {"a":2,"x":4,"b":7}
a = {"a":1,"b":2}
a.update(c)
print(a)


"""
             Python Value ve Referans Veri Tipleri
         -------------------------------------------------
         
----Python Value Types----

Python Value tipinde tanımlanan bir veri (örneğin; number,string)  ile referans tipindeki veri (örneğin; list) tipleri belleğin farklı bölümlerinde
tutulduklarından dolayı value ve referans tipiyle nasıl çalışmamız gerektiğini biliyor olmamız gerekiyor.         
         
Aşağıdaki örnekte;

q, 5 ve w, 25 değerlerini aldıktan sonra w' nin değerini q' e eşitliyoruz ve q, 25 değerine sahip oluyor ve sonrasında 
w' nin değerini 10 a eşitliyoruz ancak w' nin 10' a eşitlenmesi q' in değerini etkilemiyor çünkü atama sırasında 
değer ataması yapılıyor dolayısıyla q ve w farklı adreslerde tutulan verilerdir.         

----Python Reference Types----

Referans tipinde tanımlanan veri tipleri (örneğin; list) atanan değeri tutmak yerine değerin tutulduğu adresleri saklarlar. 
Adreslerin karşılığı olan veriler ise (["apple","banana"]) belleğin farklı bölgesinde tutulur.

t ve y listeleri içindeki veriler farklı adres bilgilerini tutan veri tipleridir. t = y dediğimizde y' nin adresi t' ya atanır ve sonuçta t ve y, aynı adresleri tutarlar. Dolayısıyla a ya da b' de yapılan bir değişiklik aynı adreste yapıldığından dolayı a ve b ' nin içeriği de aynı olmuş olur.

t ve y 'nin içerikleri ["grape","banana"] , ["grape","banana"] olur.
         
"""
q, w = 5, 25
q = w
w = 10

print(q,w)



t = ["apple","banana"]
y = ["apple","banana"]

t = y

y[0] = "grape"

print(t, y)
# ["grape","banana"] , ["grape","banana"]


"""
               Gömülü Fonksiyonlar
          --------------------------------- 
 
---- abs() ----
abs() fonksiyonunu bir sayının mutlak değerini elde etmek için kullanıyoruz.


---- round() ----
round() fonksiyonu bir sayıyı belli ölçütlere göre yukarı veya aşağı doğru yuvarlamamızı sağlar.
kayan noktalı bir sayının üst ve alt tam sayılara olan uzaklığının birbirine eşit olduğu durumlarda Python’ın 
çift sayıya doğru yuvarlama yapmayı tercih etmesidir.

---- all() ----
All kelimesi Türkçede ‘hepsi’ anlamına gelir. Bu fonksiyonun görevi de bu anlamı çağrıştırır. all() fonksiyonunun görevi,
bir dizi içinde bulunan bütün değerler True ise True değeri, eğer bu değerlerden herhangi biri False ise de False değeri döndürmektir.
Bildiğiniz gibi, 0 hariç bütün sayıların bool değeri True’dur.

---- any() ----
Any kelimesi İngilizcede ‘herhangi bir’ anlamına gelir. İşte any() fonksiyonunun görevi de, bir dizi içindeki bütün 
değerlerden en az biri True ise True çıktısı vermektir.

---- bool() ----
Bu fonksiyon bir nesnenin bool değerini verir.
# True : 0 hariç tüm sayılar 'True' dur.
# False : 0 , " " , [] , () , dict() , set() gibi veriler 'False' boolean tipindedir.

---- bin() ----
Bu fonksiyon, bir sayının ikili düzendeki karşılığını verir.

---- chr() ----
Bu fonksiyon, kendisine parametre olarak verilen bir tam sayının karakter karşılığını döndürür.

---- ord() ----

Bu fonksiyon, bir karakterin karşılık geldiği ondalık sayıyı verir. Örneğin:

---- set() ----
set() fonksiyonu list() fonksiyonuna çok benzer. Bu fonksiyon da tıpkı list() fonksiyonu gibi, veri tipleri arasında 
dönüştürme işlemleri gerçekleştirmek için kullanılabilir. set() fonksiyonunun görevi farklı veri tiplerini kümeye dönüştürmektir.

---- list() ----
Bu fonksiyon iki farklı amaç için kullanılabilir:

Liste tipinde bir veri oluşturmak
Farklı veri tiplerini liste adlı veri tipine dönüştürmek

---- frozenset() ----
Bu fonksiyonu kullanarak farklı veri tiplerini frozensete dönüştürebilirsiniz.


---- tuple() ----
tuple() fonksiyonu da, tıpkı list(), set() ve benzerleri gibi bir dönüştürücü fonksiyondur. Bu fonksiyon farklı veri tiplerini demete dönüştürür.

---- complex() ----
Karmaşık sayılar, bir gerçek, bir de sanal kısımdan oluşan sayılardır.
Karmaşık sayılar Python’da ‘complex’ ifadesiyle gösteriliyor.

---- float() ----
Bu fonksiyonu, sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürmek için kullanıyoruz.

---- str() ----
Bu fonksiyonun, farklı veri tiplerini karakter dizisine dönüştürmek için kullanıldığını biliyorsunuz.

---- int() ----
Python 3'te Tamsayılar sınırsız hassasiyete sahiptir.

Bu fonksiyon birkaç farklı amaç için kullanılabilir. int() fonksiyonunun en temel görevi, 
bir karakter dizisi veya kayan noktalı sayıyı (eğer mümkünse) tam sayıya dönüştürmektir.

---- dict() ----
Bu fonksiyon, farklı veri tiplerinden sözlükler üretmemizi sağlar. Örneğin bu fonksiyonu kullanarak boş bir sözlük oluşturabiliriz.

---- hex() ----
Bu fonksiyon, bir sayıyı onaltılı düzendeki karşılığına çevirmemizi sağlar.

---- dir() ----
Eğer dir() fonksiyonunu parametresiz olarak kullanırsak, mevcut isim alanındaki öğeleri bir liste halinde elde ederiz.

---- enumerate() ----
İngilizcede enumerate kelimesi ‘numaralandırmak’ anlamına gelir. enumerate() fonksiyonunun görevi de kelimenin bu anlamıyla aynıdır. 
Yani bu fonksiyonu kullanarak nesneleri numaralandırabiliriz.

---- exit() ----
Bu fonksiyon, o anda çalışan programdan çıkmanızı sağlar. Eğer bu komutu etkileşimli kabukta verirseniz o anda açık olan oturum kapanacaktır.

---- help() ----
help() fonksiyonu gömülü fonksiyonlar içinde en faydalı fonksiyonların başında gelir. 
Bu fonksiyonu kullanarak Python programlama diline ait öğelere ilişkin yardım belgelerine ulaşabiliriz.

---- format() ----
Bu gömülü fonksiyonun görevi, daha önce karakter dizilerini işlerken, karakter dizilerinin bir metodu olarak öğrendiğimiz format() metoduna benzer bir şekilde, karakter dizilerini biçimlendirmektir.

---- hash() ----
Bu fonksiyon, belirli türdeki nesnelere bir karma değeri vermemizi sağlar. 

---- isinstance() ----
isinstance(object, type)
İşlev isinstance(),belirtilen nesne belirtilen türdeyse True, aksi takdirde False değer döndürür.

---- len() ----
Bu fonksiyon yardımıyla nesnelerin uzunluklarını hesaplayabileceğimizi biliyorsunuz:

---- max() ----
max() gömülü fonksiyonunun görevi, bir dizi içindeki en büyük öğeyi vermektir.

---- min() ----
min() fonksiyonu max() fonksiyonunun tam tersini yapar. Bildiğiniz gibi max() fonksiyonu bir dizi içindeki en büyük öğeyi buluyordu.

---- print() ----

---- quit() ----
Bu fonksiyonu programdan çıkmak için kullanıyoruz.

---- range() ----
Bu fonksiyonu belli bir aralıktaki sayıları listelemek için kullanıyoruz.

---- reversed() ----
Diyelim ki elimizde şöyle bir liste var:

isimler = ['ahmet', 'mehmet', 'veli', 'ayşe', 'çiğdem', 'ışık']
Eğer bu listedeki isimleri ters çevirmek, yani şöyle bir liste elde etmek isterseniz:

['ışık', 'çiğdem', 'ayşe', 'veli', 'mehmet', 'ahmet']

print(list(reversed(isimler)))

---- sorted() ----
bir dizi içindeki öğeleri belirli bir ölçüte göre sıraya dizmemizi sağlıyor.

---- sum() ----
Bu fonksiyonun temel görevi, bir dizi içindeki değerlerin toplamını bulmaktır.

---- type() ----
type() fonksiyonunun görevi bir nesnenin hangi veri tipine ait olduğunu söylemektir.

---- zip() ----
listelerin öğelerini birbirleriyle eşleştirmek istersek zip() fonksiyonundan yararlanabiliriz.

"""
print(abs(-20),abs(-20),abs(20.0))

print(round(12.4),round(12.7),round(1.5),round(12.5))
print(round(100.2563, 3))
print(round(100.000056, 3))


# ÖNEMLİ
"abs() ve round() gibi fonksiyonlarda ondalıklı sayıdan sonra gelen fazla 0 lar görmezden gelinip yuvarlanır."
"Mesela 300.000 ı 300.0 olarak kabul ederiz. Keza 25.600 sayısını 25.6 olarak ele alırız."

liste = [1, 2, 3, 4]
print(all(liste))

liste1 = ['ahmet', 'mehmet', '']
print(all(liste1))


print(any(liste1))
l = ['', 0, [], (), set(), dict()]
print(any(l))

print(bool(0),bool(1),bool([]))

print(bin(12))

print(chr(65))

print(complex(15))

s = set('istihza')
df = frozenset(s)
print(df)

x = isinstance(5, int)
print(x)

y = isinstance("Hello", (float, int, str, list, dict, tuple))
print(y)

print(list(enumerate('istihza')))

print(sorted('ahmet'))

a =["a","b","c"]
b = [1,2,3]
print(list(zip(a,b)))


"""
         Kaçış Dizeleri
   --------------------------------- 
   
   
---- Ters Slash (\) ----

---- Satır Başı (\n) ----

---- Sekme (\t) ----
 Tab (sekme) tuşuna basılmış gibi bir etki oluşturarak ifadeyi sağa doğru itiyor
 
---- Zil Sesi (\a) ----
\ işareti ‘a’ harfiyle birleşerek !bip! benzeri bir zil sesi üretilmesini sağlayabilir.

---- Aynı Satır Başı (\r) ----
Bu kaçış dizisi, bir karakter dizisinde aynı satırın en başına dönülmesini sağlar.

---- Düşey Sekme (\v) ----
Eğer \ işaretini ‘v’ harfiyle birlikte kullanırsak düşey sekme denen şeyi elde ederiz.
"""

print('Yarın Adana\'ya gidiyorum.')
print("\"book\" kelimesi Türkçede \"kitap\" anlamına gelir.")

print("birinci satır\nikinci satır\nüçüncü satır")

print("abc\tdef")

print("\a")

print("Merhaba\rZalim Dünya!")
print("Merhaba\rDünya")

print("düşey\vsekme")


"""
     Print Fonksiyonun Parametreleri
   -----------------------------------

----sep----

print(), kendisine verilen parametreleri birleştirirken, parametreler arasına bir boşluk yerleştiriyor. 
Bunu daha net görmek için şöyle bir örnek daha verelim:

print("Python", "PHP", "C++", "C", "Erlang")  --->  Python PHP C++ C Erlang


Fonksiyonların bir de daha özel görünümlü parametreleri vardır. Mesela print() fonksiyonunun sep adlı özel bir parametresi bulunur. 
Bu parametre print() fonksiyonunda görünmese bile her zaman oradadır. Yani diyelim ki şöyle bir kod yazdık:

print("http://", "www.", "google.", "com")

Burada herhangi bir sep parametresi görmüyoruz. Ancak Python yukarıdaki kodu aslında şöyle algılar:

print("http://", "www.", "google.", "com", sep=" ")



----end----

Tıpkı sep parametresi gibi, end parametresi de print() fonksiyonunda görünmese bile her zaman oradadır.

sep parametresi print() fonksiyonuna verilen parametreler birleştirilirken araya hangi karakterin gireceğini belirliyordu. 
end parametresi ise bu parametrelerin sonuna neyin geleceğini belirler.



print("Bugün günlerden Salı", end=".\n")

output:

Bugün günlerden Salı.
(bir sonraki yazma buradan başlar)


print('a', 'b', end='')

output:

a b>>>



----file----

dosya = open("deneme.txt", "w")
print("Ben Python, Monty Python!", file=dosya)
dosya.close()


----Yıldızlı Parametre----

Şimdi size şöyle bir soru sormama izin verin: Acaba yandaki gibi bir çıktıyı nasıl elde ederiz?   L.i.n.u.x

Aklınıza hemen şöyle bir cevap gelmiş olabilir:

print("L", "i", "n", "u", "x", sep=".") output --> L.i.n.u.x

Yukarıdaki, gerçekten de doğru bir çözümdür. Ancak bu soruyu çözmenin çok daha basit bir yolu var. Şimdi dikkatle bakın: 
print(*"Linux", sep=".")  output --> L.i.n.u.x


print(*"Galatasaray")  output --> G a l a t a s a r a y


"""

print("http://", "www.", "istihza.", "com", sep="")
print("bir", "iki", "üç", "dört", "on dört", sep="mumdur")
print('a', 'b', sep=None)
print('a', 'b', sep='')



print("bir", "iki", "üç", "dört", "on dört",
sep=" mumdur ", end=" mumdur\n")





"""
     Mutable vs Immutable Objects
    -----------------------------------
    
Mutable Objects durumlarını veya içeriklerini değiştirebilirken,Immutable Objects durumlarını veya içeriklerini değiştiremez.

Immutable Objects : int, float, bool, string, unicode, frozenset, tuple gibi yerleşik türlerdir . Basit bir ifadeyle, 
değişmez bir nesne oluşturulduktan sonra değiştirilemez.


Mutable Objects : Bunlar list , dict , set türündedir 
"""


"""
   Snake Case , Camel Case , Pascal Case 
  ---------------------------------------------
  
Snake case, her kelimeyi bir alt çizgi karakteriyle "_" ayırır.
Snake case kullanırken, tüm harflerin küçük olması gerekir.


Camel case kullanırken, ilk kelimeyi küçük harf yaparak başlarsınız. Ardından, takip eden her kelimenin ilk harfini büyük yazarsınız.


Pascal case kullanırken, her kelime büyük harfle başlar (ilk kelimenin küçük harf olduğu camel case'in aksine).

"""

number_of_donuts = 34
fave_phrase = "Hello World"


numberOfDonuts = 34
favePhrase = "Hello World"


NumberOfDonuts = 34
FavePhrase = "Hello World"





"""
    EXAMPLE
  ------------
"""

liste = [1,2,3,4]

liste.extend([1,2,5,6,7])
print(liste)

s = {'elma': 44, 'armut': 10, 'erik': 100}
list(s)


a = 1,2,3,4
print(a)

print(tuple([1,2,3,4]))
print(tuple('dodo'))

c = (1,"a",True,5,"a")
print(c)

print(c.count("a"))

Dict = dict([(1, 'Geeks'), (2, 'For')])
print(Dict)

print(Dict.items())


a = set("dodo")
print(a)
"""
print(a[1])  #sets'ler indikslenemez.
"""

set1 = set([4, 5, (6, 7)])
set1.update([10, 11])  #birden fazla öge ekleme için
print(set1)


""""
set1.discard(8)

print(set1) >>> listede olmayan bir elemanı kaldırmaya çalışırsak hata oluşmaz liste öylece kalır

set1.remove(8) >>> listede olmayan bir elemanı kaldırmaya çalışırsak Keyerror hatası oluşur.

print(set1)

"""

set1.pop()
print(set1)
set1.pop()
print(set1)

# list nesnesinde pop ile veri silerken indeks belirtmedikçe sondna silmeye başlardı ama sets'lerde baştan silmeye çalışıyor.Ayrıca sets'lerde
# indiksleme olayı olmadığından pop ile istediğimiz karakteri silemeyiz.




my_dict = {1: "One", 2: "Two", 3: "Three"}
my_set2 = set(my_dict)
print("my_dict as a set: ", my_set2)

A = {2, 4, 5, 6}
B = {4, 6, 7, 8}

print("A U B:", A.union(B))


A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print(A.difference(B))
print(B.difference(A))


A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print(A-B)


A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
A.difference_update(B)
print(A)


set_A = {1, 2, 3, 3, 4, 5}
set_B = {6, 7, 3, 9, 4}
print(set_A.symmetric_difference(set_B))


s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2))
#iki kümenin kesişimi boş kümeyse True döndürür.


