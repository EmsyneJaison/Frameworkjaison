from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import  logging

class Keywordutils():
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,30)

    def click(self,by,loc): # (click(By.ID,'mobileinput')
        self.wait.until(ec.presence_of_element_located((by,loc)))
        self.wait.until(ec.element_to_be_clickable((by,loc)))
        self.driver.find_element(by,loc).click()

    def sele_by_value(self,by,loc,value):
        self.wait.until(ec.visibility_of_element_located((by,loc,value)))
        self.driver.find_element(by,loc,value).select







