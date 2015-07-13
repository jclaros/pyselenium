import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class TestStringMethods(unittest.TestCase):

  def test_upper(self):


    fp = webdriver.FirefoxProfile()

    fp.add_extension(extension='firebug-2.0.10.xpi')
    fp.add_extension(extension='netExport-0.9.xpi')

    fp.set_preference("extensions.firebug.currentVersion", "2.0.10")
    fp.set_preference("extensions.firebug.DBG_NETEXPORT", False)
    fp.set_preference("extensions.firebug.addonBarOpened", True)
    
    fp.set_preference("extensions.firebug.allPagesActivation", "on")
    fp.set_preference("extensions.firebug.onByDefault", True)
    fp.set_preference("extensions.firebug.defaultPanelName", "net")
    fp.set_preference("extensions.firebug.net.enableSites", True)
    fp.set_preference("extensions.firebug.net.defaultPersist", True)

    fp.set_preference("extensions.firebug.netexport.defaultLogDir", "/Users/jonathan/projects/pytest/projecttesting/logs")
    fp.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport", True)
    fp.set_preference("extensions.firebug.netexport.autoExportToFile", True)
    fp.set_preference("extensions.firebug.netexport.saveFiles", True)

    fp.set_preference("extensions.firebug.netexport.autoExportToServer", False)
    fp.set_preference("extensions.firebug.netexport.Automation", True)
    #fp.set_preference("extensions.firebug.netexport.pageLoadedTimeout", 1500)
    # toggle on for per page report or false for a global but first call
    fp.set_preference("extensions.firebug.netexport.showPreview", False)

    fp.set_preference("extensions.firebug.console.enableSites", True)
    #fp.set_preference("extensions.firebug.consoleexport.defaultLogDir", "/Users/jonathan/projects/pytest/testproject/logs")
    #fp.set_preference("extensions.firebug.consoleexport.logFilePath", "/Users/jonathan/projects/pytest/testproject/logs")
    #fp.set_preference("extensions.firebug.consoleexport.active", True)


    
    fp.update_preferences()

    driver = webdriver.Firefox(firefox_profile=fp)
    time.sleep(5)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    time.sleep(5)
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    time.sleep(5)
    driver.quit()
    self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()



