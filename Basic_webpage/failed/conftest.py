from selenium import webdriver

def setup(self):
    self.driver = webdriver.Chrome()
    self.driver.implicity_wait(20)

    
def clean(self):
    if self.driver != None:
        print("Cleanup of test environment")
        self.driver.close()
        self.driver.quit()
