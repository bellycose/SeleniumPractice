import pytest
import basicElement,basicLocator
from selenium import webdriver

@pytest.fixture
def test_access(self):
    b=webdriver.Chrome()
    if (basicElement.getAccess()!="") is True:
        assert False
    else:
        assert True

@pytest.fixture
def test_visual(self):
    for i in basicLocator.k:
        if type(i) != str:
            assert False
        else:
            assert True
