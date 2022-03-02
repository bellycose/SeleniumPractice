import basicLocator

class webpage(object):
    URL="https://testpages.herokuapp.com/styled/basic-web-page-test.html"

    def __init__(self, driver):
        self.driver = driver
        
    #Interaction Methods - objects/elements
    def getAccess(self):
        title = self.browser.title #accessed
        return title

    def getVisual(self):
        for i in basicLocator.k:
            return self.browser.find_element(i) #visual
