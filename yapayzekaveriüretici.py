import numpy as np

notes=np.random.randint(0,100,size=(2,2,5))#burda aslında 3 tane 2x5 lik matris oluşturuyoruz
#size=(3,10,5) 3 boyuttan oluşur bu sırasıyla (axis=0,axis=1,axis=2) dir ,hangi veri setinde işlem yapmak istiyorsak o kısımla ilgili veri setini alıyoruz
notes_averageofstudent=np.mean(notes,axis=2)#burda notlarımız 2 . boyutta bulunuyordu yani sütünda
#ayrıca burda her bir öğrencinin not ortalaması ayrı bulunur her öğrenci için bir ortalama olacağım axis=2 düşer axis=0 ile axis=1 kalır
notes_averageofclass=np.mean(notes_averageofstudent,axis=1)#şimdi axis 1 e geçtik yani 1 sınıfa ait olan tüm notlara dolayısıyla sınıf ortalamasını bulacağım


print(f"all notes={notes}")
print(f"students notes average={notes_averageofstudent}")
print(f"class averages={notes_averageofclass}")

print("Sınıf Ortalamaları:")
for  i,ortalama in enumerate(notes_averageofclass):#enumerate sayesinde i'yi index olarak,ortalamayı bu indexe eşitleyen değeri bulduk
    print(f"Sınıf {i+1}: {ortalama:.2f}")
    
en_yuksek = np.argmax(notes_averageofclass) + 1#argmax en yüksek değere sahip olan değerin index'ini verir,index sıfırdan başlar tabi
print(f"En başarılı sınıf: Sınıf {en_yuksek}")
