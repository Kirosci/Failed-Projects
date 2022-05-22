#Necessary Imports----------------------------------------------------------
from calendar import month
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pyautogui
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#Opens and copy the email address from the site-------------------------------

driver.get("https://temp-mail.org")
time.sleep(8)
copy_btn=driver.find_element_by_id ("mail")
copy_btn.click()
copy_btn.send_keys(Keys.CONTROL,"c")

#Opens Instagram----------------------------------------------

driver.switch_to.new_window()
driver.get("https://www.instagram.com/")
time.sleep(5)

#Filling Necessary Details-----------------------------------
pyautogui.click(x=533,y=535)
time.sleep(5)
signup=driver.find_element_by_link_text("Sign up")
signup.click()
time.sleep(4)
pyautogui.click(x=843, y=327)
fill_mail=driver.find_element_by_name ("emailOrPhone")
fill_mail.click()
fill_mail.send_keys(Keys.CONTROL, "v")
fill_name=driver.find_element_by_name ("fullName")
fill_name.click()
fill_name.send_keys("kiroskee")
fill_uname=driver.find_element_by_name ("username")
fill_uname.click()
unamelist = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

uname=(random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist))
fill_uname.send_keys(uname)
fill_pass=driver.find_element_by_name ("password")
fill_pass.click()
password=(random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist)+random.choice(unamelist))
fill_pass.send_keys(password)

#saves the username and the password in credentials.txt---------------------
with open("credentials.txt",'w',encoding = 'utf-8') as f:
    f.write("Username:"+uname)
    f.write("  Password:"+password)

f.close()
time.sleep(3)
pyautogui.hotkey('enter')
time.sleep(3)
#Fills the DOB--------------------------------------------
pyautogui.click(x=531, y=405)
f=random.randint(1,20)
pyautogui.press('down', presses=f)
time.sleep(1)
pyautogui.hotkey('enter')
pyautogui.click(x=595, y=402)
p=random.randint(13,30)
pyautogui.press('down', presses=p)
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.click(x=529, y=505)
time.sleep(1)
#opens the previous tab (temp-mail.org)-----------------------------------
driver.switch_to.window(driver.window_handles[0])
time.sleep(23)
#scrolls down and copy the confirmation code------------------------------
pyautogui.scroll(-600)
time.sleep(1)
pyautogui.click(x=533,y=396)
pyautogui.click(x=533,y=396)
pyautogui.click(x=533,y=396)
time.sleep(1)
pyautogui.keyDown('ctrl')
pyautogui.hotkey('c')
pyautogui.keyUp('ctrl')
time.sleep(2)
#switch to instagram tab and fills the code ------------------------
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
pyautogui.click(x=515, y=383)
time.sleep(1)
pyautogui.keyDown('ctrl')
pyautogui.hotkey('v')
pyautogui.keyUp('ctrl')
time.sleep(1)
#Erases the extra charachters from the code---------------- 
pyautogui.hotkey('backspace')
pyautogui.hotkey('backspace')
time.sleep(1)
#TADA! 
pyautogui.hotkey('enter')






