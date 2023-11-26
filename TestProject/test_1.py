import pytest
import allure
from selenium.webdriver import ActionChains
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


url = 'H:/Sciense/Testing/Diplom/Defense/Sinyakova/cakeNastya-main/index.html'
#adres=''         #ввести почту
#security=''      #ввести пароль


@pytest.mark.usefixtures('setup')
class Test:

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store1(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в каталог'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку детские'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[1]/ul/li[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store2(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в каталог'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[2]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку детские'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[1]/ul/li[2]').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Покупка торта домика'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[2]/div[1]/div/button/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)


    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store3(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в начинки'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку мартини'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[1]/div[4]/div/button/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store4(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в начинки'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку три шоколада'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[2]/div[5]/div/button/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store5(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в начинки'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/ul/li[3]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку медовый'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/section/div[5]/div[2]/div/button/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store6(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в доставки и оплата'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[4]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку заказать'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store7(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в доставки и оплата'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[4]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку адресу'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div[1]/div/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store8(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в контакты'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[5]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку VK'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[2]/div/ul/li[1]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store9(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в контакты'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[5]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку TELEGRAM'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[2]/div/ul/li[2]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.epic('')
    @allure.feature('Тест сайта по продаже тортов')
    @allure.story('Тест заказа торта')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('')
    def test_store10(self):
        with allure.step('Открывает сайт'):
            self.browser.get(url)
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('переход в контакты'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div[2]/ul/li[5]/a').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        with allure.step('Открывает ссылку TELEGRAM'):
            self.browser.find_element(By.XPATH, '/html/body/main/div[2]/div/ul/li[3]/a/img').click()
            allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)





















   # @allure.epic('')
   # @allure.feature('Тест банка')
   # @allure.story('Тест личного кабинета')
   # @allure.severity(allure.severity_level.BLOCKER)
   # @allure.description('')
   # def test_store6(self):
       # with allure.step('Открывает ссылку'):
           # self.browser.get(url)
           # allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       # with allure.step('Открывает ссылку'):
           # self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/ul/li[3]/a').click()
           # allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
       # with allure.step('Открывает ссылку'):
            #self.browser.find_element(By.XPATH, '//*[@id="firstname"]').click()
           # element61 = self.browser.find_element(By.XPATH, '//*[@id="firstname"]').send_keys('Иван')
           # allure.attach(self.browser.get_screenshot_as_png(), name="Screenshot",
                         # attachment_type=AttachmentType.PNG)
        #assert element61 == "Иван", "Ошибка!!!!"


