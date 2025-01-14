from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from playsound import playsound

driver = webdriver.Chrome() 

try:
    driver.get("https://flexstudent.nu.edu.pk/")
   
except TimeoutException:
    driver.get("https://flexstudent.nu.edu.pk/")

time.sleep(15)
wait = WebDriverWait(driver, 10)
link_element = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/Student/CourseRegistration')]")))
while True:
    try:
        div_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "m-alert__text"))
            )   
    
        elements = driver.find_elements(By.ID, "CourseReg")
        # Monitor for changes in the `div`'s text
        initial_text = div_element.text 
        print(f"Initial text: {initial_text}")
        
        current_text = div_element.text
        if (current_text != initial_text) or elements:
            print(f"Change detected! New text: {current_text}")
            playsound("sound.mp3")
            time.sleep(1000)
        time.sleep(3)
        driver.refresh()
    except:
        playsound("sound.mp3")
        time.sleep(1000)
    finally:
        time.sleep(15)