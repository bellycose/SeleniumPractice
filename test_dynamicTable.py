import pytest
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

#Scenario - to develop a new table by JSON
#Feature: JSON create HTML Table
def test_dynTable():
    URL='https://testpages.herokuapp.com/styled/tag/dynamic-table.html'

    #Given a table already
    b=webdriver.Chrome()
    wait = WebDriverWait(b,20)
    b.get(URL)

    table1=b.find_element(By.TAG_NAME,'table').text
    if type(table1)!=str:
        assert False
    else:
        assert True

    #When user clicked on the pull-down button
    wait.until(EC.visibility_of_element_located((By.TAG_NAME,"summary"))).click()
    
    #Then the JSON text box is revealed
    jbox=b.find_element(By.ID,'jsondata')
    if type(jbox.text)!=str:
        assert False
        print("The pull-down button was not clicked.")
    else:
        assert True
    
    #AND JSON info is inputted after clearing the textbox
    p="[{'name':'Rick','member':'grandpa'},{'name':'Summers','member':'daughter'}]"
    clearbox=jbox.clear()
    jbox.send_keys(p)

    #AND Title is changed to "New Table" after clearing the textbox
    capbox=b.find_element(By.ID,"caption").clear()
    b.find_element(By.ID,"caption").send_keys("New Table")
    
    #AND Id is changed to "Tablet132" after clearing the textbox
    tabbox=b.find_element(By.ID,"tableid").clear()
    b.find_element(By.ID,"tableid").send_keys("Tablet132")

    #AND user click "Refresh" button to update to a new table
    wait.until(EC.visibility_of_element_located((By.ID,"refreshtable"))).click()

    #Try to confirm if the new table is created
    newtab=b.find_element(By.TAG_NAME,'table').text
    print(newtab)

    b.quit()

test_dynTable()
