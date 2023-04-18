"""

     Python'da Aritmetik(Arithmetic) Operatörler
    ---------------------------------------------
Python Aritmetik işleçleri toplama, çıkarma, çarpma ve bölme gibi temel matematiksel işlemleri gerçekleştirmek için kullanılır .


+	Toplama: iki işleneni toplar	x + y
–	Çıkarma: iki işleneni çıkarır	x – y
*	Çarpma: iki işleneni çarpar	x * y
/	Bölme (kayan nokta): birinci işleneni ikinciye böler	x / y
//	Bölme (zemin): birinci işleneni ikinciye böler. Tam kısmı alır. x // y
%	Katsayı: birinci işlenen ikinciye bölündüğünde kalanı verir	x % y
**	Güç: ilk işlenin üssü 2.işlenendir.	x ** y



Python'da Aritmetik Operatörlerin Önceliği

P - parantezler
E – Üs Alma
M – Çarpma (Çarpma ve bölme aynı önceliğe sahiptir)
D – Bölüm
A – Toplama (Toplama ve çıkarma aynı önceliğe sahiptir)
S – Çıkarma
"""

#Float division

print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)


#Integer division( Floor division)

print(10//3)
print(-5//2)
print(5.0//2)
print(-5.0//2)
print(-12//5)

"""
      Python'da Karşılaştırma(Comparison ) Operatörleri
    ----------------------------------------
Python'da ilişkisel operatörlerin karşılaştırılması değerleri karşılaştırır.Koşula göre True veya False döndürür .

>	Büyüktür: Sol işlenen sağdan büyükse doğrudur	x > y
<	Küçüktür: Sol işlenen sağdan küçükse doğrudur	x <y
==	Eşittir: Her iki işlenen de eşitse doğrudur	x == y
!=	Eşit değil – İşlenenler eşit değilse doğrudur	x != y
>=	Sol işlenen sağdan büyük veya ona eşitse True'dan büyük veya eşittir	x >= y
<=	Sol işlenen sağdan küçük veya ona eşitse True'dan küçük veya ona eşit	x <= y

= bir atama operatörü ve == karşılaştırma operatörüdür.

Python'da karşılaştırma işleçleri, aritmetik işleçlerden daha düşük önceliğe sahiptir. Karşılaştırma operatörleri 
içindeki tüm operatörler aynı öncelik sırasına sahiptir.

"""

a = 13
b = 33

# a > b is False
print(a > b)

# a < b is True
print(a < b)

# a == b is False
print(a == b)

# a != b is True
print(a != b)

# a >= b is False
print(a >= b)

# a <= b is True
print(a <= b)



"""
    Python'da Mantıksal(Logical) Operatörler
 -------------------------------------------------

Python Mantık operatörleri , Logical AND , Logical OR ve Logical NOT işlemlerini gerçekleştirir . 
Koşullu ifadeleri birleştirmek için kullanılır.




and	Logical AND: Her iki işlenen de doğruysa doğrudur.	x and y
or	Logical OR: İşlenenlerden biri doğruysa doğrudur.  	x or y
not	Logical NOT: İşlenen yanlışsa doğru. 	            not x


Python'da Mantıksal Operatörlerin Önceliği:
1) logical not
2) logical and
3) logical or

"""

# Examples of Logical Operator
a = True
b = False

# Print a and b is False
print(a and b)

# Print a or b is True
print(a or b)

# Print not a is False
print(not a)

"""

      Python'da Bitsel(Bitwise) Operatörler
   -------------------------------------------------

Python Bitwise operatörleri, bitler üzerinde hareket eder ve bit-bit işlemleri gerçekleştirir. Bunlar ikili sayılar üzerinde işlem yapmak için kullanılır.

&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<


Python'da Bitsel Operatörlerin Önceliği:

1) Bitwise NOT
2) Bitwise Shift
3) Bitwise AND
4) Bitwise XOR
5) Bitwise OR




"""

# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


"""
        Python'da Atama (Assignment) Operatörler
   -------------------------------------------------
   
=	İfadenin sağ tarafındaki değeri sol taraftaki işlenene atayın 	                                    x = y + z
+=	AND ekle: Sağ taraftaki işleneni sol taraftaki işlenenle ekleyin ve ardından sol işlenene atayın	a+=b a=a+b
-=	Çıkart VE: Sağ işleneni sol işlenenden çıkar ve ardından sol işlenene ata	                        a-=b a=ab
*=	Çarp VE: Sağ işleneni sol işlenenle çarp ve ardından sol işlenene ata	                            a*=b a=a*b
/=	Böl VE: Sol işleneni sağ işlenenle bölün ve ardından sol işlenene atayın	                        a/=b a=a/b
%=	Modül AND: Sol ve sağ işlenenleri kullanarak modülü alır ve sonucu sol işlenene atar	            a%=b a=a%b
//=	Böl(zemin) VE: Sol işleneni sağ işlenenle bölün ve ardından değeri(kat) sol işlenene atayın	        a//=b a=a//b
**=	Üs VE: İşlenenleri kullanarak üs (gücü artır) değerini hesaplayın ve sol işlenene değer atayın  	a**=b a=a**b
&=	İşlenenlerde Bitsel AND gerçekleştirir ve sol işlenene değer atar	                                a&=b a=a&b
|=	İşlenenlerde Bitsel OR gerçekleştirir ve sol işlenene değer atar	                                a|=b a=a|b
^=	İşlenenlerde Bitwise xOR gerçekleştirir ve sol işlenene değer atar	                                a^=b a=a^b
>>=	İşlenenlerde Bit yönünde sağa kaydırma gerçekleştirir ve sol işlenene değer atar	               a>>=b a=a>>b
<<=	İşlenenlerde Bit yönünde sola kaydırma gerçekleştirir ve sol işlenene değer atar	            a<<= b    a= a << b
"""


# Examples of Assignment Operators
a = 10

# Assign value
b = a
print(b)

# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# bitwise lishift operator
b <<= a
print(b)

"""

      Python'da Identity(Kimlik) ve Membership(Üyelik) Operatörler
   -----------------------------------------------------------------

Python'da, is ve is not kimlik işleçlerinin her ikisi de 
iki değişkenin aynı nesneye atıfta bulunup bulunmadığını test etmek için kullanılır.

İki değişkenin eşit olup olmadığını test etmek için == operatörünü kullanın.
Eşit olan iki değişken, aynı oldukları anlamına gelmez.

ÖNEMLİİİİ !!!

Verilerimiz Value data type (örneğin; string,number vs) ise, sonucun True olması için tanımlanan iki değişkenin birbirine eşit olması yeterlidir.
Ancak tanımladığımız değişkenlerin veri tipleri Reference data type (örneğin;list) ise is operatörüyle ilişkilendirdiğimizde sonucun True çıkması
için birbirine atanmaları gerekir. Yani eşit olmaları bile sonucun False olmasına sebep olur.


is         
is not      


Python'da in ve not in , bir değerin veya değişkenin bir sırada olup olmadığını test etmek için kullanılan üyelik işleçleridir.

in         
not in     


"""

a = "Ali"
b = "Ali"
print(a is b)


c = "Ada"
d = "Ade"
d = c
print(c is d)


e = 5
f = 5
print(a is b)

g = 6
h = 4
g = h
print(g is h)


k = [1,2,3]
l = [1,2,3]

print(k is l)

m = [1,2,3,4]
n = [1,2,3,4]
n = m
print(m is n)


# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")


if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")


"""
         Python'da Üçlü Operatörler
   ----------------------------------------
   
Python'da, koşullu ifadeler olarak da bilinen Üçlü işleçler , bir koşulun doğru veya yanlış olmasına göre bir şeyi değerlendiren işleçlerdir. 2.5 sürümünde Python'a eklendi. 

Basitçe, kodu kompakt hale getiren çok satırlı if-else yerine tek bir satırda bir koşulu test etmeye izin verir .

Sözdizimi:   [on_true] if [expression] else [on_false] 
   
   
"""

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)


"""
       Python'da Operatörlerin Önceliği ve İlişkilendirilebilirliği
     ------------------------------------------------------------------
Python'da Operatör önceliği ve ilişkilendirilebilirlik , operatörün önceliklerini belirler.
Bu, hangi işlemin önce gerçekleştirileceğini belirlemek için farklı önceliğe sahip birden fazla işleç içeren bir ifadede kullanılır.



 Operatörler	                                        Anlam
---------------                                      ------------

()	                                                Parantez
**	                                                   üs
+x, -x,~x	                             Tekli artı, Tekli eksi, Bitsel DEĞİL
*, /, //,%       	                         Çarpma, Bölme, Kat bölme, Modül
+,-	                                              Ekleme çıkarma
<<,>>	                                      Bitsel kaydırma işleçleri
&	                                             bit düzeyinde VE
^	                                               bit düzeyinde XOR
|	                                                 bitsel VEYA
==, !=, >, >=, <, <=, is, is not, in,not in	    Karşılaştırmalar, Kimlik, Üyelik işleçleri
not	                                                mantıksal DEĞİL
and                                              	mantıksal VE
or	                                                 mantıksal VEYA
"""

# Precedence of '+' & '*'
expr = 10 + 20 * 30
print(expr)

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
	print("Good Bye!!")


"""
     Python'da Bölme Operatörleri
   ---------------------------------

(i) Float division: 
Bu operatör tarafından getirilen bölüm, iki sayının tamsayı olup olmadığına bakılmaksızın her zaman bir kayan sayıdır.


(ii) Integer division( Floor division): 
Bu operatör tarafından döndürülen bölüm, iletilen bağımsız değişkene bağlıdır. Sayılardan herhangi biri değişken ise,
çıktıyı değişken olarak döndürür. Kat bölümü olarak da bilinir, çünkü herhangi bir sayı negatifse çıktı tabana bölünür.



"""

print(5/5,10/2,-10/2,20.0/2)


print(5.0/2)
print(-5.0/2)


print(5//2)
print(-5//2)
print(5.0//2)
print(-5.0//2)
