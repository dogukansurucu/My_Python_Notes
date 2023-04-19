import re

result = dir(re)
print(result)
print("\n")

"""
    regular expression modulü metodlarıya arama işlemi
  --------------------------------------------------------
"""

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# ----re.findall()----

print(re.findall("Python",str))
# string bir ifadeyi str içinde arıyoruz.Aradığımız kelime varsa bize liste şeklinde geri döner.Yoksa boş liste şeklinde döner.

# Regular Expresssion ifadelerini öğrendikten sonra RegEx şeklinde de aratabiliriz.


# ----re.split()----

print(re.split(" ",str))
print(re.split("R",str))


#  ----re.sub()----
# substring in kısaltılmasıdır.karakterleri değiştirebiliyoruz.

print(re.sub(" ","-",str))


#  ----re.search()----

result = re.search("Python",str)

print(result)
print(result.start())  #0.karakterden başlıyor
print(result.end())    # 6.karaktere kadar(6.karakter dahil)
print(result.endpos)   # dizedeki toplam karakter sayısını verir.
print(result.group())  # .group() eşleşmelerinin yerlerini içeri
print(result.string)   # .string dönen string değeri yazdırır



# çıktıdaki span ifadesi, aradığımız karakterin string ifadedeki indeks aralığını söyler.
# nitekim çıktıdaki match kısmında da görüldüğü gibi aradığımız karakter Python ve str karkter dizisinde


txt1 = "Bu metin boşluklar içeriyor."
x = re.search("\s", txt1)
print("İlk boşluğun bulunduğu yer kaçıncı karakter?:", x.start())


# search metodunda aradığımız karakter dizede yoksa çıktıda None değeri döner.
txt2 = "Türkiye'de yağmur"
x = re.search("Kanada", txt2)
print(x)


# search ile match arasındaki fark ?

"""
Her ikisi de dizede bulunan bir alt dizenin ilk eşleşmesini döndürür. Ancak
re.search(), dizi çok satırlı olsa bile tüm dizeyi arar ve dizenin tüm satırlarında alt dizenin bir eşleşmesini bulmaya çalışır.
Oysaki re.match() 'ın aramak istediği ilk olarak 2.satırdaysa None değeri döndürür.
"""

Substring ='string'


String1 ='''We are learning regex with geeksforgeeks
		regex is very useful for string matching.
		It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks
		regex is very useful for string matching.
		It is fast too.'''

# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))

# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))



""""
             regular expression
   ------------------------------------------
"""

"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.
         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""

result1 = re.findall("[abc]", str)
result2 = re.findall("[sat]", str)
result3 = re.findall("[a-e]", str)
result4 = re.findall("[a-z]", str)
result5 = re.findall("[0-5]", str)
result6 = re.findall("[^abc]", str)
result7 = re.findall("[^0-9]", str)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print("----"*42)

"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

"""

result8 = re.findall("...", str)
result9 = re.findall("Py..on", str)
print(result8)
print(result9)
print("----"*42)
"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""

result = re.findall("^P", str)
print(result)
print("----"*42)
"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""

result10 = re.findall("t$", str)
result11 = re.findall("saat$", str)
result12 = re.findall("saatt$", str)
print(result10)
print(result11)
print(result12)
print("----"*42)
"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""
result13 = re.findall("sa*t", str)
print(result13)
print("----"*42)
"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

result14 = re.findall("sa+t", str)
print(result14)
print("----"*42)
"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

result15 = re.findall("sa?t", str)
print(result15)
print("----"*42)
"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
result16 = re.findall("a{2}", str)
result17 = re.findall("[0-9]{2}", str)
print(result16)
print(result17)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
               
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    
    \b - Belirtilen karakter kelimenin  başında ya da sonunda mı ?
         \bthe => the kelimenin  başında mı?
         the\b => the kelimenin  sonunda mı?
    
    \B - Belirtilen karakter kelimeninin başında ya da sonunda değil mı ?
         \Bthe => the kelimenin  başında değil mi?
         the\B => the kelimenin  sonunda değil mi?

    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    
    \s - Boşluk karakterlerini arar.  
    
    \S - Boşluk karakterleri dışındakiler.
    
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    
    \W - \w nin tam tersi

"""
