1-"-----------------------------------------PythonVeriTipleri-------------------------------------------"
# String : Metinsel ifadelerin belirtilmesi icin  'char' veri tiplerinin bir araya gelmesiyle meydana gelen veri tipidir. 

# Integer : Sayısal verileri ifade etmek icin kullanılan veri tipidir. Ondalikli sayilarin ifade edilmesi durumunda sadece sayinin tam kismini alir.

# Float : Reel sayilarin ifade edilmesi icin kullanılır.

# List : Farkli veri tiplerinin sadece tek bir degiskende toplanmasidir.

# Tuple: Farkli veri tiplerinin tek bir degiskende toplanmasina ek olarak bu degiskende herhangi bir degisiklik yapilamamaktadır.

# Dictionary: Birbiri ile iliskisi olan varlıkları bir degiskende yani köseli parantez icinde ifade edilmesidir.

# Boolean : Sadece 1 bit yer kaplayan True veya False olarak ifade edilen veri tipidir.

#2 "Kodlamaio sitesinin anasayfasinda yer alan birbirinden farkli Kurslarin ayri ayri cerveve seklinde siralanmasi bir dizidir. "Bu kurslarin isimlerinin ifade edilmesi metinsel ifade kursun süresi ve zamaninin belirtilmesi ise numerik bir ifadedir"
# string: Sitede kullanılan tüm metinler için string veri tipi kullanılmıştır.
# örneğin; Kurslarım,Kurs Programı
# integer: Sitede derslerde olan ilerlememizi göstermesi için int komutu kullanılmıştır.
# boolean:  "Bitir ve devam et" butonuna tıklanan alan bool veri tipi kullanılmıştır.

#3 print("Sitemize Hoş geldiniz. Yapmak istediğiniz işlem için yukarıda yer alan kutulara tıklayabilirisiniz")

#if ogrenciTamamlamaYuzdesi == 100:
#   print("Kurs Başarıyla Tamamlandı")

#else:
#   print("Kurs Bitmedi")

#if butunKurs == "(Kurs tamamlandı)
#    print("Birinci Odev Tamamlandı")

#else: 
#   print("Birinci Odev tamamlanmadı Lutfen Odevı Yapınız")

#if sifre =="123"
#  print("Giris Basarılı")

#else:
#   print("Yanlis Sifre Girdiniz")




#PyTestDecorators

 # (@pytest.fixture: Bu dekoratör, test fonksiyonlarının ihtiyaç duydukları bağımlılıkları ayarlamak için kullanılır. Örneğin, bir test fonksiyonunun bir veritabanı bağlantısına ihtiyacı varsa, bu bağımlılığı @pytest.fixture ile bir bağımlılık olarak tanımlayabilirsiniz.)

 # (@pytest.mark.parametrize: Bu dekoratör, aynı test fonksiyonunu farklı parametrelerle çalıştırmak için kullanılır. Örneğin, bir fonksiyonun farklı giriş değerlerini test etmek istiyorsanız, @pytest.mark.parametrize kullanarak bu değerleri belirleyebilirsiniz.)

 # (@pytest.mark.skip: Bu dekoratör, belirli bir testin çalıştırılmasını atlamak için kullanılır. Örneğin, bir test henüz tamamlanmadıysa veya hatalar içeriyorsa, bu testi atlamak için @pytest.mark.skip kullanabilirsiniz.)


 # (@pytest.mark.xfail: Bu dekoratör, bir testin başarısız olması beklenen durumlarda kullanılır. Örneğin, bir testin bir hata döndürmesi bekleniyorsa, bu testi @pytest.mark.xfail ile işaretleyebilirsiniz.)

 # ()
 # (@pytest.mark.timeout: Bu dekoratör, bir testin belirli bir zaman sınırı içinde tamamlanmasını sağlar. Örneğin, bir testin 5 saniye içinde tamamlanması gerekiyorsa, @pytest.mark.timeout&#40;5&#41; kullanarak bu sınırı belirleyebilirsiniz.)

 # ()
