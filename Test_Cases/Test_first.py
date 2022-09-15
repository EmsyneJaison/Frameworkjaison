import time

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
from Test_Cases.Test_config import test_setupp
from Page_obeject.Application_submissionpage import Applicationsubmissionpage

@pytest.mark.usefixtures('test_setupp')
class Testapplication():


    # @pytest.fixture()
    # def test_setup(self):
        # # global driver
        # self.driver=Chrome(executable_path=ChromeDriverManager().install())
        # self.driver.implicitly_wait(30)
        # self.driver.maximize_window()
        # yield
        # self.driver.quit()

    def test_title_validation(self):
        title = self.driver.title
        assert title == 'eMLeads | Application Submission'


    def test_fillapp(self):
        # self.driver.get("https://plleads.muthootfinance.com/indexApplication.html")
        # ser_area=Select(self.driver.find_element(By.ID,'ddlArea'))
        # ser_area.select_by_value("11112")
        self.asp=Applicationsubmissionpage(self.driver)
        self.asp.select_service_area("11112")
        # ser_in=Select(self.driver.find_element(By.ID,'ddlSourceOfIncome'))
        # ser_in.select_by_value("1")
        self.asp.select_income("1")
        # self.driver.find_element(By.ID,'txtMobileNo').send_keys("9995355522wtyrw")
        self.asp.Mob_input("9995355522")
        # print("Given Mobile Number is :",self.driver.find_element(By.ID,'txtMobileNo').get_attribute('value'))
        # self.driver.find_element(By.ID,'txtDOB').send_keys("04/01/2000")
        # self.driver.find_element(By.ID,'txtPanNo').send_keys("AQSPJ5542Q")
        # self.driver.find_element(By.ID,'btnVerify').click()
        self.asp.dob_input("04/01/2000")
        self.asp.pan_input("AQSPJ5542Q")

        self.asp.button_click()
        Text=self.asp.sendmobile_validation()
        # text = self.driver.find_element(By.XPATH,'//*[@id="divOTPDetails"]/div[1]').text
        assert Text == "Activation Key is sent to 9995355522"


    def test_Otp_validation(self):
        self.driver.find_element(By.ID,'txtOTP').send_keys("5")
        self.driver.find_element(By.ID, 'txtOTP1').send_keys("5")
        self.driver.find_element(By.ID, 'txtOTP2').send_keys("5")
        self.driver.find_element(By.ID, 'txtOTP3').send_keys("5")
        self.driver.find_element(By.ID, 'txtOTP4').send_keys("5")
        self.driver.find_element(By.ID, 'txtOTP5').send_keys("5")
        self.driver.find_element(By.ID,'btnSubmitOTP').click()
        time.sleep(5)
        tex1 = self.driver.find_element(By.XPATH,'//div[@class="bootbox-body"]').text
        print('error message is ',tex1)
        assert tex1 == "The Key you have entered is incorrect. Please try again."










    # def test_teardown():
    #     driver.quit()



