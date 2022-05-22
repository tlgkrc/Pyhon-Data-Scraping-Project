import User
import database
import innerMenu
import secondaryProgress


def projectTester():
    print("""
    Hoşgeldiniz...
    Üye iseniz lütfen giriş yapınız.Üye değilseniz lütfen giriş yapabilmek içi kayıt olunuz...

    1.Oturum Aç
    2.Kayıt Ol
    3.Çıkış
    """)
    try:
        selectedOption = int(input("Yapılacak işlem numarasını giriniz : "))
        if selectedOption == 3:
            secondaryProgress.exit1()
        else:
            mail = input("Mail adresinizi giriniz...\n")
            password = input("Lutfen sifrenizi giriniz...\n")
            newUser = User.User(mail, password)
            if selectedOption == 1 and newUser.isMailExist(mail):
                if newUser.isExistAccount(mail, password):
                    listOfUserInfo = database.getNameAndSurname(mail)
                    print(listOfUserInfo)
                    name = listOfUserInfo[0]
                    surname = listOfUserInfo[1]
                    innerMenu.project(name, surname, mail)
            elif selectedOption == 2 and not newUser.isMailExist(mail):
                newUser.createUser(mail, password)
                name = str(input("Lutfen isminizi giriniz!!!"))
                surname = str(input("Lutfen soyisminizi giriniz!!!"))
                innerMenu.project(name, surname, mail)
            else:
                print("Lutfen gecerli bilgiler giriniz!!!")
                projectTester()
    except Exception as ex:
        print(ex)


projectTester()
