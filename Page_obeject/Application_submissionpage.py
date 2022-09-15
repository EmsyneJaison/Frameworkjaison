from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.KeywordUtils import Keywordutils
class Applicationsubmissionpage():
    ser_area='ddlArea'
    ser_in='ddlSourceOfIncome'
    mob='txtMobileNo'
    dob='txtDOB'
    pan='txtPanNo'
    submit='btnVerify'
    msge='//*[@id="divOTPDetails"]/div[1]'

    def __init__(self,driver):
        self.driver=driver
        self.ku=Keywordutils(driver)


    def select_service_area(self,value):
        ser_area = Select(self.driver.find_element(By.ID, self.ser_area))
        ser_area.select_by_value(value)

    def select_income(self,value):
        ser_in = Select(self.driver.find_element(By.ID,self.ser_in))
        ser_in.select_by_value(value)

    def Mob_input(self,value):
        self.driver.find_element(By.ID,self.mob).send_keys(value)
        print("Given Mobile Number is :", self.driver.find_element(By.ID,self.mob).get_attribute('value'))

    def dob_input(self,value):
        self.driver.find_element(By.ID,self.dob).send_keys(value)

    def pan_input(self,value):
        self.driver.find_element(By.ID,self.pan).send_keys(value)

    def button_click(self):
        self.ku.click(By.ID,self.submit)
        # self.driver.find_element(By.ID,self.submit).click()

    def sendmobile_validation(self):
        Test = self.driver.find_element(By.XPATH,self.msge).text
        return Test




