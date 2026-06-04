"""
Test runner that executes all test suites
"""
import sys
import os
from selenium.webdriver.chrome.webdriver import WebDriver
from config import TestConfig
from scripts.webdriver_factory import WebDriverFactory
from scripts.screenshot_manager import ScreenshotManager
from scripts.report_generator import ReportGenerator
from scripts.test_amazon import AmazonTests
from scripts.test_flipkart import FlipkartTests
from scripts.test_bestbuy import BestBuyTests
from scripts.test_target import TargetTests
from scripts.test_walmart import WalmartTests
from scripts.test_ebay import EbayTests
from scripts.test_myntra import MyntraTests

class TestRunner:
    """Orchestrates execution of all test suites"""
    
    def __init__(self):
        self.config = TestConfig()
        self.config.create_directories()
        self.driver_factory = WebDriverFactory(self.config)
        self.screenshot_manager = ScreenshotManager(self.config.SCREENSHOT_DIR)
        self.report_generator = ReportGenerator(self.config.REPORT_DIR)
        self.driver: WebDriver = None
        
    def setup(self):
        """Setup test environment"""
        print("\n" + "="*60)
        print("🚀 Setting up test environment...")
        print("="*60)
        self.driver = self.driver_factory.create_driver()
        
    def teardown(self):
        """Cleanup test environment"""
        print("\n" + "="*60)
        print("🧹 Cleaning up test environment...")
        print("="*60)
        if self.driver_factory:
            self.driver_factory.quit_driver()
        
    def run_all_tests(self):
        """Execute all test cases"""
        print("\n" + "="*60)
        print("🎯 STARTING TEST EXECUTION")
        print("="*60)
        
        # Initialize all test classes
        test_classes = [
            AmazonTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            FlipkartTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            BestBuyTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            TargetTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            WalmartTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            EbayTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
            MyntraTests(self.driver, self.screenshot_manager, self.report_generator, self.config),
        ]
        
        # Execute tests
        for test_class in test_classes:
            print(f"\n📝 Running tests for: {test_class.site_name}")
            print("-" * 40)
            
            # Get all test methods from the class
            test_methods = [method for method in dir(test_class) 
                          if method.startswith('test_') and callable(getattr(test_class, method))]
            
            for method_name in test_methods:
                try:
                    method = getattr(test_class, method_name)
                    method()
                except Exception as e:
                    print(f"⚠️ Error in {method_name}: {e}")
                    test_class.log_result(method_name, "FAIL", f"Unexpected error: {str(e)}", 
                                         test_class.take_screenshot(method_name))
        
        # Generate final report
        report_path = self.report_generator.generate_report()
        
        print("\n" + "="*60)
        print("✅ TEST EXECUTION COMPLETED")
        print(f"📊 Report generated at: {report_path}")
        print(f"📸 Screenshots saved in: {self.config.SCREENSHOT_DIR}")
        print("="*60)
        
        return report_path