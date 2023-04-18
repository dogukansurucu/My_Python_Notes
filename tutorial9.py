import random
import math
import sys

"""

        Python Random Module
    -------------------------------

Eğer yazdığınız programlarda, belirli bir aralıkta rastgele sayıların üretilmesine ihtiyaç duyarsanız
Python’ın standart kütüphanesinde bulunan random adlı bir modülü kullanabilirsiniz.

Tıpkı öteki modüllerde olduğu gibi, random modülü de birtakım faydalı nitelik ve fonksiyonları barındırır.
Biz bu bölümde, bu nitelik ve fonksiyonlar arasında en sık kullanılanları inceleyeceğiz.


----random()----
random modülünün random() adlı fonksiyonunu kullanarak, 0.0 ile 1.0 arasında rastgele bir kayan noktalı sayı üretebilirsiniz.
random() fonksiyonu, kendisini her çalıştırışınızda farklı bir kayan noktalı sayı üretecektir:
Üretilen sayıların 0 ile 1 arasında olduğunu özellikle dikkatinizi çekmek isterim.


----uniform()----
random.uniform(a, b)

İşte, belirli bir aralıkta kayan noktalı sayılar üretmek istediğimizde, random() yerine uniform() adlı bir fonksiyon kullanacağız.


----randint()----
random.randint(start, stop)

Şimdiye kadar öğrendiğimiz random() ve uniform() fonksiyonları bize yalnızca kayan noktalı sayılar üretme imkanı veriyordu. 
Ancak elbette biz kimi durumlarda kayan noktalı sayılar yerine tam sayılar üretmek de isteyebiliriz. 
İşte böyle bir durumda, random modülünün randint() adlı başka bir fonksiyonunu kullanabiliriz.


----choice()----
random.choice(sequence)

random modülünün choice() adlı fonksiyonunu kullanarak, dizi niteliği taşıyan veri tiplerinden rastgele öğeler seçebiliriz. 


----shuffle()----
random.shuffle(sequence)

shuffle() fonksiyonunu kullanarak, dizi niteliği taşıyan veri tiplerindeki 
öğeleri karıştırabilirsiniz(yani öğelerin sırasını karışık bir hale getirebilirsiniz).


----sample()----
random.sample(sequence, k)

‘Sample’ kelimesi ‘numune’ anlamına gelir. İşte kelimenin bu anlamına paralel olarak sample() fonksiyonu da, 
dizi niteliği taşıyan veri tiplerinden belli sayıda numune alınabilmesini sağlar.


----seed()---- 
Rasgele sayı üretecini başlatır.



----randrange()----
random.randrange(start, stop, step)

Yöntem, randrange()belirtilen aralıktan rastgele seçilen bir öğe döndürür.

"""

print(random.random())
print(random.uniform(0.5, 1.5))
print(random.randint(45, 500))

liste = ['ali', 'veli', 'ahmet', 'mehmet', 'celal', 'selin', 'nihat']
print(random.choice(liste))

kardiz = 'istihza'
print(random.choice(kardiz))

random.shuffle(liste)
print(liste)


liste1 = range(100)
print(random.sample(liste, 5))

print(random.seed(10))


"""
        Python Math Module
    -------------------------------

math modülü matematiksel işlemler yapmanızı kolaylaştırmak için yazılmış bir modüldür.


----math.ceil()----
Verilen ondalıklı sayıyı bir üst sayıya çevirir.

----math.floor()----
ceil fonksiyonunun tam tersi bir işleve sahip. Verilen ondalıklı sayıyının bir altındaki tam sayıyı döndürür.

----math.copysign()----
Aldığı iki parametreden ikincisinin işaretini birincisine verir.

----math.fabs()----
Verilen değerin mutlak değerini alır. Gömülü fonksiyonlardan abs’den küçük bir farkı var. abs'da tam sayının mutlak değeri tam
sayıyıken fabs'da sayı ister tam sayı olsun ister ondalıklı sayı olsun sonuç float(kayan nokta) şeklinde döner.

----math.factorial()----
Verilen sayının faktoriyelini döndürüyor. Eğer verilen değer pozitif tam sayı değilse ValueError hatası veriyor.

----math.fmod()----
Verdiğiniz birinci parametrenin ikinci parametreye bölümünden kalanı buluyor.

----math.gcd()----
Verilen iki sayının EBOB’unu veriyor.

----math.trunc()----
int fonksiyonu ile aynı işi yapıyor. tam/ondalıklı sayının tam kısmını alıyor.Yani ondalıklı kısmını atıyor.

----math.e----
euler sabitini tutan bir değişken. Değeri: 2.718281…

----math.pi----
pi sayısını tutan değişken. Değeri: 3.141592….

----math.log()----
Birinci değerin ikinci değere göre logaritmasını hesaplar.

----math.log2()----
Verilen sayının 2 tabanında logaritmasını hesaplar.

----math.log10()----
Verilen sayının 10 tabanında logaritmasını hesaplar.

----math.pow()----
** ve gömülü fonksiyonlardan pow ile aynı işi yapıyor. Yani birinci sayının ikinci sayıya göre kuvvetini alıyor.

----math.sqrt()----
Verilen sayının karekökünü hesaplar.

----math.degrees()----
Verilen sayıyı radyandan dereceye çevirir.

NOT: 1 pi radyan 180 derecedir.
     matematikte radyanı dereceye çevirirken "pi cinsindeki radyanı" , 180/pi ile çarpıyoruz.

----math.radians()----
Verilen sayıyı dereceden radyana çevirir. 

NOT: matematikte dereceyi radyana çevirirken pi/180 ile çarpıyoruz ve pi'li bir radyan ifades, ortaya çıkar.

----math.sin()----
Radyan cinsinden verilen sayının sinüsünü hesaplar.

AMAAA, mesela sin(math.radians(30)) dersek derece cinsinden verilen sayının sinüs değerini bulmuş oluruz. 
yukarıdaki örneğin yani 30 derecenin değeri 0,5 dir.

----math.cos()----
Radyan cinsinden verilen parametrenin kosinüsünü hesaplar. 

----math.tan()----
Radyan cinsinden verilen parametrenin tanjantını hesaplar.


"""

print(math.ceil(32.05),math.ceil(5))
print(math.floor(25.42),math.floor(-12.25))
print(math.copysign(25,-12))
print(math.fabs(-28))
print(math.factorial(5))
print(math.fmod(45,2))
print(math.gcd(45,70))
print(math.trunc(15.12))
print(math.log(10,10))
print(math.log2(2))
print(math.log10(1000))
print(math.pow(2,5))
print(math.sqrt(16))
print(math.degrees(1.5707963267948966))
print(math.radians(90))
print(math.sin(math.radians(60)))




"""
       Python Sys Module
    -------------------------------
    
Python'daki sys modülü, Python çalışma zamanı ortamının farklı bölümlerini işlemek için kullanılan çeşitli işlevler ve değişkenler sağlar.
Yorumlayıcı ile güçlü bir şekilde etkileşime giren değişkenlere ve işlevlere erişim sağladığı için yorumlayıcı üzerinde çalışmaya izin verir.


sys.exit([arg]);

programdan çıkmak için kullanılabilir. İsteğe bağlı argüman arg, çıkışı veya başka türde bir nesneyi veren bir tamsayı olabilir. Bir tamsayı ise, sıfır "başarılı sonlandırma" olarak kabul edilir.

Not: sys.exit() yöntemine bir dize de iletilebilir.

"""

print(sys.version)


age = 17

if age < 18:

    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")
