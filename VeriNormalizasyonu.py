import numpy as np
from numpy.ma.core import append

giris = input("Virgülle ayırarak sayı girin: ")  # örnek: 12.5,3.4,5.0
veriler = [float(x.strip()) for x in giris.split(",")]#split stringlerle çalışıyor,değerleri aldık strip ile boşlukları silip float olarak kaydettik
new_array=np.array(veriler)#numpy dizisi dönüşümü
print("Girilen sayılar:", veriler)

ortalama=np.mean(new_array)#girilecek sayıların ortalaması
standart_sapma=np.std(new_array)#standart sapma
en_kucuk=np.min(veriler)
en_buyuk=np.max(veriler)

#min max normalizasyonu
minmaxnorm=[]
for num in veriler:
    num=(num-en_kucuk)/(max-min)
    minmaxnorm.append(num)

print(f"min-max Normalizasyonu={minmaxnorm}")

#Z-Score Normalizasyonu
zccorenorm=[]
for num in veriler:
    num=(num-ortalama)/(standart_sapma)
    zccorenorm.append(num)

print(f"min-max Normalizasyonu={minmaxnorm}")
print(f"Z-Score Normalizasyonu={zccorenorm}")





