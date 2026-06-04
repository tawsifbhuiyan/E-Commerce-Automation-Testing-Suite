


```markdown
# E-Commerce Automation Testing Suite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15+-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Table of Contents
- [Overview](#overview)
- [What This Project Does](#what-this-project-does)
- [Why This Project is Unique](#why-this-project-is-unique)
- [Project Structure](#project-structure)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Understanding Test Results](#understanding-test-results)
- [Test Coverage](#test-coverage)
- [Configuration Options](#configuration-options)
- [Troubleshooting](#troubleshooting)
- [Adding New Websites](#adding-new-websites)
- [Code Examples](#code-examples)
- [FAQ](#faq)
- [License](#license)

## Overview

The **E-Commerce Automation Testing Suite** is a professional, production-ready automation framework built with Python and Selenium. It automatically tests **8 major e-commerce websites**, captures screenshots, generates beautiful HTML reports, and handles real-world web automation challenges like dynamic content, popups, and website structure changes.

## What This Project Does

This project automatically:

- Tests shopping flows across Amazon, Flipkart, Best Buy, Target, Walmart, eBay, and Myntra
- Searches for products on each website
- Captures screenshots of every test step
- Generates professional HTML test reports with pass/fail statistics
- Handles cookies, popups, and dynamic content
- Simulates real user behavior with random delays
- Performs infinite scroll testing (eBay)
- Tests filter combinations (Amazon, Myntra)
- Extracts product information and prices

## Why This Project is Unique

Unlike basic Selenium scripts that test just one website, this framework:

1. Tests 8 different websites in a single execution
2. Self-healing selectors that adapt to website changes
3. Professional reporting with clickable screenshots
4. Modular architecture - add new websites in minutes
5. Real-world testing - handles popups, delays, and dynamic content
6. Visual debugging with element highlighting
7. Performance metrics for page load times
8. Multi-class design pattern following SOLID principles

## Project Structure

```
ecommerce_testing_suite/
│
├── screenshots/                 # All captured screenshots (auto-created)
│   ├── Amazon_Search_20240101.png
│   ├── Flipkart_Navigation_20240101.png
│   └── ...
│
├── test_reports/                # HTML test reports (auto-created)
│   └── test_report_20240101.html
│
├── main.py                      # Entry point - Run this!
├── config.py                    # All configuration settings
├── webdriver_factory.py         # Browser setup and management
├── screenshot_manager.py        # Screenshot capture and storage
├── report_generator.py          # HTML report generation
├── test_base.py                 # Base class with common methods
├── test_runner.py               # Orchestrates all test execution
├── utils.py                     # Utility functions
│
├── test_amazon.py               # Amazon specific tests
├── test_flipkart.py             # Flipkart specific tests
├── test_bestbuy.py              # Best Buy specific tests
├── test_target.py               # Target specific tests
├── test_walmart.py              # Walmart specific tests
├── test_ebay.py                 # eBay specific tests
└── test_myntra.py               # Myntra specific tests
```

## Features

### Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| Multi-site testing | Tests 8 different e-commerce websites | Yes |
| Screenshot capture | Automatic screenshots for every test | Yes |
| HTML reports | Professional reports with statistics | Yes |
| Self-healing selectors | Finds elements even if selectors change | Yes |
| Popup handling | Automatically closes cookies and modals | Yes |
| Random delays | Simulates human behavior | Yes |
| Error handling | Graceful failure with screenshots | Yes |
| Performance metrics | Page load time tracking | Yes |
| Modular design | Easy to add new websites | Yes |

### Self-Healing Capabilities

The framework includes intelligent element location that tries multiple selectors automatically:

- Search boxes: Tries 13+ different selectors to find search inputs
- Product items: Tries 7+ product listing selectors
- Add to cart buttons: Tries 8+ button selectors
- Price elements: Tries 5+ price display selectors

## Prerequisites

### Required Software

- Python 3.8 or higher - Download from python.org
- Google Chrome Browser - Download from google.com/chrome
- Git (optional, for cloning) - Download from git-scm.com

### Required Python Packages

```
selenium==4.15.0
webdriver-manager==4.0.1
pillow==10.1.0
```

## Installation

### Step 1: Clone or Download the Project

```bash
git clone https://github.com/yourusername/ecommerce-testing-suite.git
cd ecommerce-testing-suite
```

### Step 2: Install Python Packages

Open Command Prompt (CMD) or Terminal and run:

```bash
pip install selenium webdriver-manager pillow
```

### Step 3: Verify Installation

Create a quick test file to verify everything works:

```python
# test_setup.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

print("Testing setup...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print("Setup successful! Browser opened!")
driver.quit()
```

Run it:

```bash
python test_setup.py
```

## How to Run

### Basic Execution

```bash
python main.py
```

### What Happens When You Run

1. Chrome browser opens automatically
2. Tests start executing on each website sequentially
3. Console shows real-time progress with pass/fail status
4. Screenshots are saved in screenshots/ folder
5. HTML report is generated in test_reports/ folder

### Expected Console Output

```
============================================================
STARTING TEST EXECUTION
============================================================

Running tests for: Amazon
----------------------------------------
[PASS] Amazon - Search Products: Found 24 products for 'laptop backpack'
[WARNING] Amazon - Apply Filters: Filter elements not found

Running tests for: Flipkart
----------------------------------------
[PASS] Flipkart - Navigation Menu: Successfully hovered over Electronics menu

Running tests for: Best Buy
----------------------------------------
[PASS] Best Buy - Product Details: Successfully searched for 'wireless mouse'

Running tests for: Target
----------------------------------------
[PASS] Target - Add to Cart: Found products for 'water bottle'

Running tests for: Walmart
----------------------------------------
[PASS] Walmart - Price Comparison: Successfully searched and loaded results

Running tests for: eBay
----------------------------------------
[PASS] eBay - Infinite Scroll: Performed 3 scrolls successfully

Running tests for: Myntra
----------------------------------------
[PASS] Myntra - Filter Combinations: Successfully searched for products

============================================================
TEST EXECUTION COMPLETED
Report generated at: test_reports/test_report_20240101_143030.html
Screenshots saved in: screenshots
============================================================
```

## Understanding Test Results

### Test Status Meanings

| Status | Meaning | Action Required |
|--------|---------|-----------------|
| PASS | Test completed successfully | None |
| WARNING | Test completed but with minor issues | Check screenshot; usually normal |
| FAIL | Test failed completely | Check internet or website changes |

### Reading the HTML Report

1. Locate the report: Open test_reports/ folder
2. Open in browser: Double-click any .html file
3. View statistics: See total tests, passes, failures at the top
4. Check screenshots: Click on any screenshot thumbnail to enlarge
5. Review timestamps: See exactly when each test ran

## Test Coverage

### Website Test Matrix

| Website | Test Case | What is Tested |
|---------|-----------|----------------|
| Amazon | Search Functionality | Product search and results display |
| Amazon | Filter Application | Department and category filters |
| Flipkart | Navigation Menu | Hover over electronics menu |
| Best Buy | Product Search | Search for wireless mouse |
| Target | Product Search | Search for water bottle |
| Walmart | Price Comparison | Search multiple products |
| eBay | Infinite Scroll | Scrolling through results |
| Myntra | Filter Combinations | Search and filter products |

## Configuration Options

### config.py Settings

```python
class TestConfig:
    # Browser settings
    HEADLESS_MODE = False        # Run without GUI (True/False)
    IMPLICIT_WAIT = 10           # Default wait time in seconds
    EXPLICIT_WAIT = 15           # Explicit wait timeout
    
    # Test settings
    RANDOM_DELAY_MIN = 2.0       # Minimum delay between actions
    RANDOM_DELAY_MAX = 4.0       # Maximum delay between actions
    MAX_RETRIES = 3              # Retry attempts for failed actions
    
    # URLs
    AMAZON_URL = "https://www.amazon.com"
    FLIPKART_URL = "https://www.flipkart.com"
    BESTBUY_URL = "https://www.bestbuy.com"
    TARGET_URL = "https://www.target.com"
    WALMART_URL = "https://www.walmart.com"
    EBAY_URL = "https://www.ebay.com"
    MYNTRA_URL = "https://www.myntra.com"
```

### Modifying Configuration

**To enable headless mode (no browser window):**
```python
HEADLESS_MODE = True
```

**To speed up tests (for quick execution):**
```python
RANDOM_DELAY_MIN = 0.5
RANDOM_DELAY_MAX = 1.0
```

**To slow down tests (for debugging):**
```python
RANDOM_DELAY_MIN = 3.0
RANDOM_DELAY_MAX = 5.0
```

## Troubleshooting

### Common Issues and Solutions

**Issue 1: WebDriver Manager not found**

Error:
```
ModuleNotFoundError: No module named 'webdriver_manager'
```

Solution:
```bash
pip install webdriver-manager
```

**Issue 2: Chrome browser doesn't open**

Error:
```
selenium.common.exceptions.WebDriverException: Message: chrome not reachable
```

Solution:
- Update Google Chrome to latest version
- Run: pip install --upgrade webdriver-manager
- Restart your computer

**Issue 3: Tests fail on specific websites**

Error:
```
[FAIL] Best Buy - Search box not found with any selector
```

Explanation: Websites frequently change their HTML structure. This is normal in real-world testing.

Solution:
- Tests will still continue with other websites
- Check the screenshot to see current website layout
- The self-healing selectors will try multiple alternatives

**Issue 4: Permission denied for screenshots folder**

Error:
```
PermissionError: [Errno 13] Permission denied: 'screenshots'
```

Solution:
- Windows: Run terminal as Administrator
- Mac/Linux: Use sudo python main.py

## Adding New Websites

### Step-by-Step Guide

**Step 1: Create a New Test File**

Create `test_newegg.py`:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from test_base import BaseTest

class NeweggTests(BaseTest):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_name = "Newegg"
        
    def test_search_functionality(self):
        test_name = f"{self.site_name} - Search Products"
        
        try:
            self.driver.get(self.config.NEWEGG_URL)
            self.random_delay()
            
            search_box = self.find_search_box()
            
            if search_box:
                search_box.send_keys(self.config.SEARCH_TERMS["newegg"][0])
                search_box.send_keys(Keys.RETURN)
                
                screenshot = self.take_screenshot(test_name)
                self.log_result(test_name, "PASS", "Search successful", screenshot)
            else:
                self.log_result(test_name, "FAIL", "Search box not found", 
                              self.take_screenshot(test_name))
                
        except Exception as e:
            self.log_result(test_name, "FAIL", str(e), 
                          self.take_screenshot(test_name))
```

**Step 2: Update config.py**

```python
# Add to TestConfig class
NEWEGG_URL = "https://www.newegg.com"

# Update SEARCH_TERMS dictionary
SEARCH_TERMS = {
    # ... existing sites ...
    "newegg": ["gaming laptop", "ssd drive"]
}
```

**Step 3: Update test_runner.py**

```python
from test_newegg import NeweggTests

# In run_all_tests method add:
test_classes = [
    # ... existing tests ...
    NeweggTests(self.driver, self.screenshot_manager, 
                self.report_generator, self.config),
]
```

## Code Examples

### Example 1: Custom Test with Self-Healing

```python
def test_custom_scenario(self):
    test_name = "Custom Test Scenario"
    
    try:
        self.driver.get("https://example.com")
        self.random_delay()
        
        element = self.find_element_with_retry([
            (By.ID, "main-button"),
            (By.CLASS_NAME, "primary-btn"),
            (By.XPATH, "//button[contains(text(),'Submit')]")
        ])
        
        if element:
            element.click()
            screenshot = self.take_screenshot(test_name)
            self.log_result(test_name, "PASS", "Element found and clicked", screenshot)
        else:
            self.log_result(test_name, "FAIL", "Element not found", 
                          self.take_screenshot(test_name))
            
    except Exception as e:
        self.log_result(test_name, "FAIL", str(e), 
                       self.take_screenshot(test_name))
```

### Example 2: Extracting Product Data

```python
def extract_all_products(self):
    products = []
    
    product_elements = self.driver.find_elements(By.CSS_SELECTOR, ".product-item")
    
    for product in product_elements:
        try:
            name = product.find_element(By.CSS_SELECTOR, ".title").text
            price = self.find_price_element()
            price_text = price.text if price else "Price not found"
            
            products.append({
                "name": name,
                "price": price_text
            })
        except:
            continue
    
    return products
```

## FAQ

**Q1: Why do some tests show WARNING instead of PASS?**

A: Websites frequently change their HTML structure. WARNING means the test completed but couldn't find specific elements. This is completely normal in real-world testing.

**Q2: Can I test my own website with this framework?**

A: Yes! Create a new test file following the pattern in test_amazon.py and add your website's URL and selectors.

**Q3: How do I stop the test mid-execution?**

A: Press Ctrl + C in the terminal. The browser will close automatically.

**Q4: Can I run this on a server without a GUI?**

A: Yes! Set HEADLESS_MODE = True in config.py and it will run without opening a browser window.

**Q5: How do I schedule this to run daily?**

A: Use Task Scheduler (Windows) or Cron (Mac/Linux) to run python main.py automatically.

**Q6: Are screenshots saved even for failed tests?**

A: Yes! Screenshots are captured for EVERY test case, regardless of status.

**Q7: How long does the full test suite take?**

A: Fast mode: 1-2 minutes, Normal mode: 2-4 minutes, Slow mode: 4-6 minutes.

**Q8: Can I run tests for just one website?**

A: Yes, comment out other test classes in test_runner.py.

## License

MIT License - See LICENSE file for details.

## Acknowledgments

- Selenium Team for the web automation framework
- WebDriver Manager for simplifying driver management
- Python Community for excellent libraries

---

## Quick Reference

### Commands

```bash
# Install
pip install selenium webdriver-manager pillow

# Run
python main.py

# View report (Windows)
start test_reports\*.html

# View report (Mac)
open test_reports/*.html

# View report (Linux)
xdg-open test_reports/*.html
```

### Key Files

| File | Purpose |
|------|---------|
| main.py | Start here |
| config.py | Change settings |
| test_base.py | Add common methods |
| test_reports/ | Find HTML reports |
| screenshots/ | Find captured images |

### Test Status

- PASS - Working perfectly
- WARNING - Minor issue, test completed
- FAIL - Test failed, check screenshot

---

Built with Python and Selenium

For latest updates, check the GitHub repository
```

This README uses only basic markdown formatting that GitHub definitely supports (no emojis, simple headers, standard code blocks, and plain tables). Just copy this entire text and paste it into your `README.md` file. It will display perfectly on GitHub!
