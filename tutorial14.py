import json

"""
  JSON NEDİR ?
 -------------

JSON, veri alışverişi için kolayca okunabilen ve yazılabilen ve oluşturulabilen hafif bir veri biçimidir.
JSON tam bir dilden bağımsız metin biçimidir. 
Python JSON verileriyle çalışmak için Python, json adlı gömülü bir module sahiptir.



JSON modülünde 4 ana fonksiyon bulunuyor. Bunlardan ikisi Python ile JSON oluşturmaya yararken diğer ikisi JSON verilerini çözmeye yarar.
JSON oluşturan fonksiyonlar şu ikisidir:            json.dump
                                                    json.dumps


JSON verilerini çözen iki fonksiyon ise şunlardır:  json.load
                                                    json.loads

"""


"""
DİKKAT:

JSON OBJECT	  PYTHON OBJECT
object	        dict
array	        list
string	         str
null	         None
number(int)	     int
number(real)	float
true	         True
false	         False



a = '{"ad":5,"soyad":7}'  -----> a jsonstring iken

c = b.loads()   -------> b dictionary veri tipidir.


"""

"""
      json.dump ve json.dumps
    -----------------------------

Aşağıdaki Python nesnesi türleri JSON dizelerine dönüştürülebilir:

dict
list
tuple
string
int
float
True
False
None



dump fonksiyonu çıktıyı illaki bir dosya içine aktarır. Yani size al bu senin istediğin JSON çıktısı demez. 
Bunu diyen dumps fonksiyonudur. dumps fonksiyonu str tipinde bir değer döndürürken dump fonksiyonu hiçbir değer döndürmez.




Bu fonksiyonların birkaç parametresi var. Şimdi sıra bunların ne işe yaradığını öğrenmekte.

####  skipkeys ####

Normalde Python, JSON oluştururken anahtar veya değer basit tipte (str,int,float…) değilse TypeError hatası verir. Eğer bu parametre True (Varsayılan False) ise hata vermek yerine o ikiliyi atlar.

#### ensure_ascii ####

Eğer bu parametre True (varsayılan olarak) ise çıktıda ASCII tablosuna uymayan karakterlerden kaçınır. False ise buna dikkat etmez.

#### indent ####

Eğer negatif olmayan bir tamsayı veya bir karakter dizisi ise girintileme sayesinde daha güzel bir çıktı almanızı sağlar. 
Eğer 0, negatif sayı veya boş karakter dizisi(“”) ise her öğeyi yeni satıra basar. None(varsayılan) ise dip dibe bir çıktı verir. 
Pozitif bir sayı verildiğinde onu boşluk sayısı kabul ederek girintileme yapar. 

#### separators ####

Bu parametre verilen değeri öğeler arasında ayraç olarak kullanır. Verilen değer tuple tipinde olmalıdır. 
Varsayılan olarak şu kullanılır: (“,”, “: “) Ancak indent parametresi None değerindeyse ilk virgül değeri de iki nokta gibi sonuna boşluk alır. 
Yani şu şekilde olur: (”, “, “: “)

#### sort_keys ####

Sonucun sıralanıp sıralanmayacağını belirtmek için parametreyi kullanın :



"""
print("-----"*10)

print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True),"\n","-----"*10)


print(json.dumps(["üzüm"],ensure_ascii=True))
print(json.dumps(["üzüm"],ensure_ascii=False),"\n","-----"*10)



print(json.dumps({"Özellikler":{"Hız":150,"Ses":"10db"}},indent=None))
print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent=0))
print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent=4))
print(json.dumps({"Ozellikler":{"Hız":150,"Ses":"10db"}},indent="\n"),"\n","-----"*10)


"""

    json.load ve json.loads
  -----------------------------
Bu iki fonksiyon da dump ve dumps gibi birbirine çok benziyor. Hatta farkları bile neredeyse aynı. 
load fonksiyonu sadece dosyadaki JSON verilerini Python verisine çevirirken loads fonksiyonu veriyi parametre olarak alıyor. 
dump ve dumps’da olduğu gibi parametreleri tamamen aynı.


Şimdi de sıra fonksiyonların aldığı parametrelerde.

#### object_hook ####

Döndürülen değerin veri tipini değiştirmenizi sağlar. Bunu bir kod ile açıklayalım.

#### object_pairs_hook ####

object_pairs_hook, object_hook ile benzer görevler yapıyor. İkisi arasında öncelik object_pairs_hook’da.
Eğer anahtar değer ilişkisinden oluşan bir JSON verisiyse object_pairs_hook değilse object_hook parametresi kullanılır.

#### parse_int ####

int tipindeki değerlerin Python koduna dönüştürülürken hangi tipin kullanılması gerektiğini belirler.
"""

print(json.loads('{"mezuniyet": "üniversite", "Bölüm": "Tıp"}'))

print(json.loads('{"Satılan": 54, "Kalan": 46}',parse_int=float))

print(json.loads('{"mezuniyet": "üniversite", "Bölüm": "Tıp"}',object_hook=list))




# konuyu açıklar güzel örnekler





#örnek1
"""

import json

# Opening JSON file
f = open('data.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['emp_details']:
	print(i)

f.close()



"""

"""




# örnek2

import json

a = '{"name": "Bob", "languages": "English"}'

y = json.loads(a)

print("JSON string = ", y)
print("\n")




f = open ('data.json', "r")

data = json.loads(f.read())

for i in data['emp_details']:
	print(i)
	
f.close()


"""


"""
Yani bir python nesnesini dump ile json dosyasına atıp load ile python nesnesi şeklinde çekebilirsin.Keylere ulaşabilirsin.
Bir json dosyasını load ile değil de normal dosya okuma fonk. olan read ile okursan okuduğun json nesnesi olduğundan
python nesnesine çevirmek için loads metodunu kullanman gerekir.
"""