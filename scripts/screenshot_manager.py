"""
Manages screenshot capture and storage
"""
import os
from datetime import datetime
from selenium import webdriver

class ScreenshotManager:
    """Handles taking and storing screenshots"""
    
    def __init__(self, screenshot_dir: str):
        self.screenshot_dir = screenshot_dir
        self.ensure_directory()
        
    def ensure_directory(self):
        """Ensure screenshot directory exists"""
        if not os.path.exists(self.screenshot_dir):
            os.makedirs(self.screenshot_dir)
    
    def take_screenshot(self, driver: webdriver.Chrome, test_name: str) -> str:
        """Take screenshot and return file path"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{test_name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)
        driver.save_screenshot(filepath)
        return filepath