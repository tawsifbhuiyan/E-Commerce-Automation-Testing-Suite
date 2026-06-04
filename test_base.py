"""
Base test class that all specific test classes inherit from
Includes self-healing selectors and robust error handling
"""
import time
import random
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver

class BaseTest:
    """Base class providing common functionality for all tests with self-healing capabilities"""
    
    def __init__(self, driver: webdriver.Chrome, screenshot_manager, report_generator, config):
        self.driver = driver
        self.screenshot_manager = screenshot_manager
        self.report_generator = report_generator
        self.config = config
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        self.short_wait = WebDriverWait(driver, 5)
        
    def random_delay(self):
        """Add random delay to simulate human behavior"""
        delay = random.uniform(self.config.RANDOM_DELAY_MIN, self.config.RANDOM_DELAY_MAX)
        time.sleep(delay)
    
    def take_screenshot(self, test_name: str) -> str:
        """Take screenshot for current test"""
        try:
            return self.screenshot_manager.take_screenshot(self.driver, test_name)
        except Exception as e:
            print(f"⚠️ Could not take screenshot: {e}")
            return ""
    
    def log_result(self, test_name: str, status: str, message: str, screenshot: str = ""):
        """Log test result to report"""
        self.report_generator.add_result(test_name, status, message, screenshot)
        print(f"[{status}] {test_name}: {message}")
    
    def safe_find_element(self, by: By, value: str, timeout: int = None):
        """Safely find element with timeout"""
        wait_timeout = timeout or self.config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_timeout)
        try:
            element = wait.until(EC.presence_of_element_located((by, value)))
            return element
        except TimeoutException:
            return None
        except Exception:
            return None
    
    def safe_find_elements(self, by: By, value: str, timeout: int = None):
        """Safely find multiple elements"""
        wait_timeout = timeout or self.config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_timeout)
        try:
            wait.until(EC.presence_of_element_located((by, value)))
            return self.driver.find_elements(by, value)
        except:
            return []
    
    def safe_click(self, by: By, value: str, timeout: int = None):
        """Safely click element with multiple strategies"""
        wait_timeout = timeout or self.config.EXPLICIT_WAIT
        wait = WebDriverWait(self.driver, wait_timeout)
        
        try:
            # Try normal click
            element = wait.until(EC.element_to_be_clickable((by, value)))
            element.click()
            return True
        except ElementClickInterceptedException:
            # Try JavaScript click if normal click fails
            try:
                element = self.driver.find_element(by, value)
                self.driver.execute_script("arguments[0].click();", element)
                return True
            except:
                return False
        except:
            return False
    
    def safe_send_keys(self, by: By, value: str, keys: str, clear_first: bool = True):
        """Safely send keys to element"""
        try:
            element = self.safe_find_element(by, value)
            if element:
                if clear_first:
                    element.clear()
                element.send_keys(keys)
                return True
        except:
            pass
        return False
    
    def find_element_with_retry(self, selectors_list: list, timeout: int = None):
        """
        Try multiple selectors to find an element (SELF-HEALING)
        
        Args:
            selectors_list: List of tuples [(By.ID, "value"), (By.CSS_SELECTOR, "value"), ...]
            timeout: Timeout for each selector attempt
        
        Returns:
            WebElement or None
        """
        wait_timeout = timeout or self.config.EXPLICIT_WAIT
        
        for by, selector in selectors_list:
            try:
                wait = WebDriverWait(self.driver, wait_timeout)
                element = wait.until(EC.presence_of_element_located((by, selector)))
                print(f"   ✓ Found element using: {by} = '{selector}'")
                return element
            except TimeoutException:
                continue
            except Exception:
                continue
        
        print(f"   ✗ Could not find element with any of {len(selectors_list)} selectors")
        return None
    
    def wait_for_page_load(self, timeout: int = 30):
        """Wait for page to fully load"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except:
            return False
    
    def scroll_to_element(self, element):
        """Scroll to specific element"""
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
            time.sleep(0.5)
            return True
        except:
            return False
    
    def handle_popup(self, close_selectors: list = None):
        """
        Handle common popups like cookies, newsletters, etc.
        
        Args:
            close_selectors: List of selectors for close buttons
        """
        if close_selectors is None:
            close_selectors = [
                (By.XPATH, "//button[contains(text(),'Close')]"),
                (By.XPATH, "//button[contains(text(),'×')]"),
                (By.XPATH, "//button[contains(text(),'Accept')]"),
                (By.XPATH, "//button[contains(text(),'Got it')]"),
                (By.CLASS_NAME, "close"),
                (By.CLASS_NAME, "modal-close"),
                (By.CSS_SELECTOR, "[aria-label='Close']")
            ]
        
        for by, selector in close_selectors:
            try:
                element = self.short_wait.until(EC.element_to_be_clickable((by, selector)))
                element.click()
                print(f"   ✓ Closed popup using: {selector}")
                time.sleep(1)
                return True
            except:
                continue
        return False
    
    def extract_text_safe(self, by: By, value: str, default: str = ""):
        """Safely extract text from element"""
        try:
            element = self.safe_find_element(by, value, timeout=3)
            if element:
                text = element.text.strip()
                return text if text else default
        except:
            pass
        return default
    
    def get_current_url(self):
        """Get current URL safely"""
        try:
            return self.driver.current_url
        except:
            return ""
    
    def refresh_page(self):
        """Refresh current page"""
        try:
            self.driver.refresh()
            time.sleep(2)
            return True
        except:
            return False
    
    def go_back(self):
        """Navigate back in browser history"""
        try:
            self.driver.back()
            time.sleep(2)
            return True
        except:
            return False
    
    def wait_for_element_text(self, by: By, value: str, expected_text: str, timeout: int = 10):
        """Wait for element to contain specific text"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.text_to_be_present_in_element((by, value), expected_text))
            return element
        except:
            return False
    
    def is_element_visible(self, by: By, value: str, timeout: int = 5):
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located((by, value)))
            return element.is_displayed()
        except:
            return False
    
    def get_page_title(self):
        """Get current page title"""
        try:
            return self.driver.title
        except:
            return ""
    
    def highlight_element(self, element, duration: float = 0.5):
        """Highlight element for visual debugging"""
        try:
            original_style = element.get_attribute("style")
            self.driver.execute_script(
                "arguments[0].setAttribute('style', 'border: 3px solid red; background: yellow;');", 
                element
            )
            time.sleep(duration)
            self.driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);", 
                element, original_style
            )
        except:
            pass
    
    def retry_on_failure(self, func, max_retries: int = 3, delay: int = 2):
        """Retry a function if it fails"""
        for attempt in range(max_retries):
            try:
                return func()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                print(f"   Retry {attempt + 1}/{max_retries} after error: {str(e)[:50]}")
                time.sleep(delay)
        return None
    
    # ============ COMMON SEARCH SELECTORS (Self-Healing) ============
    
    def find_search_box(self):
        """Find search box using multiple common selectors"""
        search_selectors = [
            (By.ID, "search"),
            (By.ID, "twotabsearchtextbox"),  # Amazon
            (By.ID, "gh-ac"),  # eBay
            (By.ID, "global-search-input"),  # Walmart
            (By.ID, "gh-search-input"),  # Best Buy
            (By.CSS_SELECTOR, "input[type='search']"),
            (By.CSS_SELECTOR, "input[name='search']"),
            (By.CSS_SELECTOR, "input[name='q']"),
            (By.CSS_SELECTOR, "input[name='query']"),
            (By.CLASS_NAME, "search-box"),
            (By.CLASS_NAME, "desktop-searchBar"),  # Myntra
            (By.XPATH, "//input[@placeholder='Search']"),
            (By.XPATH, "//input[@aria-label='Search']"),
        ]
        return self.find_element_with_retry(search_selectors)
    
    def find_product_items(self):
        """Find product items using common selectors"""
        product_selectors = [
            (By.CSS_SELECTOR, "[data-component-type='s-search-result']"),  # Amazon
            (By.CSS_SELECTOR, ".s-item"),  # eBay
            (By.CSS_SELECTOR, "[data-test='product-title']"),  # Target
            (By.CSS_SELECTOR, ".product-item"),
            (By.CSS_SELECTOR, ".product"),
            (By.CLASS_NAME, "product-card"),
            (By.CSS_SELECTOR, "[data-testid='item-stack']"),  # Walmart
        ]
        return self.find_element_with_retry(product_selectors)
    
    def find_add_to_cart_button(self):
        """Find add to cart button using common selectors"""
        atc_selectors = [
            (By.XPATH, "//button[contains(text(),'Add to Cart')]"),
            (By.XPATH, "//button[contains(text(),'Add to cart')]"),
            (By.XPATH, "//button[contains(@name,'add')]"),
            (By.CSS_SELECTOR, "[name='add-to-cart']"),
            (By.ID, "add-to-cart-button"),
            (By.CLASS_NAME, "add-to-cart"),
        ]
        return self.find_element_with_retry(atc_selectors)
    
    def find_price_element(self):
        """Find price element using common selectors"""
        price_selectors = [
            (By.CSS_SELECTOR, "[itemprop='price']"),
            (By.CSS_SELECTOR, ".price"),
            (By.CLASS_NAME, "a-price-whole"),  # Amazon
            (By.CSS_SELECTOR, ".s-item__price"),  # eBay
            (By.CSS_SELECTOR, "[data-test='product-price']"),  # Target
        ]
        return self.find_element_with_retry(price_selectors)
    
    # ============ ASSERTION HELPERS ============
    
    def assert_page_contains_text(self, text: str, timeout: int = 10):
        """Assert that page contains specific text"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text))
            return True
        except:
            return False
    
    def assert_element_exists(self, by: By, value: str):
        """Assert that element exists"""
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False
    
    def assert_url_contains(self, text: str):
        """Assert that current URL contains text"""
        try:
            return text in self.driver.current_url
        except:
            return False
    
    # ============ SCREENSHOT HELPERS ============
    
    def take_screenshot_with_highlight(self, element, test_name: str):
        """Take screenshot with highlighted element"""
        try:
            # Highlight element
            original_style = element.get_attribute("style")
            self.driver.execute_script(
                "arguments[0].setAttribute('style', 'border: 3px solid red; background: yellow;');", 
                element
            )
            
            # Take screenshot
            screenshot_path = self.take_screenshot(f"{test_name}_highlighted")
            
            # Restore original style
            self.driver.execute_script(
                "arguments[0].setAttribute('style', arguments[1]);", 
                element, original_style
            )
            
            return screenshot_path
        except:
            return self.take_screenshot(test_name)
    
    def take_full_page_screenshot(self, test_name: str):
        """Take full page screenshot"""
        try:
            # Store original window size
            original_size = self.driver.get_window_size()
            
            # Get scroll height
            scroll_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # Set window size to full height
            self.driver.set_window_size(original_size['width'], scroll_height)
            time.sleep(1)
            
            # Take screenshot
            screenshot_path = self.take_screenshot(f"{test_name}_fullpage")
            
            # Restore original window size
            self.driver.set_window_size(original_size['width'], original_size['height'])
            
            return screenshot_path
        except:
            return self.take_screenshot(test_name)
    
    # ============ COOKIE HANDLING ============
    
    def accept_cookies(self):
        """Accept cookies using common selectors"""
        cookie_selectors = [
            (By.XPATH, "//button[contains(text(),'Accept')]"),
            (By.XPATH, "//button[contains(text(),'Allow')]"),
            (By.XPATH, "//button[contains(text(),'Agree')]"),
            (By.XPATH, "//button[contains(text(),'Got it')]"),
            (By.ID, "accept-cookies"),
            (By.CLASS_NAME, "cookie-accept"),
        ]
        
        for by, selector in cookie_selectors:
            try:
                button = self.short_wait.until(EC.element_to_be_clickable((by, selector)))
                button.click()
                print("   ✓ Accepted cookies")
                time.sleep(1)
                return True
            except:
                continue
        return False
    
    # ============ PERFORMANCE METRICS ============
    
    def get_page_load_time(self):
        """Get page load time using Navigation Timing API"""
        try:
            load_time = self.driver.execute_script(
                "return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart;"
            )
            return load_time / 1000  # Convert to seconds
        except:
            return None
    
    def log_performance(self, test_name: str):
        """Log page load performance"""
        load_time = self.get_page_load_time()
        if load_time:
            print(f"   ⏱️ Page load time: {load_time:.2f} seconds")
            self.log_result(f"{test_name} - Performance", "INFO", f"Load time: {load_time:.2f}s", "")