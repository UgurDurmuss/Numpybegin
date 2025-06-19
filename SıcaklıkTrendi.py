import numpy as np
'''
Amaç: Rastgele üretilen günlük sıcaklık verileri ile (örneğin 30 gün) farkları bul.
'''
def big_num(news):
    big_score=news[0]
    for i in range(len(news)):
        if news[i]>big_score:
            big_score=news[i]
    return big_score
def big30(new):
    en_sicak=[]
    for i in range(len(new)):#range her zaman tam sayı bekler unutma
        if new[i]>30:
           en_sicak.append(new[i])
    return en_sicak




my_array=np.random.normal(25,5,5)#ortalaması 25 standart sapması 5 olan 10 tane sayı üreteceğiz
#bu kısmın randintten farkı sayıların float olarak çıkabilmesi,ortalamaya yakın sık değerlerin çıkması ve günlük hayata daha yakın olması
dif=np.diff(my_array)#bir önceki güne göre farkları alır
print(f"5 günlük sıcaklıklar={my_array}")
print(f"bir önceki güne farklar={dif}")

ort=np.mean(my_array)
enBuyukFark=big_num(list(dif))
buyuk_30=big30(list(my_array))
sirali_sicakliklar=np.sort(my_array)
max_term=np.max(sirali_sicakliklar)
min_term=np.min(sirali_sicakliklar)

print(f"sıcaklık ortalaması={ort}")
print(f"sıcaklıklar arasındaki en büyük fark={enBuyukFark}")
print(f"en sıcak günler={buyuk_30}")
print(f"büyükten küçüğe sıcaklıklar={sirali_sicakliklar}")
print(f"maksimum sıcaklık={max_term} ve minimum sıcaklık={min_term}")
