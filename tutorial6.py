
def myFun(x, y=50,*b,**z):
    print("x: ", x)
    print("y: ", y)
    print(b[1])
    print(z['a'][2])

myFun(1,'c','a','b',a=[1,2,3])




lst = [10, 11, 12, 13, 14, 15]
def ad(x):
    x[0] = 20


ad(lst)
print(lst)



"""
Bu  örnekteki nesnemiz reference veri tipindedir ama fonksiyonla bir bağlantı kuramamıştır.Yani fonksiyonda hiçbir işlemde kullanılmamıştır.Sadece
x adında yeni bir liste oluşturulmuştur burdaki olay dışardaki x i etkilemez. Localde print ile yazdırdığımızda x için yeni liste neyse o çıktıda gösterilir.
"""
def de(x):
    x = [20, 30, 40]
    print(x)


lst = [10, 11, 12, 13, 14, 15]
de(lst)
print(lst)


def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

"""
Pass by Reference or pass by value konusu:

Aşağıda 2 benzer fonksiyon var. ilk örneğe bakacak olursak:

iki parametreyi fonksiyona ilettikden sonra x verisini fonksiyon içindeki işlemle bağlantı kurmuş
oluyoruz.Yani demek istediğim, x verisini y verisine atayarak fonk. dışındaki x listesiyle bağlantı kurmuş oluyoruz çünkü fonksiyon içinde y=x diyerek x i kullanmış oluyoruz.
Tabi y = x diyerek refence ları aynı olmuş oluyor.Daha sonra x veya y nesnesinde değişiklik yaparsak 'fonksiyon içinde x ve y'yi print ile yazdırırsak' x ve y nesneleri refence kuralına
göre değişmiş olur.Fonksiyon dışındaki x ve y nesnelerini yazdırdığımızda ise şöyle bir tabloyla karşılaşmış oluruz;
fonksiyona gönderdiğimiz x ve y verilerinden sadece x verisinde deişiklik yaptığımızdan 'dışardaki print(x)' x nesnesi yazdırıldığında fonksiyon içinde
olduğu gibi değişiklik olur.Fakat y verisini fonksiyonla bağlantı kurmadığı 'y verisini kullanmadığımız' için y nesnesi aynı kalır.


"""
def o(x, y):
    y = x
    x.append(5)
    print(x)
    print(y)


x = [2]
y = [3]
o(x, y)
print(x)
print(y)

""" Bu örnek de üstteki örnekle aynı mantıktadır."""
def p(x, y):
    x = y
    y.append(5)
    print(x)
    print(y)

x = [2]
y = [3]
p(x, y)
print(x)
print(y)


"""" aşağıdaki örneklerdeki dışardaki veriler zaten reference tipteki nesneler olmadığı için x=y olayı bir işe yaramıyor.Ayrıca dışardaki verilerle fonksiyon
arasında bir bağlantı yok."""

def r(x, y):
	temp = x
	x = y
	y = temp

x = 2
y = 3
r(x, y)
print(x)
print(y)


def s(x):
	print(x.replace('A','E'))

x = 'Ali'
s(x)
print(x)




def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3

for value in simpleGeneratorFun():
    print(value)



def g(x):
    yield 1
    yield 2
    yield 3
    yield 4

a = g(x)
print(next(a))
print(next(a))
print(next(a))


a = lambda x: print("Çift sayı") if x%2==0 else print("Tek sayı")

for i in range(10):
    a(i)



numbers = [1, 3, 5, 9, 10, 4]

def square(num):
    return num ** 2


result = list(map(square, numbers))
print(result)

liste = [1,2,3,4,5]
print(list(map(lambda x: x%2==0,liste)))



def divise(x):
    if x%2==0:
        return x

print(list(filter(divise,numbers)))



a=[1,2,3,4,5]

b = iter(a)
print(next(b))
print(next(b))


c = {'a':5,'b':6,'c':7,'d':8,'e':9}

d = iter(c)
print(next(d))
print(next(d))
print(next(d))



c = 7
def a():
    global c
    c = c+5
    print(c)

a()
print(c)

a = 15


# function to change a global value
"""
def change():
    # increment value of a by 5
    b = a + 5
    a = b
    print(a)


change()

output: UnboundLocalError: local variable 'a' referenced before assignment
"""