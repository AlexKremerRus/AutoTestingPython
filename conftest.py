#conftest для написания фикстур  - фикстура драйвера - открывать и закрывать браузер
import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
	driver = webdriver.Chrome(ChromeDriverManager().install()) 					#(v2)(13:42) (webdriver-manager)
	driver.maximize_window()
	yield driver
	driver.quit()