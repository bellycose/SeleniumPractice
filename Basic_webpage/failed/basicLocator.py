from selenium.webdriver.common.by import By

class locator(object):
    
    #Locator
    header=(By.XPATH,"/html/body/div/h1")
    explain=(By.XPATH,"/html/body/div/div[2]")
    mainpar=(By.ID,"para1")
    subpar=(By.ID,"para2")

    k=[header,explain,mainpar,subpar]
    
    
