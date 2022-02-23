"""
    Ingresar a la pagina. buscar un producto y agregarlo al carrito
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import data


class NisseiBot:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://nissei.com/py/customer/account/login/')
        try:
            sleep(7)
            bot.find_element(by='id', value='btn-cookie-allow').click()
            captcha = bot.find_element(
                by='class name', value='grecaptcha-badge')
            if captcha:
                email = bot.find_element(by='id', value='email')
                email.clear
                email.send_keys(self.username)

                sleep(2)
                password = bot.find_element(by='id', value='pass')
                password.clear()
                password.send_keys(self.password)
                password.send_keys(Keys.RETURN)
        except:
            bot.close()

    def home_page(self):
        bot = self.bot
        bot.find_element(by='class name', value='img-fluid').click()
        sleep(3)
        bot.execute_script("window.scrollTo(0, 1000)")
        sleep(2)
        bot.find_element(by='class name', value='product-item-link').click()

    def add_to_cart(self):
        bot = self.bot
        bot.find_element(by='id', value='product-addtocart-button').click()
        sleep(2)
        # Ir a carrito
        bot.get('https://nissei.com/py/checkout/cart/')
        sleep(4)
        # Finalizar pedido
        bot.get('https://nissei.com/py/checkout/')

    def logout(self):
        bot = self.bot
        bot.get('https://nissei.com/py/customer/account/logout/')


bot = NisseiBot(username=data['username'], password=data['pass'])
bot.login()
sleep(3)
bot.home_page()
sleep(3)
bot.add_to_cart()
sleep(2)
bot.logout()
