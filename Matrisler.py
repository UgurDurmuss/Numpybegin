import numpy as np

A = np.random.randint(0, 10, size=(3, 3))# başlangıç değeri 0 son değeri sıfır 3x3 lük bir matris
B = np.random.randint(0, 10, size=(3, 3))
A_transpose = A.T#iki farklı yöntemle transpoz alabiliriz,satır ve sutünleri yer değiştirmektir bu
B_transpose = np.transpose(B)
suM=A+B#matrisleri topla,değerleri üst üste basılmış gibi toplanır
multip=np.dot(A,B)#matrisleri çarp
try:
    ters_A = np.linalg.inv(A)#matrisin tersini alma
except np.linalg.LinAlgError:
    print("Bu matrisin tersi yoktur (determinant sıfır).")
try:
    ters_B = np.linalg.inv(B)
except np.linalg.LinAlgError:
    print("Bu matrisin tersi yoktur (determinant sıfır).")

print(f"A matrisi={A}")
print(f"A nın transpozu={A_transpose}")
print(f"A matrisinin tersi={ters_A}")

print(f"B matrisi={B}")
print(f"B nin transpozu={B_transpose}")
print(f"B matrisinin tersi={ters_B}")

print(f"matrislerin toplamı={suM}")
print(f"matrislerin çarpımı={multip}")
