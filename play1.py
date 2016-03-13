from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PopCharacter:

    def __init__(self):
        self.current_page = ''
        self.driver = webdriver.Firefox()
        self.curr_city = ''
        self.curr_locale = ''
        self.leisure_act = ''
        self.professional_act = ''
        self.attitude = ''
        self.condition = ''
        self.mood = ''
        self.health = ''
        self.star_quality = ''
        self.cash = 111
        self.achievement_points = 0
        self.online_status = ''

    def load_pass(self):
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
        password.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
        # driver.close()

        # if self.driver.title.strip() == 'Popmundo - Vera Lobyntseva':
    def read_user_status(self):
        self.curr_city = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[1]/a[contains(@href,"City")]').text
        self.curr_locale = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[1]/a[contains(@href,"Locale")]').text
        self.leisure_act = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[2]/strong[1]').text
        self.professional_act = self.driver.find_element_by_xpath('//div[@class="float_left characterPresentation"]/p[2]/strong[2]').text
        self.attitude = self.driver.find_element_by_id('ctl00_cphLeftColumn_ctl00_lnkAttitude').text
        self.condition = self.driver.find_element_by_xpath('//*[@id="content"]/div[@class="charMainToolbox"]/table/tbody/tr[2]/td[2]').text
        self.mood = self.driver.find_element_by_xpath('//*[@id="content"]/div[@class="charMainValues"]/table/tbody/tr[1]/td[2]/div').get_attribute('title')
        self.health = self.driver.find_element_by_xpath('//*[@id="content"]/div[@class="charMainValues"]/table/tbody/tr[2]/td[2]/div').get_attribute('title')
        self.star_quality = self.driver.find_element_by_xpath('//*[@id="content"]/div[@class="charMainValues"]/table/tbody/tr[3]/td[2]/div').get_attribute('title')
        cash = self.driver.find_element_by_xpath('//*[@id="content"]/div[@class="charMainValues"]/table/tbody/tr[4]/td[2]').text.strip(' лв.')
        cash_b = ''
        for i in cash:
            if i.isdigit():
                cash_b += i
            elif i == ',':
                cash_b += '.'
        self.cash = float(cash_b)
        print(self.curr_city, self.curr_locale, self.leisure_act, self.professional_act, self.attitude, self.condition, self.mood, self.health, self.star_quality, self.cash)

    def page_character(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkCharacter').click()

    def page_start(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkStart').click()

    def page_city(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkCity').click()

    def page_locale(self):
        self.driver.find_element_by_id('ctl00_ctl05_ucMenu_lnkLocale').click()

if __name__ == '__main__':
    vera = PopCharacter()
    vera.login()
    vera.driver.implicitly_wait(1)
    vera.page_character()
    vera.driver.implicitly_wait(3)
    #vera.page_start()
    #vera.driver.implicitly_wait(1)
    #vera.page_city()
    #vera.driver.implicitly_wait(2)
    #vera.page_locale()
    #vera.driver.implicitly_wait(1)
    vera.read_user_status()
