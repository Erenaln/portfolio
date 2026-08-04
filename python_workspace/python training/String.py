# Karakterlerin yan yana gelmesi ile oluşan "text" lere String denir.
# String değişkenler iki şekilde tanımlanabilir tek tırnak içinde 'ABC' ve çift tırnak içinde "ABC" şeklinde tanımlanabilir.

string1 = "Hello World" #bir String değişkendir.
string2 = 'Hello World' #bu da bir string değişkendir.
string3 = 'A' # Tek karakter olsa da bu yine bir String'dir, Python'da ayrı bir 'char' tipi yoktur.
# String değişkenler char değişkenlerin bir araya gelmesi ile oluşan değişken türüdür.

# tek_tirnak = 'Eren's project' # şeklinde yazılırsa hata meydana gelir (baştaki # kaldırılarak hata görülebilir).
# Hatanın sebebi Python 2. tırnaktan sonra String değişkenin kapandığını düşünür ve hata meydana gelir.
# Bu hatadan kaçınmak için \' şeklinde tırnak atlama komutu verebilir veya dış tırnakları çift tırnak yaparak bu hatadan kaçınılabilir.
tek_tirnak = 'Eren\'s Project' # Tırnak atlama
tek_tirnak = "Eren's Project" # Çift Tırnak


# String metotları
text = "Hello World"

# Stringlerin index numaraları 0'dan başlar
# Eğer tersten okunmak istenirse "-" ile işlem yapılmalıdır
print(text[0]) # ilk karakteri yazdırır, sayı arttıkça sona doğru gidilir.
print(text[-1]) # son karakteri yazdırır, sayı arttıkça başa doğru gidilir.

# len(degisken_adi) 
# String değişkeninin uzunluğunu int (sayı) olarak döndürür.
print(len(text)) # şeklinde direkt olarak atama yapmadan konsola yazdırılabilir.

# Eğer bu sayıyı kodun başka bir bloğunda kullanmak üzere bir yerde tutmak istersek atama yapmamız gerekir.
uzunluk = len(text) # uzunluk değişkenine text değişkeninin uzunluğunu = operatörü ile atıyoruz.
print(uzunluk) # daha sonra istersek bu değişken ile değeri konsola yazdırabilir
                # veya
print(uzunluk + 1) # şeklinde amtematiksel işleme tabi tutabiliriz

# type(degisken_adi) 
# değişkenin türünü öğrenmemize yarar.
print(type(uzunluk)) # çıktıda görüleceği üzere uzunluk değişkeninin türü 'int' yani Integer türündedir.


# .capitalize() 
# girilen degiskenin ilk harfini büyütüp diğer harfleri küçültür.
# istenirse değişkene atanabilir veya direkt print fonksiyonu ile konsola yazdırılabilir.
print(text.capitalize()) # direkt konsola yazar.
capitalized_text = text.capitalize() # değişkene atanır.
print(capitalized_text) # değişken konsola yazdırılır.

# .lower() 
# String değişkenin harflerini küçültür.
# istenirse değişkene atanabilir veya direkt print fonksiyonu ile konsola yazdırılabilir.
print(text.lower()) # direkt konsola yazar.
lowered_text = text.lower() # değişkene atandı.
print(lowered_text) #değişken konsola yazdırıldı.

# .upper() 
# String değişkenin harflerini büyütür.
# istenirse değişkene atanabilir veya direkt print fonksiyonu ile konsola yazdırılabilir.
print(text.upper()) # direkt konsola yazar.
uppered_text = text.upper() # değişkene atanır.
print(uppered_text) # değişken konsola yazdırılır.

# .count("aranan", start, end)  
# String değişkenin içinde aranan karakterden kaç tane olduğu bilgisini integer olarak döndürür.
# start, end değerleri başlangıç ve bitiş aralığını belirler.
print(text.count("l", 0, 3)) # start dahil edilir ve girilen değerden başlanır ama end dahil edilmez end değeri - 1 gibi düşünülebilir.
# işleme tabi tutulmak istenirse değişkene atama yapılabilir.
aranan_count = text.count("l", 0, 3)
print(aranan_count)

# .startswith("aranan", start, end) 
# String değişkeninin aranan ile başlayıp başlamadığına bakar ve buna göre True veya False döndürür.
# start, end ile belirli bir aralıkta arama yapılabilir.
print(text.startswith("Hel"))

# .endswith("aranan", start, end) String değişkeninin aranan ile bitip bitmediğne bakar ve buna göre True veya False döndürür.
# start, end ile belirli bir aralıkta arama yapılabilir.
print(text.endswith("rld"))

# .find("aranan", start, end) 
# String değişken içerisinde "aranan"ın konumunu bulur ve başlangıç indeksini döndürür.
# eğer bulamazsa sonucu -1 olarak döndürür.
print(text.find("ell")) # e 1. index

# .index("aranan", start, end)
# String değişken içerisinde "aranan"ın konumunu bulur, bulamazsa hata verir.
# .find() ile arasındaki fark hata vermesidir.
print(text.index("llo"))

# .islower()
# String değişkenin harflerinin hepsinin küçük olup olmadığına bakar.
# Küçük ise True değil ise False döndürür.
print(text.islower())

# .isupper()
# String değişkenin harflerinin hepsinin büyük olup olmadığına bakar.
# Büyük ise True değil ise False döndürür.
print(text.isupper())

# .isnumeric()
# String değişkenin içeriğindeki tüm karakterleri rakam mı diye bakar.
# Rakam ise True değil ise False döndürür.
print(text.isnumeric())

# .isalpha()
# String değişkenin içeriğindeki tüm karakterler alfabetik mi diye bakar.
# Alfabetik ise True değil ise False döndürür.
# Boşluk (" ") karakteri alfabetik sayılmaz ve bulunuyorsa False döner.
print(text.isalpha())

# .replace("eski", "yeni")
# String değişken içerisindeki karakterleri veya metin bölümlerini değiştirmek için kullanılır.
print("İstanbul")
print("İstanbul".replace("İ", "i"))
print("Ankara")
print("Ankara".replace("Ankar", "Burs")) # "Ankar" yerine "Burs" yazıldı.

# .split()
# String bir ifadeyi belirli bir karaktere göre parçalar ve bir liste döndürür.
# argüman girilmezse varsayılan olarak boşluğa (" ") göre parçalama yapar.
print(text.split())

# .join()
# Belirli bir ayırıcı kullanarak ("," gibi) dizi, liste elemanlarını birleştirmek için kullanılır.
liste = ["istanbul", "ankara", "izmir"]
sehirler = ", ".join(liste)
print(sehirler) # Dikkat! parantez içerisine liste yazılırsa işlem görünmez, işlemi atadığımız değişkeni (sehirler) yazmalıyız.

# .strip()
# String ifadenin sağ ve sol kısımlarında bulunan boşluk (WhiteSpace) karakterini siler
# whiteSpace karakterler boşluk, newline, tab vb.
strip_text = "    text    "
print(strip_text.strip())
# .lstrip() ile sadece sol .rsplit ile sadece sağ taraftaki boşlukları silmek için kullanılabilir. l = left r = right.