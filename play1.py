from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
    "(KHTML, like Gecko) Chrome/15.0.87"
)

class PopCharacter:

    def __init__(self):
        self.current_page = ''
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS(desired_capabilities=dcap)
        self.driver.set_window_size(1120, 550)
        self.curr_city = ''
        self.curr_locale = ''
        self.leisure_act = ''
        self.professional_act = ''
        self.attitude = ''
        self.condition = ''
        self.mood = 200
        self.health = 200
        self.star_quality = 200
        self.cash = 111
        self.achievement_points = 0
        self.online_status = ''

    @staticmethod
    def load_pass():
        """
        read user and pass from file
        """
        with open('userinfo.txt','r') as f:
            login = f.readlines()
        return login

    def login(self):
        """
        login to the site
        """

        self.driver.get("http://www.popmundo.com/")
        assert "Popmundo" in self.driver.title
        user_name = self.driver.find_element_by_id('ctl00_cphRightColumn_ucLogin_txtUsername')
        password = self.driver.find_element_by_id('ctl00_cphRightColumn_ucLogin_txtPassword')
        user_cred = self.load_pass()
        print(user_cred[0].strip())
        print(user_cred[1].strip())
        user_name.send_keys(user_cred[0].strip())
        # user_name.send_keys(Keys.RETURN)
        password.send_keys(user_cred[1].strip())
        vera.driver.get_screenshot_as_file(r'C:\Users\Vladi\Pictures\screenshots\tests\login.png')
        #password.send_keys(Keys.RETURN)
        self.driver.find_element_by_id('ctl00_cphRightColumn_ucLogin_btnLogin').click()
        #assert "No results found." not in self.driver.page_source
        # driver.close()

       
    def read_user_status(self):
        self.curr_city = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[1]/a[contains(@href,"City")]').text
        self.curr_locale = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[1]/a[contains(@href,"Locale")]').text
        self.leisure_act = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[2]/strong[1]').text
        self.professional_act = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[2]/strong[2]').text
        self.attitude = self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl00_lnkAttitude').text
        self.condition = self.driver.find_element_by_xpath('//*[@id="ppm-content"]/div[@class="charMainToolbox"]/table/tbody/tr[2]/td[2]').text
        self.mood = int(self.driver.find_element_by_xpath('//*[@id="ppm-content"]/div[@class="charMainValues"]/table/tbody/tr[1]/td[2]/div').get_attribute('title').strip('%'))
        self.health = int(self.driver.find_element_by_xpath('//*[@id="ppm-content"]/div[@class="charMainValues"]/table/tbody/tr[2]/td[2]/div').get_attribute('title').strip('%'))
        self.star_quality = int(self.driver.find_element_by_xpath('//*[@id="ppm-content"]/div[@class="charMainValues"]/table/tbody/tr[3]/td[2]/div').get_attribute('title').strip('%'))
        cash = self.driver.find_element_by_xpath('//*[@id="ppm-content"]/div[@class="charMainValues"]/table/tbody/tr[4]/td[2]').text.strip(' лв.')
        cash_b = ''
        for i in cash:
            if i.isdigit():
                cash_b += i
            elif i == ',':
                cash_b += '.'
        self.cash = float(cash_b)
        self.achievement_points = self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl00_lnkAchievementPoints').text
        self.online_status = self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl00_lnkOnlineStatus').text
        print(self.curr_city, self.curr_locale, self.leisure_act, self.professional_act)
        print(self.attitude, self.condition)
        print(self.mood, self.health, self.star_quality, self.cash)
        print(self.online_status, self.achievement_points)

    def select_character(self):
        #self.driver.find_element_by_id('ctl00_cphLeftColumn_repCharacters_ctl00_btnChooseCharacter2').click()
        self.driver.find_element_by_xpath('//input[@value="Избери Vera"]').click()

    def page_character(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkCharacter').click()

    def page_start(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkStart').click()

    def page_city(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkCity').click()

    def page_locale(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkLocale').click()

    def page_focus(self):
        """
        first have to be on character page
        """
        self.driver.find_element_by_xpath('//*[@id="mnuToolTipFocus"]/a').click()

    def change_leisure_focus(self, leisure):
        select = Select(self.driver.find_element_by_name('ctl00$cphLeftColumn$ctl00$ddlPriorities'))
        select.select_by_value(str(leisure))
        self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl00_btnSetPriority').click()
        #alert = self.driver.switch_to.alert
        #print(alert.text)
        #alert.accept()

    def change_proffi_focus(self, proffi):
        select = Select(self.driver.find_element_by_name('ctl00$cphLeftColumn$ctl01$ddlWorkTypes'))
        select.select_by_value(str(proffi))
        self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl01_btnSetWorkType').click()
        #alert = self.driver.switch_to.alert
        #print(alert.text)
       # alert.accept()

'''
"0">Приоритет за свободното време
"17">Криене от останалите
"13">Нелегално сваляне на музика
"5">Обикаляне по кръчмите
"9">Общуване с приятели
"19">Посещение на психиатър
"1">Почивка и разпускане
"18">Разхождане
"12">Свирене по улиците
"6">Фитнес тренировки
"4">Ходене по магазините

"0">Приоритет за кариерата
"13">Агитация на масите
"9">Говорене с медиите
"29">Зарязване на всичко
"22">Обществен труд
"3">Отдаване на работата
"2">Писане на песни
"8">Подобряване на умение
"33">Посещаване на курс
"15">Преподаване на умение
"19">Репетиция на сцени
"17">Събиране на цветя
"14">Успокояване на масите
"16">Учене от преподавател/ка

'''


if __name__ == '__main__':
    vera = PopCharacter()

    vera.login()
    vera.driver.implicitly_wait(3)
    vera.driver.get_screenshot_as_file(r'C:\Users\Vladi\Pictures\screenshots\tests\select_character.png')
    print(vera.driver.page_source)
    vera.select_character()
    vera.driver.get_screenshot_as_file(r'C:\Users\Vladi\Pictures\screenshots\tests\char_slected.png')
    vera.page_character()
    vera.driver.implicitly_wait(3)
    #vera.page_start()
    #vera.driver.implicitly_wait(1)
    #vera.page_city()
    #vera.driver.implicitly_wait(2)
    #vera.page_locale()
    #vera.driver.implicitly_wait(1)
    vera.read_user_status()
    vera.page_focus()
    if vera.health in range(90, 101):
        vera.change_leisure_focus(6) # "6">Фитнес тренировки
    elif vera.health in range(70, 90):
        vera.change_leisure_focus(18) # "18">Разхождане
    elif vera.health in range(0, 69):
        vera.change_leisure_focus(1) # "1">Почивка и разпускане

    if vera.mood in range(0, 20):
        vera.change_leisure_focus(19)  # "19">Посещение на психиатър
    elif vera.mood in range(20, 50):
        vera.change_leisure_focus(4) # "4">Ходене по магазините
