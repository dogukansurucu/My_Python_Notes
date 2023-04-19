import requests
import json

"""
HTTP NEDİR ?

Http açılımı, İngilizce “Hyper Text Transfer Protokol”, Türkçesi “Hiper Metin Transfer Protokolü” olarak bilinir.
internet üzerinde yer alan bilgilerin sunuculardan kullanıcılara nasıl aktarımının sağlanacağını gösteren bir internet protokolüdür.

HTTP ‘de 2 adet mesaj formatı vardır:
Bunlar; Request ve Response (HTTP istek ve HTTP tepki-cevap) mesajlarıdır.



API NEDİR ?

API, birden fazla bilgisayar programı ve yazılımının birbiri ile iletişim kurmasını sağlayan yazılım arayüzü olarak tanımlanabilir.



REST API NEDİR ?

Rest, HTTP protokolünü kullanarak, URL adresleri üzerinden veri ve dosya alışverişi sağlayan bir yapıdır.
Rest API ise Rest işlemini yapabilmek için kurgulanmış modüle verilen isimdir.
"""


"""

HTTP İSTEKLERİ

Get = En çok kullanılan istek türüdür. Webdeki verileri çekmenize yarar.
Post = Webdeki sunucuya veri göndermenizi sağlar.
Put = Mevcut bilgileri değiştirmenize yarar.
Delete = Bilgileri siler.

"""

"""
STATUS_CODE methodu:

HTTP durum kodlarını döndürür. HTTP durum kodları aşağıdaki şekildedir:

200 : İstek başarıyla gerçekleşti.
204 : URL'nin geçerli olduğu ve Sunucunun yürütmeyi başarıyla gerçekleştirdiği ancak döndürülecek verisi olmadığı anlamına gelir.
301 : İstenen sayfanın taşındığını döndürür ve o adresi yönlendirir.
400 : Yanlış istek biçimi
401 : İşlem için yetkiniz yok.
403 : Erişim reddedildi.
404 : Kaynağın bulunmadığı veya mevcut olmadığı veya URL'nin geçersiz olduğu anlamına gelir
500 : Sunucu hatası.


ELAPSED methodu:

HTTP isteklerinden sonra dönen cevabın ne kadar sürede döndüğünü bildirir.


"""




r = requests.get('http://httpbin.org/get')

print(r.text,"\n")

print(json.loads(r.text),"\n")
print(r.json())  #genellikle şunu kullanıcaz.

print(r.status_code)

print(r.elapsed)