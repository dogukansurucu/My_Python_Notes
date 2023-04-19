"""
import datetime

print(dir(datetime))

output: ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']


import date
import time
"""



"""
datetime modülü; zaman, saat ve tarihlerle ilgili işlemler yapabilmemiz için bize çeşitli
fonksiyon ve nitelikler sunan bazı sınıflardan oluşur. Bu modül içinde temel olarak üç farklı sınıf bulunur.



datetime modülü içinde yer alan bu üç sınıf şunlardır:

date sınıfı; tarihle ilgili işlemler yapabilmemizi sağlayan fonksiyon ve nitelikleri barındırır.
time sınıfı; zamanla/saatle ilgili işlemler yapabilmemizi sağlayan fonksiyon ve nitelikleri barındırır.
datetime sınıfı; date ve time sınıflarının birleşiminden ve ilave birkaç nitelik ve fonksiyondan oluşur.

"""


from datetime import date
from datetime import time

from datetime import datetime
from datetime import timedelta


# print(dir(datetime))  --> datetime modülünün datetime sınıfındaki içeren nitelik ve fonksiyonları verir.

"""   now()
   ------------

datetime modülünün içindeki datetime sınıfının now() adlı fonksiyonu, bize içindeki bulunduğumuz
andaki tarih, saat ve zaman bilgilerini verir.
"""


a = datetime.now()
print(a,"\n")
print(a.date(),":",a.year,a.month,a.day,"\t",a.time(),":",a.hour,a.minute,a.second,a.microsecond,"\n")
print("-------------------------------------------------------------------------------------------------","\n")



"""
    today()
   ----------
 
Bu fonksiyon now() ile aynı içeriğe ve işleve sahiptir. today() fonksiyonunu now fonksiyonunu kullandığınız gibi kullanabiliriz.
 
"""


b = datetime.today()
print(b,"\n")
print(b.date(),":",b.year,b.month,b.day,"\t",b.time(),":",b.hour,b.minute,b.second,b.microsecond,"\n")
print("-------------------------------------------------------------------------------------------------","\n")


"""
from datetime import datetime

   datetime(Yıl,Ay,Gün,Saat,Dakika,Saniye,...)
 ------------------------------------------------
 
Yukarıdaki yöntem kullanıcıdan tarih bilgisi girerek o tarih üzerinde datetime sınıfının fonksiyonlarını kullanmak istenebilir.
  
"""

d = datetime(2023,2,5)    #datetime sınıfına tarih bilgisini girerken, başta '0' olamaz.
print(d.date(),",",d.time())           # tarih bilgisi sıralaması yıl ay gün şeklindedir.
                           # çıktıda tarihler arasında '-' olur.


c = datetime(2015,5,17)

print("\n\n")
"""
      ctime()
  ---------------

ctime() fonksiyonu, içinde bulunduğumuz ana ilişkin tarih ve zaman bilgilerini içeren okunaklı bir karakter dizisi verir.
Bu fonksiyona, parametre olarak bir datetime.datetime() sınıfı vermemiz gerekir. 
Yani:


"""
print("-------------------------------------------------------------------------------------------------","\n")
x = datetime.ctime(a)
print(x,"\n\n")
print("-------------------------------------------------------------------------------------------------","\n")

"""
       strftime()
    ----------------

strftime() fonksiyonu, size tarih ve zaman bilgilerini ihtiyaçlarınız doğrultusunda biçimlendirme imkanı sunar.

Bu fonksiyon toplam iki parametre alır. İlk parametre, tıpkı ctime() fonksiyonunda olduğu gibi, bir datetime.datetime sınıfıdır.
İkinci parametre ise, tarih/zaman bilgisini içeren karakter dizisini nasıl biçimlendirmek istediğimizi gösteren bir biçimlendiricidir.


BİÇİMLENDİRME OPERATÖRLERİ:

%a : hafta gününün kısaltılmış adı
%A : hafta gününün tam adı
%d : sayı değerli bir karakter dizisi olarak gün

%b : ayın kısaltılmış adı
%B : ayın tam adı
%m : sayı değerli bir karakter dizisi olarak ay

%y : yılın son iki rakamı
%Y : yılın dört haneli tam hali

%x : tam tarih bilgisi
%X : tam saat bilgisi

%c : tam tarih, saat ve zaman bilgisi

%j : belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
%U : belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı



"""
z = datetime.strftime(d,"%d %B %Y %A günü")
y = datetime.strftime(a,"%d %B %Y %A günü")

print(z)
print(y)
print("gün: ",y.split()[3])

f = datetime.strftime(a,"%d.%m.%Y")
print(f)


"""
      strptime()
  -------------------

Eğer elimizdeki karakter dizisi şöyle bir şeyse ne yapacağız?

t = "21 June, 2018"


"""
print("----"*24,"\n")
date_string = "21 June, 2018"


date_object = datetime.strptime(date_string, "%d %B, %Y")
print("\n")
print(date_object)
print("gün: ",date_object.day,"ay: ",date_object.month,"yıl: ",date_object.year)

"""
       timestamp()-fromtimestamp()
    --------------------------------
Eğer datetime.datetime nesnelerinden bir zaman damgası üretmek isterseniz timestamp() fonksiyonunu kullanabilirsiniz:

Eğer daha sonra bu zaman damgasını anlamlı bir tarihe dönüştürmeniz gerekirse fromtimestamp() fonksiyonunu kullanabileceğinizi biliyorsunuz:

"""

print("----"*24,"\n")
z = datetime.timestamp(a)
print(z)


print(datetime.fromtimestamp(z),"\n","----"*24)


"""
   İki Tarih Arasındaki Farkı Bulmak
------------------------------------------
"""


sonuc = a - c
print(a)
print(c)
print("gün farkı: ",sonuc.days)

print("----"*24)

"""
  İleri Bir Tarihi Bulmak-Geçmiş Bir Tarihi Bulmak
------------------------------------------------------

Diyelim ki 200 gün sonra hangi tarihte olacağımızı bulmak istiyoruz. Tıpkı bir önceki başlıkta tartıştığımız gibi, 
bu isteğimizi yerine getirmek için de timedelta nesnesinden yararlanacağız.


Geçmiş bir tarihi bulmak da, tahmin edebileceğiniz gibi, ileri bir tarihi bulmaya çok benzer.
"""

ileri = a+timedelta(days=25)
print(ileri)

geri = a-timedelta(days=12,hours=4,minutes=14)
print(geri)
