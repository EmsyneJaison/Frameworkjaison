from webbrowser import Chrome
import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from Utilities.ConfigUtilis import config


#class TestConfig():
@pytest.fixture(scope='class')
    #@pytest.fixture()
def test_setupp(request):
    request.cls.driver = Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver.implicitly_wait(30)
    request.cls.driver.maximize_window()
    # request.cls.driver.get("https://plleads.muthootfinance.com/indexApplication.html")
    request.cls.config= config('QC')
    request.cls.driver.get(request.cls.config.get_value('url'))
    yield
    request.cls.driver.quit()
