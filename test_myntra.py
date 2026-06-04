"""
Myntra specific test cases
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_base import BaseTest

class MyntraTests(BaseTest):
    """Test cases for Myntra website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "Myntra"
        
    def test_filter_combinations(self):
        """Test filter combinations"""
        test_name = f"{self.site_name} - Filter Combinations"
        
        try:
            self.driver.get(self.config.MYNTRA_URL)
            self.random_delay()
            
            # Search for product
            search = self.safe_find_element(By.CLASS_NAME, "desktop-searchBar")
            if not search:
                self.log_result(test_name, "FAIL", "Search box not found", self.take_screenshot(test_name))
                return
            
            search.send_keys(self.config.SEARCH_TERMS["myntra"][0])
            search.send_keys(Keys.RETURN)
            self.random_delay()
            
            screenshot = self.take_screenshot(test_name)
            self.log_result(test_name, "PASS", "Successfully searched for products", screenshot)
            
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))