import functools

print(functools.reduce(lambda a,b:a+b+5,[i for i in range(1,6)]))

"""
işlem şu şekilde oluyor:
1+2+5 = 8   --> 1 ve 2 elemanlarını kullandık.
8+3+5 = 16  --> 3 elemanını ....
16+4+5 = 25 
25+5+5 = 35
"""
print("\n")



"""

  open() işlevinin çalışması
-------------------------------
Dosya üzerinde okuma yazma gibi herhangi bir işlem yapmadan önce o dosyayı açmamız gerekiyor.
Bunun için Python'un yerleşik fonksiyonu open()'u kullanmalıyız, ancak açılış sırasında, açılış dosyasının amacını temsil eden modu belirtmeliyiz.


f = open(filename, mode)

filename: Dosya, Python betiği ile aynı dizinde bulunmalıdır, aksi takdirde dosyanın tam adresi yazılmalıdır.
Dosya mevcut değilse, dosyanın mevcut olmadığına dair bir hata oluşturulur


r: okuma işlemi için mevcut bir dosyayı açın.
w: yazma işlemi için mevcut bir dosyayı açar. Dosya zaten bazı veriler içeriyorsa geçersiz kılınır, ancak dosya yoksa dosyayı da oluşturur.
a:   ekleme işlemi için mevcut bir dosyayı açın. Mevcut verileri geçersiz kılmaz.
r+:  Dosyaya veri okumak ve yazmak(ilk satırdan başlar ve hangi karakteri eklediysek önceki karakterle değişir.) için. Dosyadaki önceki veriler geçersiz kılınacaktır.
w+: Veri yazmak ve okumak için. Mevcut verileri geçersiz kılacaktır.
a+: Dosyaya veri eklemek ve okumak için. Mevcut verileri geçersiz kılmaz.


read() :  Okunan baytları bir dize biçiminde döndürür. n bayt okur, n belirtilmemişse, tüm dosyayı okur.  File_object.read([n])

readline() :  Dosyanın bir satırını okur ve string biçiminde döndürür.Belirtilen n için en fazla n bayt okur. 
ancak, n satırın uzunluğunu aşsa bile birden fazla satır okumaz.  File_object.readline([n])

readlines() :  Tüm satırları okur ve her satırı listedeki bir dize öğesi olarak döndürür.  File_object.readlines()

write() :  Str1 dizesini metin dosyasındaki tek bir satıra ekle.  File_object.write(str1)

writelines() : Dize öğelerinin listesi için, her dize metin dosyasına eklenir. Aynı anda birden fazla dizi eklemek için kullanılır.  File_object.writelines(L) for L = [str1, str2, str3] 

tell():  Python programlamada, dosya işleme kavramı içinde tell() işlevi, dosya nesnesinin gerçek konumunu elde etmek için kullanılır. 
Dosya nesnesi ile bir imleci kastediyoruz. 


seek():  Dosya nesnesinin konumunu gerekli konuma kaydırmak/değiştirmek için seek() işlevi kullanılır. 
Dosya nesnesi ile bir imleci kastediyoruz. 


"""



"""
write() ve writelines() arasındaki fark nedir?
Ne işe yararlar?
"""
file1 = open("createfile1.txt","w",encoding="utf-8")    # encoding = "utf-8"  : dosyadaki türkçe karakterler bazen değişik gözükebiliyor.Buna engel olmak için kullanılır.
file1.write("Dogukan Sürücü\n2001 Şubat 9\nFenerbahçe")
file1.close()


x = ['a','b','c','d']
file2 = open("createfile2.txt","w",encoding="utf-8")
for i in x:
    file2.writelines(i)
file2.close()

y = ['a\n','b\n','c\n','d\n']
file3 = open("createfile3.txt","w",encoding="utf-8")
for i in y:
    file3.writelines(i)
file3.close()


"""
read() ve readlines() nedir?
aralarındaki farklar nelerdir?
"""
file1_1= open("createfile1.txt","r",encoding="utf-8")
print(file1_1.read())

file1_1 = open("createfile1.txt","r",encoding="utf-8")
print(file1_1.readlines())



"""
Bir txt dosyasındaki verileri for döngüsüyle yazdırma          ### Akıldaki önemli soruları giderme
"""
a = open("createfile2.txt","r",encoding="utf-8")
for each in a:
    print(each)       # textin içeriği: abcd
                      # txt dosyasından satır sonuna kadarki karakterleri sırasıyla alır. ilk satır abcd
a.close()

exapmle = open("createfile1.txt","r",encoding="utf-8")
for i in exapmle:
    print(i)

b = open('2 sayının toplamı ve çıkan sonuç ile 2 arasında sayıların asallarını bulma', 'r')
for each1 in b:
    print(each1)       # textin içeriği  2
#                                        3
#                                        5
#                                        7
b.close()
                       # hemen üstteki koddan farkı txt dosyasında satır sonunda gizli /n (kod mantığında) olmasıdır.
#                                                                                          |
#                                                                                          |
#                         <<<<<<<-----------------------------------------------------------
# bilgiyi destekleyecek bilgi
liste = ['a','b','c']
for i in liste:
    print(i+"\n")


# aradaki boşluk satırlarını ortadan kaldırmak için end parametresi güzel fikir.
b = open('2 sayının toplamı ve çıkan sonuç ile 2 arasında sayıların asallarını bulma', 'r')
for each2 in b:
    print(each2,end="")

b.close()


print("\n")

exapmle = open("createfile1.txt","r",encoding="utf-8")
print(exapmle.read(16))    # dosyadaki verinin ilk 16 karakterini okumamızı ister.


print("\n")
print("\n")

#KONUYU ÖZETLEYECEK GÜZEL ÖRNEK-1

file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()


file1.seek(0)   # İMLECİ 1.KARAKTERDEN İTİBAREN BAŞLATIR.

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)   # SEEK(0) DEMEMİZİN SEBEBİ read(n) derken sadece ilk n karakteri okuyoruz ve sonra diğer veriler anlık olarka gidiyor.
               # bunu önlemek için seek(0) yapmalıyızki imlec yine ilk karakterden başlasn.

print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))
print()

file1.seek(0)

print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()


print("\n")
print("\n")


#KONUYU ÖZETLEYECEK GÜZEL ÖRNEK-2


L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

with open("myfile.txt", "w") as file1:
    # Writing data to a file
    file1.write("Hello \n")
    file1.writelines(L)

with open("myfile.txt", "r+") as file1:
    print(file1.write("dogukan"))
with open("myfile.txt", "r+") as file1:
    # Reading from a file
    print(file1.read())



print("\n")
print("\n")


#KONUYU ÖZETLEYECEK GÜZEL ÖRNEK-3

file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()


file1 = open("myfile.txt", "a")


file1.write("\n")
file1.write("Today")


file1.write("Tomorrow")

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()


#MASAÜSTÜNDEKİ DOSYAYI OKUMAK VEYA DOSYAYA VERİ EKLEMEK İSTİYORSAK ÖNCELİKLE ADRES YOLUNU YAZMAMIZ LAZIM.
"""
file2 = open(r"D:\Text\MyFile2.txt", "r+")
"""


#ÖRNEK

e = open("createfile2.txt","r",encoding="utf-8")
print(e.read())
 #dosyadaki verinin len'ini bulmak için önce read() deyip veriyi okumamız lazım.Yoksa direkt dosya.tell() dersek her dosya için konum 0 değerini gösterir.

e.seek(2)
print(e.read())
e.seek(0)
print(e.read())


print("\n")

#ÖRNEK
k = open("createfile2.txt","r",encoding="utf-8")
print(k.read(3))
k.seek(0)
print(k.read())
print(k.tell())
k.seek(1)
print(k.read())
print(k.tell()) # tell() , read() gibi seek() fonksiyonundan etkilenmez. Her zaman 'read() fonksiyonundna sonra' dosya verisinin len'ini verir.

"""
print(k.tell())
print(k.seek(1))
print(k.read())
print(k.tell())
"""
