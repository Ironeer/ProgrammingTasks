

# BUILTIN
import time

# SELENIUM
from selenium.webdriver import Firefox

def main():
    browserDriver = Firefox()
    browserDriver.get('https://www.google.de')

    inputSearch  = browserDriver.find_element_by_css_selector(".gLFyf.gsfi")
    inputSearch.send_keys("do a barrel roll")
    inputSearch.submit()

if __name__ == '__main__':
    main()
