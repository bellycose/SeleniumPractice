import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

#Scenario - Webpage has various types of texts and explore how to select them
#Feature: Various of text with different approaches
def test_find():
    URL='https://testpages.herokuapp.com/styled/find-by-playground-test.html'
    
    #Given user read texts
    b=webdriver.Chrome()
    b.get(URL)
    WebDriverWait(b,20)
    
    #When text is readable
    header = b.find_element(By.XPATH,'/html/body/div[1]/h1').text
    if type(header)!=str:
        assert False
    else:
        assert True

    '''Normal paragraph'''
    #Then paragraph is selectable by Selenium ID 
    para1=b.find_element(By.ID,"p1").text
    if type(para1) != str:
        assert False
    else:
        assert True
    
    #AND by Name
    para2=b.find_element(By.NAME,"pName1").text
    if type(para2) != str:
        assert False
    else:
        assert True

    '''Nested paragraph'''
    #AND by Class
    para3=b.find_element(By.NAME,('pName31')).text
    if type(para3) != str:
        assert False
    else:
        assert True
    #AND by XPATH
    para4=b.find_element(By.XPATH,"//*[@id='p26']").text
    if type(para4) != str:
        assert False
    else:
        assert True
    
    '''Linked paragraph'''
    #AND click embedded link
    linked=b.find_element(By.XPATH,"//*[@id='a40']").click()
    if linked!=None:
        assert False
        print("Method did not click.")
    else:
        assert True
        print("Method did click.")
    #AND a group of texts with similar or exact naming convention
    for i in range(25):
        linked2=b.find_elements(By.LINK_TEXT,f"jump to para {i}")
        if type(linked2)!=list:
            assert False
        else:
            assert True


    b.close()
    b.quit()


test_find()
