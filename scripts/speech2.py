from selenium import webdriver
import time
import keyboard
import pyperclip
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://dictation.io/speech")
time.sleep(14)
driver.find_element_by_xpath('//*[@id="dictation"]/div[2]/div/div[3]/div[2]/a[8]/span').click()
print("Listening...")
driver.find_element_by_xpath('//*[@id="dictation"]/div[2]/div/div[3]/div[1]/a/span').click()
keyboard.press_and_release('tab')
keyboard.press_and_release('enter')
keyboard.wait('esc')
driver.find_element_by_xpath('//*[@id="dictation"]/div[2]/div/div[3]/div[1]/a/div').click()
#el = driver.find_element_by_xpath("//*[text()='Stop']")
#el.click()
driver.find_element_by_xpath('//*[@id="dictation"]/div[2]/div/div[3]/div[2]/a[1]/span').click()
t=pyperclip.paste()
print(t)
driver.quit()
			
