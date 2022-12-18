import os
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def process():
    print("Press Yes to Enter Message, Press No To Exit")
    response = input()
    if response == "yes" or "YES":
        name_input()
    else:
        return
    process()

def name_input():
    print("Input Name")
    name = input()
    searchbar = wdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    searchbar.send_keys(name, Keys.ENTER)
    msg_send()

def msg_send():
    print("Enter Message to Send")
    message = input()
    textbox = wdriver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    textbox.send_keys(message, Keys.ENTER)

os.environ['PATH'] += r"C:\selenium drivers"
wdriver = webdriver.Chrome()
wdriver.get('https://web.whatsapp.com/')
print("Scan QR & Press Enter")
input()
process()
wdriver.quit()
