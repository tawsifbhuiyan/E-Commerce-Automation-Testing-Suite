"""
WebDriver factory for creating and managing browser instances
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import TestConfig

class WebDriverFactory:
    """Factory class to create and configure WebDriver instances"""
    
    def __init__(self, config: TestConfig):
        self.config = config
        self.driver = None
        
    def create_driver(self):
        """Create and return a configured Chrome WebDriver"""
        chrome_options = Options()
        
        if self.config.HEADLESS_MODE:
            chrome_options.add_argument('--headless')
        
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.implicitly_wait(self.config.IMPLICIT_WAIT)
        
        return self.driver
    
    def quit_driver(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            self.driver = None