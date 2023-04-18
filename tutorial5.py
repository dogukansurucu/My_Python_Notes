"""
     Python For Loops
  -------------------------

Python For döngüsü, sıralı geçiş için kullanılır, yani String, Tuple, List, Set veya Dictionary gibi bir
yineleme üzerinde yineleme yapmak için kullanılır.

Syntax:


for var in iterable:
    # statements


Burada yinelenebilir, listeler, demetler gibi nesnelerin bir koleksiyonudur. For döngülerinin içindeki girintili ifadeler,
yinelemedeki her öğe için bir kez yürütülür. var değişkeni, döngü boyunca her seferinde yinelenebilirin bir sonraki öğesinin değerini alır.

"""


l = ["geeks", "for", "geeks"]
for i in l:
    print(i)


# Iterating over dictionary
print("Dictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("% s % d" % (i, d[i]))


# Iterating over a String
print("String Iteration")
s = "Geeks"
for i in s:
    print(i)


"""
    Loop Control Statements
  --------------------------

Döngü kontrol ifadeleri, yürütmeyi normal dizisinden değiştirir. Yürütme bir kapsamdan ayrıldığında, o kapsamda oluşturulan 
tüm otomatik nesneler yok edilir. Python aşağıdaki kontrol ifadelerini destekler.


----Continue Statement----
Python devam deyimi, kontrolü döngünün başına döndürür.
Python Devam deyimi, yalnızca mevcut yineleme için döngü içindeki kodun geri kalanını atlarken döngünün bir 
sonraki yinelemesini yürütmeye zorlayan bir döngü kontrol ifadesidir, yani, devam deyimi döngüde yürütüldüğünde, 
döngü içindeki kod devam deyimi geçerli yineleme için atlanacak ve döngünün bir sonraki yinelemesi başlayacaktır.



----Break Statement----
Python'daki break deyimi, bazı harici koşullar tetiklendiğinde kontrolü döngüden çıkarmak için kullanılır. 
break deyimi döngü gövdesinin içine konur (genellikle if koşulundan sonra). Geçerli döngüyü, yani içinde göründüğü 
döngüyü sonlandırır ve o döngünün bitiminden hemen sonra bir sonraki ifadede yürütmeye devam eder. 
Break deyimi iç içe geçmiş bir döngü içindeyse, break en içteki döngüyü sonlandırır.



----Pass Statement----
Boş döngüler yazmak için pass ifadesi . Geçiş ayrıca boş kontrol ifadeleri, işlevler ve sınıflar için de kullanılır.

Kullanıcı hangi kodu yazacağını bilmediğinde, kullanıcı pass'ı o satıra yerleştirir. Bazen, kullanıcı herhangi bir 
kodun yürütülmesini istemediğinde pass kullanılır. Böylece kullanıcı , döngüler, işlev tanımları, sınıf tanımları veya 
if deyimleri gibi boş koda izin verilmeyen yerlere pass yerleştirebilir. 
Bu nedenle, pass deyimi kullanıcısını kullanmak bu hatayı önler.


"""

# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)




for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)



for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)






"""
      range() function
  -----------------------------
range(start, stop, step)

Python range(), bir kullanıcının bir eylemi belirli sayıda gerçekleştirmesi gerektiğinde kullanılan yerleşik bir işlevdir. 
Python(3.x) içindeki range(), Python(2.x) içindeki xrange() adlı bir fonksiyonun yeniden adlandırılmış versiyonudur.

Range(start,stop,step) işlevi, bir sayı dizisi oluşturmak için kullanılır. Kullanıcının işleve kaç argüman ilettiğine bağlı olarak, 
kullanıcı bu sayı dizisinin nerede başlayacağına ve biteceğine ve ayrıca bir sayı ile next.range() 
arasındaki farkın ne kadar büyük olacağına karar verebilir, esas olarak üç argüman alır;


start: tamsayı dizisinin döndürüleceği başlangıç tamsayı

stop: tamsayı dizisinin döndürüleceği tamsayı. 
Tam sayıların aralığı stop - 1'de sona erer.

step: dizideki her bir tamsayı arasındaki artışı belirleyen tamsayı değeri



ÖNEMLİ: Python range() yalnızca tamsayılarla çalışır. Float tipini desteklemiyor, 
yani argümanlarının hiçbirinde kayan nokta/ondalık değeri kullanamıyoruz. Eğer kullanırsak bu TypeError'a neden olur.

NumPy, kayan noktalı sayıların aralığını elde etmek için arange() işlevine sahiptir. 
Python yerleşik range() işleviyle aynı sözdizimine ve işlevselliğe sahiptir. 
Ayrıca start, stop ve step argümanlarında kayan noktalı sayılar kullanmamıza izin verir.

np.arange (start, stop, step)

"""

# printing a number
for i in range(10):
    print(i, end=" ")


# performing sum of first 10 numbers
sum = 0
for i in range(1, 10):
    sum = sum + i
print("\nSum of first 10 numbers :", sum)


import numpy as np

# range for floats with np.arange()
for i in np.arange(0, 4.5, 0.5):
    print(i, end=', ')


print(type(range(5)))
"""
    loop in Python with else - For & While
  -----------------------------------------
Çoğu programlama dilinde (C/C++, Java, vb.), else deyimlerinin kullanımı if koşullu deyimlerle sınırlandırılmıştır. 
Ancak Python, else koşulunu for döngüleriyle kullanmamıza da izin verir. 

Not: for/while'dan hemen sonra gelen else bloğu, yalnızca döngü bir break deyimi ile SONLANDIRILMADIĞINDA yürütülür. Yalnız,koşullu döngü varsa
ve contiune ifadesi ile döngü bittikten sonra da else ifadesi yürütülür.
"""

a=6

while a<5:
    print("dodo")
    break
else:
    print("kemal")


a=6
b=7
c=7
while a>5 and b==c:
    print("dodo")
    break
else:
    print("kemal")


d=5
while d<7:
    print("dodo")
    d+=1
else:
    print("kemal")



for i in range(1, 4):
    print(i)
else:
    print("No Break\n")



i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")


"""
        Python While Loop
     -------------------------
     
Python While Loop, belirli bir koşul sağlanana kadar bir ifade bloğunu tekrar tekrar yürütmek için kullanılır. 
Koşul yanlış olduğunda ise programdaki döngüden hemen sonraki satır çalıştırılır.


Syntax:

while expression:
    statement(s)
    
    
While döngüsü belirsiz yineleme kategorisine girer. Belirsiz yineleme, döngünün yürütülme sayısının önceden açıkça belirtilmediği anlamına gelir. 
İfadeler, bir programlama yapısının tek bir kod bloğunun parçası olarak kabul edilmesinden sonra aynı sayıda karakter 
boşluğu ile girintili tüm ifadeleri temsil eder. Python, ifadeleri gruplama yöntemi olarak girinti kullanır. 
Bir while döngüsü yürütüldüğünde, ifade önce bir Boole bağlamında değerlendirilir ve doğruysa, döngü gövdesi yürütülür. 
Daha sonra ifade tekrar kontrol edilir, hala doğruysa gövde tekrar çalıştırılır ve bu ifade yanlış olana kadar devam eder.

"""

count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")



a = [1, 2, 3, 4]

while a:
    print(a.pop())



i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1



i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break

    print('Current Letter :', a[i])
    i += 1




a = 'geeksforgeeks'
i = 0

while i < len(a):
    i += 1
    pass

print('Value of i :', i)




# Initialize a counter
count = 0

# Loop infinitely
while True:
    # Increment the counter
    count += 1
    print(f"Count is {count}")

# Check if the counter has reached a certain value
    if count == 10:
# If so, exit the loop
        break
# This will be executed after the loop exits
print("The loop has ended.")




s = 'geeksforgeeks'
# Using for loop
for letter in s:
    print(letter)
    if letter == 'e' or letter == 's':
        break

print("Out of for loop" )
print()




i = 0
# Using while loop
while True:
    print(s[i])
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1

print("Out of while loop ")



# loop from 1 to 10
for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")



a = dict()
print(a)

a["dodo"] = 5
print(a)
a["ali"] = 7
print(a)

for i in a:
    print(" key: %s value: %d" % (i,a[i]))

"""

----Single statement while block---

Tıpkı if bloğu gibi, while bloğu tek bir ifadeden oluşuyorsa, tüm döngüyü tek bir satırda ilan edebiliriz. 
Döngü gövdesini oluşturan blokta birden fazla ifade varsa, bunlar noktalı virgülle (;) ayrılabilir. 


"""

count = 0
while (count < 5): count += 1; print("Hello Geek")


"""
    Looping Techniques in Python
  ----------------------------------

Python, çeşitli sıralı kaplarda belirli yerleşik işlevlerle çeşitli döngü tekniklerini destekler. Bu yöntemler öncelikle
rekabetçi programlamada ve ayrıca kodun genel yapısını koruyan döngülerle belirli bir teknik gerektiren çeşitli 
projelerde çok faydalıdır. Geleneksel döngü yaklaşımında bildirdiğimiz ekstra değişkenleri bildirmeye gerek 
olmadığı için çok fazla zaman ve bellek alanı tasarrufu sağlanır.


----Using enumerate()----
enumerate(), belirli bir dizinde bulunan değerle birlikte dizin numarasını yazdıran kaplar arasında döngü yapmak için kullanılır.


----Using zip()----
Zip(), değerleri sırayla yazdıran 2 benzer kabı (list-list veya dict-dict) birleştirmek için kullanılır. 
Döngü yalnızca daha küçük kap bitene kadar var olur.


----Using items()----

----Using sorted()----

----Using reversed()----

"""



for key, value in enumerate(['The', 'Big', 'Bang', 'Theory']):
    print(key, value)



for key, value in enumerate(['Geeks', 'for', 'Geeks',
							'is', 'the', 'Best',
							'Coding', 'Platform']):
    print(value, end=' ')




# initializing list
questions = ['name', 'colour', 'shape']
answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
# and print values
for question, answer in zip(questions, answers):
    print('What is your {0}? I am {1}.'.format(question, answer))




basket = ['guave', 'orange', 'apple', 'pear',
		'guava', 'banana', 'grape']

for fruit in sorted(set(basket)):
    print(fruit)




for i in reversed(range(1, 10, 3)):
    print(i)
