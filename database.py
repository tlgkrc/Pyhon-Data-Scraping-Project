import sqlite3
import datetime


def saveNewProduct(name, surname, mail, productInfo):
    productName = productInfo[0]
    productPrice = productInfo[1]
    searchTime = datetime.datetime.strptime(productInfo[2], '%Y-%m-%d %H:%M:%S.%f')
    productLink = productInfo[3]
    try:
        productData = sqlite3.connect("productData.db")
        crsr = productData.cursor()
        crsr.execute("""CREATE TABLE IF NOT EXISTS productData(isim TEXT,soyisim TEXT,mail TEXT,urunIsmi TEXT,urunFiyati TEXT,
        kayitTarihi NUMERIC ,urunLinki TEXT )""")
        productData.commit()
        productData.close()
    except Exception as ex:
        print(ex)

    try:
        productData = sqlite3.connect("productData.db")
        crsr = productData.cursor()
        newList = [name, surname, mail, productName, productPrice, searchTime, productLink]
        crsr.execute("""INSERT INTO productData VALUES (?,?,?,?,?,?,?)""", newList)
        productData.commit()
        productData.close()
    except Exception as ex:
        print(ex)


def showOldSavedDataOfProduct(mail, productName):
    try:
        productData = sqlite3.connect("productData.db")
        crsr = productData.cursor()
        newList = [mail, productName]
        crsr.execute("""SELECT rowid ,*FROM productData WHERE mail = ? and urunIsmi = ?""", newList)
        items = crsr.fetchall()
        for item in items:
            print(str(item[0]) + ".) " + item[4] + " | " + item[5] + " | " + item[6])
        productData.commit()
        productData.close()
    except Exception as ex:
        print(ex)

def reportOfLastDay(mail):
    try:
        productData = sqlite3.connect("productData.db")
        crsr = productData.cursor()
        now = datetime.datetime.now()
        dt = now.strftime("%Y-%m-%d")
        mailAddress = [mail]
        crsr.execute("""SELECT rowid ,*FROM productData WHERE mail = ?""", mailAddress)
        items = crsr.fetchall()
        counter = 0
        for item in items:
            nTime = str(item[6])
            nDateTime = datetime.datetime.strptime(nTime, "%Y-%m-%d %H:%M:%S.%f")
            actualTime = nDateTime.strftime("%Y-%m-%d")
            if actualTime == dt:
                counter = counter + 1
                print(str(counter) + ".) " + item[4] + " | " + item[5] + " | " + item[6])
        productData.commit()
        productData.close()
    except Exception as ex:
        print(ex)


def getNameAndSurname(mail):
    newList = []
    try:
        productData = sqlite3.connect("productData.db")
        crsr = productData.cursor()
        newList = [mail]
        crsr.execute("""SELECT rowid ,*FROM productData WHERE mail = ?""", newList)
        items = crsr.fetchall()
        for item in items:
            if item[3] == mail:
                newList.append(item[1])
                newList.append(item[2])
                return newList
        productData.commit()
        productData.close()
    except Exception as ex:
        print(ex)
