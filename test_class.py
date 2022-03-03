import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Scenario: Website having class-locators
#Feature: Registered these classes in webpage object
def test_class():
    URL='https://testpages.herokuapp.com/styled/attributes-test.html'
        
    #Given user access the webpage
    b=webdriver.Chrome()
    wait = WebDriverWait(b,20)
    b.get(URL)

    #When loaded, contents is available
    firstpar=b.find_element(By.XPATH,'//*[@id="domattributes"]').text
    secondpar=b.find_element(By.CSS_SELECTOR,'#jsattributes').text
    for i in [firstpar,secondpar]:
        if type(i)!=str:
            assert False
            #print(f"{i}")
        else:
            assert True
            #print("This Paragraph is accounted.")
    
    #Then user click on the "button"
    button=b.find_element(By.XPATH,'//html/body/div/div[4]/button')
    
    if (button.click==True)!=False:
        #print('Button was not clicked')
        assert False
    else:
        #print("Button was clicked")
        assert True
        
    b.close()
    b.quit()

test_class()
