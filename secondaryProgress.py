import time
import datetime
import database
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def searchProductOnSite(nameOfProduct: str):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # chrome un kapanmasini onlemek icin ayarlar duzenlemesi
    try:
        driver = webdriver.Chrome(chrome_options=options, executable_path=r"./drivers/chromedriver.exe")
        time.sleep(2)
        driver.maximize_window()
        url = '-----------------------'
        driver.get(url)
        searchInput = driver.find_element("xpath",
                                          "/html/body/div[1]/div/div/div[3]/div[6]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div[1]/div[2]/input")
        time.sleep(2)
        searchInput.send_keys(nameOfProduct)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)
        while True:
            islemBitti = input("Isleminiz bitti mi?(Evet)").upper()
            if islemBitti == "EVET":
                driver.switch_to.window(driver.window_handles[1])
                listData = getInfoOfProduct(driver)
                return listData
    except Exception as ex:
        print(ex)


def getInfoOfProduct(currentDriver):
    listOfInfo = []
    nameOfProduct = currentDriver.find_elements_by_id("product-name")
    element = nameOfProduct[0].text
    listOfInfo.append(element)

    priceOfProduct = currentDriver.find_elements_by_id("offering-price")
    pOP = priceOfProduct[0].text
    listOfInfo.append(pOP)

    timeOfSearching = datetime.datetime.now()
    listOfInfo.append(str(timeOfSearching))

    urlOfProduct = currentDriver.current_url
    listOfInfo.append(str(urlOfProduct))

    return listOfInfo


def exit(mail):
    database.reportOfLastDay(mail)
    print("Uygulamamızı tercih ettiğiniz için teşekkür ederiz...İyi günler!!!")


def exit1():
    print("Uygulamamızı tercih ettiğiniz için teşekkür ederiz...İyi günler!!!")
