import secondaryProgress
import database


def project(name, surname, mail):
    print("""
Hoşgeldiniz!!! Lütfen sizin için uygun olan işlem numarasını giriniz!

1-Ürün Araması
2-Ürünun Daha Önce Kaydedilmiş Fiyat Listesi
3-Kaydedilmiş Bütün Ürünlerin Fiyat Listesi
4-İşlemi sonlandır
""")
    numberOfOperation = int(input("İşlem numarası :\n"))
    nameOfProduct = str(input("Ürün Adı:\n"))
    if numberOfOperation == 1:
        productlist = secondaryProgress.searchProductOnSite(nameOfProduct)  # Ürünü ismine göre sitede aratma
        print("""
Lütfen sıradaki işlem numarasını giriniz!

1-{} ürününü listeye kaydet
2-{} ürününü eski fiyatlarıyla karşılaştır
3-İşlemi sonlandır
""".format(nameOfProduct, nameOfProduct))
        try:
            numberOfOperationInside = int(input("Islem Numarasi :"))
            if numberOfOperationInside == 1:
                database.saveNewProduct(name, surname, mail, productlist)
            elif numberOfOperationInside == 2:
                database.showOldSavedDataOfProduct(mail, productlist[0])
            elif numberOfOperationInside == 3:
                secondaryProgress.exit(mail)
            else:
                print("Geçersiz işlem çıkışınız yapılıyor...")
        except Exception as ex:
            print(ex)
        finally:
            contProcess = str(input("Başka bir işlem yapmak ister misiniz? (Yes/No)")).upper()
        while contProcess == "YES":
            project(name, surname, mail)
    elif numberOfOperation == 2:
        database.showOldSavedDataOfProduct(mail,
                                           nameOfProduct)  # Ürünü ismine göre saklanan verilerden tarihlerine göre fiyat listesini çekme
    elif numberOfOperation == 3:
        numberOfOperationInside = int(input("İslem Numaranızı giriniz(Ana Menü:1 / Çıkış:2) :"))
        if numberOfOperationInside == 1:
            project(name, surname, mail)
        elif numberOfOperationInside == 2:
            secondaryProgress.exit(mail)
        else:
            print("Geçersiz işlem çıkışınız yapılıyor...")
            secondaryProgress.exit(mail)
    elif numberOfOperation == 4:
        secondaryProgress.exit(mail)
    else:
        print("Lütfen geçerli bir işlem numarasi seçiniz!!!")
        project(name, surname, mail)
