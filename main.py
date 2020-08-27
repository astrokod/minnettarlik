import p5

# Bitkinin dalları için, a.ı ve uzunluk değeri
aci = 0.2
uzuluk = 15

# Her frame için yeni ismim elde etmek için kullanılacağımız sayac değeri
sayac = 0

# Tüm isimleri tuttuğumuz değişken
isimler = None


# Override etmek için yazdoğımız setup fonksiyonu
def setup():
    # isimler adlı değikeni düzenleyebilmek için global
    global isimler

    # Pencere boyutu ayarla
    p5.size(1920, 1080)
    # isimler listesini al
    isimler = isimleri_al()

    # çizgi rengi belirle
    p5.stroke(p5.Color(41, 255, 41, 41))
    # çizgi kalınlığı belirle
    p5.stroke_weight(3)


# draw fonksiyonunu override et
def draw():
    # sayac değikenini düzenlemek için global
    global sayac
    # Eğer ilk framede isek, arka planı siyah yap
    if sayac == 0:
        p5.background(p5.Color(0, 0, 0))

    # isimlerin sayacinci elemanını al
    isim = isimler[sayac]

    # 0, 0 noktasını ekranın sol üst köşesine taşı (resetleme)
    p5.reset_matrix()
    # 0, 0 noktasını ekranın x ekseninnde orta, y ekseninde alt tarafa taşı
    p5.translate(1920/2, 1080-50)

    # isim deki her harf için döngü başlat
    for harf in isim:
        # harfın ascii değerine bak.
        if ord(harf) % 2:
            # Çift ise pozitif yönde aci kadar dön
            p5.rotate(aci)
        else:
            # Tek ise negatif yönde aci kadar dön
            p5.rotate(-aci)

        # 0, 0'dan y yönünde uzunluk kadar br çizgi çiz
        p5.line(p5.Vector(0, 0), p5.Vector(0, -uzuluk))
        # 0, 0 noktasını çizilen çizginin son noktasına taşı
        p5.translate(0, -uzuluk)

    # Eğer sayac isimlerin uzunluğundan bir eksik ise
    if sayac == len(isimler) - 1:
        # Bitti yaz ve p5, döngüsünü durdur
        print("Bitti")
        p5.no_loop()
    else:
        # değilse, sayac'ı bir arttır
        sayac += 1



# İsim lisetesini almak için fonksiyon
def isimleri_al():
    # bos bir liste olsutur
    tum_isimler = []
    # isimlerin bulunduğu dosyayı aç
    with open("veri/isimler.dat", "r") as dosya:
        # Dosyaının satırları içinde döngü başlat
        for satir in dosya:
            # her satırın ilk elemanını al. ","e göre bölünmüş
            tum_isimler.append(satir.strip().split(",")[0])

    # tüm isimler listesini return et
    return tum_isimler


if __name__ == "__main__":
    # p5'i çalıştır
    p5.run()
