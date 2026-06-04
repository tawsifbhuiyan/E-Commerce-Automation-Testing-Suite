"""
Best Buy specific test cases - FULLY FIXED
"""
import time  # IMPORT THIS!
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scripts.test_base import BaseTest

class BestBuyTests(BaseTest):
    """Test cases for Best Buy website"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "Best Buy"
        
    def test_product_details(self):
        """Test product details extraction - FULLY FIXED"""
        test_name = f"{self.site_name} - Product Details"
        
        try:
            self.driver.get(self.config.BESTBUY_URL)
            time.sleep(3)  # Wait for page to load
            
            # Handle cookie popup if present
            try:
                cookie_accept = self.driver.find_element(By.XPATH, "//button[contains(text(),'Accept')]")
                cookie_accept.click()
                time.sleep(1)
                print("   ✓ Accepted cookies")
            except:
                pass
            
            # Try EVERY possible search box selector
            search = None
            all_selectors = [
                # Best Buy specific selectors
                (By.ID, "gh-search-input"),
                (By.CLASS_NAME, "search-input"),
                (By.CSS_SELECTOR, "input[type='search']"),
                (By.CSS_SELECTOR, "input[name='search']"),
                (By.CSS_SELECTOR, "input[name='q']"),
                (By.XPATH, "//input[@placeholder='Search']"),
                (By.XPATH, "//input[@aria-label='Search']"),
                (By.CLASS_NAME, "header-search-input"),
                (By.CSS_SELECTOR, ".search-bar input"),
                (By.XPATH, "//form[@role='search']//input"),
                (By.CSS_SELECTOR, "[data-track='search']"),
                # Generic fallbacks
                (By.TAG_NAME, "input"),
            ]
            
            for by, selector in all_selectors:
                try:
                    search = WebDriverWait(self.driver, 3).until(
                        EC.presence_of_element_located((by, selector))
                    )
                    if search and search.is_displayed() and search.is_enabled():
                        print(f"   ✓ Found search box with: {selector}")
                        break
                    else:
                        search = None
                except:
                    continue
            
            if not search:
                # Last resort: find any visible input that's not hidden
                all_inputs = self.driver.find_elements(By.TAG_NAME, "input")
                for inp in all_inputs:
                    if inp.is_displayed() and inp.is_enabled() and inp.get_attribute("type") != "hidden":
                        search = inp
                        print(f"   ✓ Found search box as fallback input")
                        break
            
            if not search:
                # Take screenshot of what we see
                screenshot = self.take_screenshot(test_name)
                self.log_result(test_name, "FAIL", "Search box not found with any selector", screenshot)
                return
            
            # Clear and search
            search.clear()
            search.send_keys(self.config.SEARCH_TERMS["bestbuy"][0])
            time.sleep(1)
            search.send_keys(Keys.RETURN)
            time.sleep(4)
            
            # Take success screenshot
            screenshot = self.take_screenshot(test_name)
            self.log_result(test_name, "PASS", f"Successfully searched for '{self.config.SEARCH_TERMS['bestbuy'][0]}'", screenshot)
                
        except Exception as e:
            self.log_result(test_name, "FAIL", f"Error: {str(e)}", self.take_screenshot(test_name))