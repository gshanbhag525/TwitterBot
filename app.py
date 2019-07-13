from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/login')
        time.sleep(10)
        email = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
        password = bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
        email.clear()
        password.clear()

        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def liketweet(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        for i in range(1,3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            tweets = bot.find_elements_by_class_name('tweet')

            links = [elem.get_attribute('data-permalink-path')
                     for elem in tweets]

            for link in links:
                bot.get('https://twitter.com' + link)
                time.sleep(4)
                try:
                    bot.find_element_by_class_name('HeartAnimation').click()
                    print('Clicked')
                    time.sleep(10)
                except Exception as ex:
                    print('Error')
                    time.sleep(60)




            print(links)



gun = TwitterBot('Your_username/email/phone', 'Your_password')
gun.login()
gun.liketweet('aws')

