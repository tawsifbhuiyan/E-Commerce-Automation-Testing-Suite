"""
Flipkart specific test cases
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from test_base import BaseTest

class FlipkartTests(BaseTest):
    """Test cases for Flipkart website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "Flipkart"
        self.actions = ActionChains(self.driver)
        
    def test_navigation_menu(self):
        """Test navigation menu interaction"""
        test_name = f"{self.site_name} - Navigation Menu"
        
        try:
            self.driver.get(self.config.FLIPKART_URL)
            self.random_delay()
            
            # Close login popup if appears
            try:
                close_btn = self.driver.find_element(By.CSS_SELECTOR, "._30XB9F")
                close_btn.click()
                self.random_delay()
            except:
                pass
            
            # Find electronics menu
            electronics = self.safe_find_element(By.XPATH, "//div[contains(text(),'Electronics')]")
            if electronics:
                self.actions.move_to_element(electronics).perform()
                self.random_delay()
                screenshot = self.take_screenshot(test_name)
                self.log_result(test_name, "PASS", "Successfully hovered over Electronics menu", screenshot)
            else:
                screenshot = self.take_screenshot(test_name)
                self.log_result(test_name, "WARNING", "Electronics menu not found", screenshot)
                
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))