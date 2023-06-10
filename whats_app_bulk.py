from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
message=str(input("Enter the message: "))
Contact_list_number=int(input("Enter the contact count number: "))
contacts=[]
for i in range(Contact_list_number):
    Con=input("Enter name {}:".format(i+1))
    contacts.append(Con)
print(contacts)

driver=webdriver.Chrome()
#action=ActionChains(driver)
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
time.sleep(20)

 #add contacts in this list
for i in contacts:
    searchbox=driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]")
    searchbox.click()
    searchbox.send_keys(i)
    time.sleep(5)
    driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]").send_keys(Keys.ENTER)
    time.sleep(5)
    messagebox=driver.find_element(By.XPATH,"//div[@title='Type a message']//p")
    messagebox.click()
    time.sleep(5)
    messagebox.send_keys(message)
    time.sleep(10)
    driver.find_element(By.XPATH,"//span[@data-testid='send']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//span[@data-testid='clip']").click()
    time.sleep(5)
    attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").click()
    time.sleep(5)
    #absolute file path
    file_path ="C:\SMARTS\Screenshot.png"

# Make sure the file path is absolute
    absolute_file_path = os.path.abspath(file_path)

# Use the absolute file path to send the keys
    attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").send_keys(absolute_file_path)
    
    # attach=driver.find_element(By.XPATH,"//span[@data-testid='attach-document']").send_keys("C:/SMARTS/Vyshnavi_Resume.pdf")
    #attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[@data-testid='send']").click()
    