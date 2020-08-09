from ...webdriver_majroch import webdriver_majroch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class _Downloader:
    def __init__(self):
        self._author = "Majroch"
        self.driver = webdriver_majroch.run()
    
    def is_element_exist(self, cond: tuple, timeout: int=15) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        try:
            elements = wait.until(EC.presence_of_all_elements_located(cond))
            return True if elements else False
        except:
            return False
    
    