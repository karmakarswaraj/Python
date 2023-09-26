from selenium import webdriver
import time
from random import seed
from random import randint

class InstaBot:
    def __init__(self, username, password):
        followFarm = ["mahi7781", "_meisp_", "sutirtha_8623"]
       
        driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
        driver.get("https://instagram.com")      
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        time.sleep(getRandomTime())      
        driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()


        time.sleep(getRandomTime())
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
  
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
            .click()
            
            
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")\
          .send_keys(followFarm[randint(0, 7)])
    
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div")\
            .click()    
      
        time.sleep(getRandomTime())
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click() 

        time.sleep(getRandomTime())
     
    
        htmlBadBoyToFollow = "/html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[3]/button"   
        for i in range(2,20,1):
             htmlBadBoyToFollow = "/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button"
        
             if(driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/ul/div/li["+str(i)+"]/div/div[3]/button").text == "Following"):
                 # This is so we dont follow people we already follow- trust me this would cause issues otherwise
                 continue               
             driver.find_element_by_xpath(htmlBadBoyToFollow).click()
             time.sleep(getRandomTime())

        driver.quit()

def getRandomTime():
        randTime = randint(3, 5)
        return randTime
        
        
        
InstaBot("https.swaraj", "@nobodycares")
