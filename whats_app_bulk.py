from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
#from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time
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

# searchbox=driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]")
# searchbox.click()
# time.sleep(5)
 #add contacts in this list
for i in contacts:
    searchbox=driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]")
    searchbox.click()
    searchbox.send_keys(i)
    time.sleep(5)
    driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]").send_keys(Keys.ENTER)
    #action.send_keys(Keys.ENTER)
    time.sleep(5)
    messagebox=driver.find_element(By.XPATH,"//div[@title='Type a message']//p")
    messagebox.click()
    time.sleep(5)
    messagebox.send_keys("I'm happy!!!")
    time.sleep(10)
    
    driver.find_element(By.XPATH,"//span[@data-testid='send']").click()

    time.sleep(5)

    driver.find_element(By.XPATH,"//span[@data-testid='clip']").click()
    time.sleep(5)
    attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").click()
    # send_keys("C:\SMARTS\Screenshot.png")
    

    file_path = "C:\SMARTS\Screenshot.png"

# Make sure the file path is absolute
    absolute_file_path = os.path.abspath(file_path)

# Use the absolute file path to send the keys
    attach_box.send_keys(absolute_file_path)
    # attach=driver.find_element(By.XPATH,"//span[@data-testid='attach-document']").send_keys("C:/SMARTS/Vyshnavi_Resume.pdf")
    #attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").click()
    time.sleep(3)

    # attach_file_button = driver.find_element(By.XPATH, "//input[@accept='*']")
    # attach_file_button.send_keys("C:/Users/ngarimella2/Downloads/SMARTS proof.png")
    # send_keys("C:\\SMARTS\\Vyshnavi_Resume.pdf")
    #attach_box=driver.find_element(By.XPATH,"//span[@data-testid='attach-image']").click().send_keys("C:\SMARTS\Screenshot.png")
    # attach_box.send_keys("C:\\SMARTS\\Vyshnavi_Resume.pdf")
    # time.sleep(5)
    
    
    # driver.find_element(By.XPATH,"//span[@data-testid='attach-document']").click()

    # time.sleep(3)
    # driver.find_element(By.XPATH,"//span[@data-testid='attach-document']").send_keys("C:\\Users\\ngarimella2\\Documents")
    


    # #driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]")
    # # driver.switch_to
    # # driver.find_element(By.XPATH,"(//p[@class='selectable-text copyable-text iq0m558w'])[1]").clear()

    








# searchbox.send_keys("You")
# time.sleep(5)
# # searchbox.submit()
# # time.sleep(20)
# #driver.find_element(By.CLASS_NAME,"tvf2evcx gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr").click()
# driver.find_element(By.CSS_SELECTOR,"div[data-testid='message-yourself-row'] div[class='_21S-L']").click()
# time.sleep(20)

# messagebox=driver.find_element(By.XPATH,"//div[@title='Type a message']//p")
# messagebox.click()
# time.sleep(5)
# messagebox.send_keys("I'm happy!!!")
# time.sleep(6)

# driver.find_element(By.XPATH,"//span[@data-testid='send']").click()

# time.sleep(10)
