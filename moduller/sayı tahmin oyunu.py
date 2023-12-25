import random
import time
print("********************************\nsayı tahmin oyunu\n1-40 arasında bir sayı tutun\n5 hakkınız vardır.\n********"
      "************************")
rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 5
while True:
    tahmin = int(input("1 ile 40 arasında bir sayı tutun:"))
    if(rastgele_sayı > tahmin):
        print("bilgiler kontrol ediliyor....")
        time.sleep(1)
        print("daha yüksek bir sayı tahmin edin")
        tahmin_hakkı -= 1
    elif(rastgele_sayı < tahmin):
        print("bilgiler kontrol ediliyor....")
        time.sleep(1)
        print("daha düşük bir sayı tahmin edin")
        tahmin_hakkı -= 1
    else:
        print("tebrikler doğru tahmin")
        break
    if(tahmin_hakkı == 0):
        print("tahmin hakkınız bitmiştir.\nsayımız:",rastgele_sayı)
        break