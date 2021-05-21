from ...webdriver_majroch import webdriver_majroch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ssl

class _Downloader:
    def __init__(self):
        self._author = "Majroch"
        ssl._create_default_https_context = ssl._create_unverified_context
        self.driver = webdriver_majroch.run()

    
    def is_element_exist(self, cond: tuple, timeout: int=15) -> bool:
        # wait = WebDriverWait(self.driver, timeout)
        try:
            # elements = wait.until(EC.presence_of_all_elements_located(cond))
            elements = self.driver.find_element(cond[0], cond[1])
            return True if elements else False
        except:
            return False
    
    