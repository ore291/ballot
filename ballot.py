from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

#usernameStr = '160203066'
#passwordStr = 'eweluval'
username_password_list = []
with open("C:\\Users\\USER\\Desktop\\balloting\\venv\\ballot.txt") as file:
    for line in file:
       usernameStr, passwordStr = line.split(':')
       username_password_list.append((usernameStr, passwordStr))

for usernameStr, passwordStr in username_password_list:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(('https://accommodation.unilag.edu.ng'))

    username = browser.find_element_by_id('UsernameTextBox')
    username.send_keys(usernameStr)
    password = browser.find_element_by_id('PasswordTextBox')
    password.send_keys(passwordStr, Keys.ENTER)
    #nextButton = browser.find_element_by_link_text('login')
    #nextButton.click()
    accommodationButton = browser.find_element_by_link_text('Accommodation')
    accommodationButton.click()

                                                                                     