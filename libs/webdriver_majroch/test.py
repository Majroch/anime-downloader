import selenium
import webdriver_majroch

# Debug
import time

if __name__ == "__main__":
    driver = webdriver_majroch.run()
    
    if time:
        time.sleep(5)
    
    driver.close()