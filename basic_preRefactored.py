import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Scenario: Practice with Simple Webpage
#Feature: 
def basic():
    URL="https://testpages.herokuapp.com/styled/basic-web-page-test.html"
    
    #Given the webpage's three paragraphs and a header
    b=webdriver.Chrome()
    wait = WebDriverWait(b,20)
    m=b.get(URL)

    #When user will see these
    l = b

    header=l.find_element(By.XPATH,"/html/body/div/h1").text #XPATH, header
    explain=l.find_element(By.XPATH,"/html/body/div/div[2]").text #XPATH, explanation
    mainpar=l.find_element(By.ID,"para1").text #ID, Main paragraph
    subpar=l.find_element(By.ID,"para2").text #ID, Sub paragraph
       
    #Then copy text in python console (Setup)
    visual = header,explain,mainpar,subpar
    for i in visual:
        if type(i) != str:
            assert False
        else:
            assert True
              

    #And close files (Clean Up)
    b.close()
    b.quit()

basic()
