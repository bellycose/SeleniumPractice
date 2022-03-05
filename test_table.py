import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Scenario a HTML table is provided
#Feature: HTML table
def test_table():
    URL = 'https://testpages.herokuapp.com/styled/tag/table.html'
    
    #Given website loaded a table
    b=webdriver.Chrome()
    b.get(URL)
    wait=WebDriverWait(b,20)

    #When user arrives at the website and sees a table
    table=b.find_element(By.ID,'mytable').text
    if type(table)!=str:
        assert False
        print("Table contents not present.")
    else:
        assert True
        print("Table contents present.")

    #Then the table shows a column of names
    rows=b.find_elements(By.TAG_NAME,'tr')
    for i, col in enumerate(rows):
        col=b.find_element(By.TAG_NAME,'td').text
        print(col)

    #And shows the amount associated with names

    b.close()
    b.quit()

test_table()
