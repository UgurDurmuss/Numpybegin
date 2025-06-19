import numpy as np
'''
Amaç: numpy.random ile 1000 defa zar atıp sonuçları tut ve hangi sayının daha çok geldiğini görmek
'''

# Fonksiyon: Verilen listede en sık tekrar eden elemanı döndürür
def most_frequent(List):
    counter = 0  # En yüksek frekansı saklamak için sayaç başlangıcı
    num = List[0]  # En sık bulunan değeri tutmak üzere ilk elemanı atıyoruz

    # Listedeki her bir öğe için frekansını kontrol et
    for i in List:
        curr_frequency = List.count(i)  # 'i' değerinin listede kaç kere geçtiğini say
        if curr_frequency > counter:  # Eğer bu öğe önceki en yükseğinden daha sıksa
            counter = curr_frequency  # counter'ı yeni frekansa güncelle
            num = i  # num'u bu yeni en sık olan öğeye güncelle

    return num  # Döngü tamamlandığında, en sık eleman variable 'num' içinde


membranes = np.random.randint(1, 7, size=10)  # 1 ile 6 arasında 10 zar atımı
tekil=np.unique(membranes)#kaç farklı değer olduğunu hesaplar
#count=np.bincount(membranes)#farklı değerlerin kaç defa geçtiğini hesaplar,küçük değerler için mantıklı
#ama büyük değerler için israf


print(f"atılan zarlar={membranes}")
print(f"tekrarsız olarak hangi değerler var={tekil}")

newList=list(membranes)#numpy daki diziler yukarıda ki fonksiyonumuzda count olduğumuzdan işe yaramadı,bizde diziyi normal bir liste çevirdik
most_num=most_frequent(newList)

print(most_num)



