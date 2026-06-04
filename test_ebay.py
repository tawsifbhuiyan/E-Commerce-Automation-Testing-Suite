"""
eBay specific test cases
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_base import BaseTest

class EbayTests(BaseTest):
    """Test cases for eBay website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "eBay"
        
    def test_infinite_scroll(self):
        """Test infinite scroll functionality"""
        test_name = f"{self.site_name} - Infinite Scroll"
        
        try:
            self.driver.get(self.config.EBAY_URL)
            self.random_delay()
            
            # Search for products
            search = self.safe_find_element(By.ID, "gh-ac")
            if not search:
                self.log_result(test_name, "FAIL", "Search box not found", self.take_screenshot(test_name))
                return
            
            search.send_keys(self.config.SEARCH_TERMS["ebay"][0])
            search.send_keys(Keys.RETURN)
            self.random_delay()
            
            # Scroll multiple times
            initial_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_count = 0
            
            for i in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                self.random_delay()
                scroll_count += 1
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == initial_height:
                    break
                initial_height = new_height
                
            screenshot = self.take_screenshot(test_name)
            self.log_result(test_name, "PASS", f"Performed {scroll_count} scrolls successfully", screenshot)
            
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))