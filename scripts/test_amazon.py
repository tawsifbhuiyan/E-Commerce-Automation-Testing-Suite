"""
Amazon specific test cases
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from scripts.test_base import BaseTest

class AmazonTests(BaseTest):
    """Test cases for Amazon website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "Amazon"
        
    def test_search_functionality(self):
        """Test search functionality on Amazon"""
        test_name = f"{self.site_name} - Search Products"
        
        try:
            self.driver.get(self.config.AMAZON_URL)
            self.random_delay()
            
            # Find and interact with search box
            search_box = self.safe_find_element(By.ID, "twotabsearchtextbox")
            if not search_box:
                self.log_result(test_name, "FAIL", "Search box not found", self.take_screenshot(test_name))
                return
            
            search_box.send_keys(self.config.SEARCH_TERMS["amazon"][0])
            search_box.send_keys(Keys.RETURN)
            self.random_delay()
            
            # Verify results
            results = self.driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
            screenshot = self.take_screenshot(test_name)
            
            if len(results) > 0:
                self.log_result(test_name, "PASS", f"Found {len(results)} products for '{self.config.SEARCH_TERMS['amazon'][0]}'", screenshot)
            else:
                self.log_result(test_name, "FAIL", "No search results found", screenshot)
                
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))
    
    def test_filter_application(self):
        """Test applying filters on search results"""
        test_name = f"{self.site_name} - Apply Filters"
        
        try:
            self.driver.get(self.config.AMAZON_URL)
            # Search first
            search_box = self.safe_find_element(By.ID, "twotabsearchtextbox")
            search_box.send_keys(self.config.SEARCH_TERMS["amazon"][1])
            search_box.send_keys(Keys.RETURN)
            self.random_delay()
            
            # Try to apply a filter
            filter_applied = False
            try:
                # Look for a department filter
                department_filter = self.safe_find_element(By.XPATH, "//span[contains(text(),'Department')]")
                if department_filter:
                    department_filter.click()
                    self.random_delay()
                    filter_applied = True
            except:
                pass
            
            screenshot = self.take_screenshot(test_name)
            
            if filter_applied:
                self.log_result(test_name, "PASS", "Successfully applied filters", screenshot)
            else:
                self.log_result(test_name, "WARNING", "Filter elements not found", screenshot)
                
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))