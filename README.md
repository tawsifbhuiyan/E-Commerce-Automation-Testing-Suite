# 🚀 E-Commerce Automation Testing Suite

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.15+-green.svg)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Test Status](https://img.shields.io/badge/Tests-Automated-brightgreen.svg)]()

## 📋 Overview

The **E-Commerce Automation Testing Suite** is a professional, production-ready automation framework built with Python and Selenium. It automatically tests **8 major e-commerce websites**, captures screenshots, generates beautiful HTML reports, and handles real-world web automation challenges like dynamic content, popups, and website structure changes.

### 🎯 What This Project Does

This project **automatically**:
- ✅ Tests shopping flows across Amazon, Flipkart, Best Buy, Target, Walmart, eBay, and Myntra
- ✅ Searches for products on each website
- ✅ Captures screenshots of every test step
- ✅ Generates professional HTML test reports with pass/fail statistics
- ✅ Handles cookies, popups, and dynamic content
- ✅ Simulates real user behavior with random delays
- ✅ Performs infinite scroll testing (eBay)
- ✅ Tests filter combinations (Amazon, Myntra)
- ✅ Extracts product information and prices

### 🤔 Why This Project is Unique

Unlike basic Selenium scripts that test just one website, this framework:
1. **Tests 8 different websites** in a single execution
2. **Self-healing selectors** that adapt to website changes
3. **Professional reporting** with clickable screenshots
4. **Modular architecture** - add new websites in minutes
5. **Real-world testing** - handles popups, delays, and dynamic content
6. **Visual debugging** with element highlighting
7. **Performance metrics** for page load times

## 📸 Demo

### Test Execution in Action
![Test Execution Demo](https://via.placeholder.com/800x400?text=Browser+Automation+Demo)

### Generated HTML Report
![HTML Report](https://via.placeholder.com/800x400?text=Beautiful+HTML+Report)

### Screenshots Captured
![Screenshots](https://via.placeholder.com/800x400?text=Automatic+Screenshots)

## 🏗️ Project Structure
ecommerce_testing_suite/
│
├── 📁 screenshots/ # All captured screenshots (auto-created)
│ ├── Amazon_Search_20240101.png
│ ├── Flipkart_Navigation_20240101.png
│ └── ...
│
├── 📁 test_reports/ # HTML test reports (auto-created)
│ └── test_report_20240101.html
│
├── 📄 main.py # Entry point - Run this!
├── 📄 config.py # All configuration settings
├── 📄 webdriver_factory.py # Browser setup and management
├── 📄 screenshot_manager.py # Screenshot capture and storage
├── 📄 report_generator.py # HTML report generation
├── 📄 test_base.py # Base class with common methods
├── 📄 test_runner.py # Orchestrates all test execution
│
├── 📄 test_amazon.py # Amazon specific tests
├── 📄 test_flipkart.py # Flipkart specific tests
├── 📄 test_bestbuy.py # Best Buy specific tests
├── 📄 test_target.py # Target specific tests
├── 📄 test_walmart.py # Walmart specific tests
├── 📄 test_ebay.py # eBay specific tests
├── 📄 test_myntra.py # Myntra specific tests
│
└── 📄 utils.py # Utility functions

text

## 🚀 Features

### Core Features
| Feature | Description | Status |
|---------|-------------|--------|
| Multi-site testing | Tests 8 different e-commerce websites | ✅ |
| Screenshot capture | Automatic screenshots for every test | ✅ |
| HTML reports | Professional reports with statistics | ✅ |
| Self-healing selectors | Finds elements even if selectors change | ✅ |
| Popup handling | Automatically closes cookies and modals | ✅ |
| Random delays | Simulates human behavior | ✅ |
| Error handling | Graceful failure with screenshots | ✅ |
| Performance metrics | Page load time tracking | ✅ |

### Test Coverage

| Website | Test Case | Status |
|---------|-----------|--------|
| Amazon | Product Search & Filters | ✅ |
| Flipkart | Navigation Menu Hover | ✅ |
| Best Buy | Product Search | ✅ |
| Target | Add to Cart Flow | ✅ |
| Walmart | Price Comparison | ✅ |
| eBay | Infinite Scroll | ✅ |
| Myntra | Filter Combinations | ✅ |

## 📦 Prerequisites

### Required Software
- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **Google Chrome Browser** - [Download Chrome](https://www.google.com/chrome/)
- **Git** (optional, for cloning) - [Download Git](https://git-scm.com/)

### Required Python Packages
selenium==4.15.0
webdriver-manager==4.0.1
pillow==10.1.0

text

## 🛠️ Installation

### Step 1: Clone or Download the Project

```bash
# Clone the repository
git clone https://github.com/yourusername/ecommerce-testing-suite.git

# Navigate to project directory
cd ecommerce-testing-suite
Or download the ZIP file and extract it.

Step 2: Install Python Packages
Open Command Prompt (CMD) or Terminal and run:

bash
pip install selenium webdriver-manager pillow
Step 3: Verify Installation
Create a quick test file to verify everything works:

python
# test_setup.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

print("Testing setup...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
print("✅ Setup successful! Browser opened!")
driver.quit()
Run it:

bash
python test_setup.py
🎮 How to Run
Basic Execution
bash
python main.py
What Happens When You Run:
Chrome browser opens automatically

Tests start executing on each website:

Amazon searches for products

Flipkart hovers over menus

Best Buy searches for items

Target adds items to cart

Walmart compares prices

eBay tests infinite scroll

Myntra applies filters

Console shows real-time progress:

text
🚀 STARTING TEST EXECUTION
============================================================

📝 Running tests for: Amazon
----------------------------------------
[PASS] Amazon - Search Products: Found 24 products
[WARNING] Amazon - Apply Filters: Filter elements not found

📝 Running tests for: Flipkart
----------------------------------------
[PASS] Flipkart - Navigation Menu: Successfully hovered menu
Screenshots are saved in screenshots/ folder

HTML report is generated in test_reports/ folder

Advanced Options
Run in Headless Mode (No Browser Window)
Edit config.py:

python
HEADLESS_MODE: bool = True  # Change from False to True
Run Specific Tests Only
Modify test_runner.py:

python
# Comment out websites you don't want to test
test_classes = [
    AmazonTests(...),
    FlipkartTests(...),
    # BestBuyTests(...),  # Disabled
    # TargetTests(...),   # Disabled
]
Increase/Decrease Test Speed
Edit config.py:

python
RANDOM_DELAY_MIN: float = 1.0  # Minimum delay between actions
RANDOM_DELAY_MAX: float = 2.0  # Maximum delay between actions
📊 Understanding Test Results
Test Status Meanings
Status	Meaning	What to Do
✅ PASS	Test completed successfully	Nothing - it's working!
⚠️ WARNING	Test completed but with minor issues	Check screenshot; usually normal
❌ FAIL	Test failed completely	Check internet connection or website changes
Reading the HTML Report
Open the report: Double-click any .html file in test_reports/

View statistics: See total tests, passes, failures at the top

Check screenshots: Click on any screenshot thumbnail to enlarge

Review timestamps: See exactly when each test ran

Sample Report Output
text
============================================================
✅ TEST EXECUTION COMPLETED
📊 Report generated at: test_reports/test_report_20240101_143030.html
📸 Screenshots saved in: screenshots
============================================================

✨ Test suite completed successfully!
📄 Open the report to view details
