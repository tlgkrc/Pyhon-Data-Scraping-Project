import re
import json


class User:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password

    def isMailExist(self,mail):
        self.mail = mail
        with open("usersData.json") as f:
            readData = json.load(f)
            for i in readData:
                if mail == i["mail"]:
                    return True
        return False

    def isExistAccount(self,mail, password):
        self.mail = mail
        self.password = password
        with open("usersData.json") as f:
            readData = json.load(f)
            for i in readData:
                print(i["mail"])
                print(i["password"])
                while True:
                    if mail == i["mail"] and password == i["password"]:
                        return True
                    else:
                        break
            return False

    def saveUserToJson(self, mail, password):
        self.mail = mail
        self.password = password
        if not self.isMailExist(mail):
            newList = []
            with open("usersData.json") as f:
                readData = json.load(f)
                newList = readData

            newDict = {
                "mail": mail,
                "password": password
            }
            with open("usersData.json", "w") as f:
                try:
                    newList.append(newDict)
                    jsonInfo = json.dumps(newList)
                    f.write(jsonInfo)
                except Exception as ex:
                    print(ex)
                finally:
                    f.close()

    def createUser(self, mail, password):
        self.mail = mail
        self.password = password
        while True:  # mail adresi olusturma kosullari
            try:
                result = re.findall(r"@(.*?).com", mail)
                countCharMailProvider = len(str(
                    result[0]))  # Burada gmail ,hotmail gibi email saglayicilarinin uzanti karakter sayisi hesaplaniyor
            except IndexError:
                continue
            if not re.findall("[@]", mail):
                print("Mail adresi ge??erli de??ildir!!!")
            elif countCharMailProvider < 3:  # @ ile .com arasinda karakter var mi kontrol ediyor
                print("Mail adresi ge??erli de??ildir!!!")
            else:
                print("Mail adresiniz uygundur...")
                break
        while True:  # sifre olusturma kosullari
            if not re.findall("[a-z]", password):
                print("??ifreniz en az bir adet k??????k harf i??ermek zorundad??r!")
            elif not re.findall("[A-Z]", password):
                print("??ifreniz en az bir adet b??y??k harf i??ermek zorundad??r!")
            elif not re.findall("[0-9]", password):
                print("??ifreniz en az bir adet rakam i??ermek zorundad??r!")
            else:
                print("??ifreniz ba??ar??yla kaydedildi...")
                self.saveUserToJson(mail, password)
                break
            password = str(input("Lutfen sifrenizi tekrar giriniz...\n"))
            self.password = password
