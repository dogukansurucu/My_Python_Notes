"""
      Python'da Kontrol Akışı Türleri
  --------------------------------------------------

Programlama dillerindeki karar verme ifadeleri, program yürütme akışının yönüne (Kontrol Akışı) karar verir.

Python programlama dilinde , kontrol akış deyimlerinin türü aşağıdaki gibidir:

if ifadesi
if-else ifadesi
iç içe if ifadesi
if-elif-else merdiveni

"""


"""
       if statement
  ----------------------
  
if ifadesi, en basit karar verme ifadesidir. Belirli bir ifadenin veya ifade bloğunun yürütülüp yürütülmeyeceğine karar vermek için kullanılır.

syntax:


if condition:
   # Statements to execute if
   # condition is true  
  

Burada, değerlendirmeden sonraki koşul doğru veya yanlış olacaktır. ifade boole değerlerini kabul ediyorsa - değer doğruysa,
altındaki ifadeler bloğunu yürütür, aksi halde yürütmez.

Bildiğimiz gibi, python bir bloğu tanımlamak için girinti kullanır. 
Böylece bir if ifadesi altındaki blok, aşağıdaki örnekte gösterildiği gibi tanımlanacaktır:    


if condition:
   statement1
statement2

# Here if the condition is true, if block 
# will consider only statement1 to be inside 
# its block.


"""

i = 10

if (i > 15):
	print("10 is less than 15")
print("I am Not in if")


"""
    if-else statement
  ---------------------
syntax:


Tek başına if ifadesi bize, bir koşul doğruysa bir ifade bloğu yürüteceğini ve koşul yanlışsa yürütmeyeceğini söyler. 
Ancak, koşul yanlışsa başka bir şey yapmak istiyorsak, if koşulu yanlış olduğunda bir kod bloğunu çalıştırmak için  
if ifadesiyle birlikte else deyimini kullanabiliriz.


if (condition):
    # Executes this block if
    # condition is true
else:
    # Executes this block if
    # condition is false
"""

i = 20
if (i < 15):
	print("i is smaller than 15")
	print("i'm in if Block")
else:
	print("i is greater than 15")
	print("i'm in else Block")
print("i'm not in if and not in else Block")



# Explicit function
def digitSum(n):
	dsum = 0
	for ele in str(n):
		dsum += int(ele)
	return dsum

# Initializing list
List = [367, 111, 562, 945, 6726, 873]

# Using the function on odd elements of the list
newList = [digitSum(i) for i in List if i & 1]

# Displaying new list
print(newList)


"""
    nested-if statement
 -------------------------

İç içe bir if, başka bir if ifadesinin hedefi olan bir if ifadesidir. İç içe if ifadeleri, başka bir if ifadesinin içindeki 
bir if ifadesi anlamına gelir. Evet, Python, if ifadelerini if ​​ifadelerinin içine yerleştirmemize izin verir. 
yani, başka bir if ifadesinin içine bir if ifadesi yerleştirebiliriz.

syntax:


if (condition1):
   # Executes when condition1 is true
   if (condition2): 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here
"""

i = 10
if (i == 10):

    # First if statement
    if (i < 15):
        print("i is smaller than 15")

    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")


"""
      if-elif-else ladder
   -------------------------
Burada, bir kullanıcı birden çok seçenek arasında karar verebilir. if ifadeleri yukarıdan aşağıya doğru yürütülür. 
if'i kontrol eden koşullardan biri doğru olur olmaz, bu if ile ilişkili ifade yürütülür ve merdivenin geri kalanı atlanır. 
Koşullardan hiçbiri doğru değilse, nihai else ifadesi yürütülür.

syntax:


if (condition):
    statement
elif (condition):
    statement 
  . 
  .
  .
  .
else:
    statement



"""


i = 20
if (i == 10):
	print("i is 10")
elif (i == 15):
	print("i is 15")
elif (i == 20):
	print("i is 20")
else:
	print("i is not present")

"""
    Short Hand if statement
  ---------------------------

if bloğu içinde yürütülecek yalnızca tek bir ifade olduğunda, kısa yoldan if kullanılabilir. İfade, if ifadesiyle aynı satıra yerleştirilebilir. 

syntax:


if condition: statement
  
  
"""

i = 10
if i < 15:print("i is less than 15")



"""

    Short Hand if-else statement
  --------------------------------
  
Bu, hem if hem de else bloğunda yalnızca bir ifadenin gerekli olduğu if-else ifadelerini tek bir satıra yazmak için kullanılabilir. 

syntax:


statement_when_True if condition else statement_when_False

"""

i = 10
print(True) if i < 15 else print(False)














