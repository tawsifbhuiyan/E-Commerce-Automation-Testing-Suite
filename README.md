



```markdown
# E-Commerce Automation Testing Suite

Python + Selenium automation framework that tests 8 e-commerce websites automatically.

## What It Does

- Tests Amazon, Flipkart, Best Buy, Target, Walmart, eBay, Myntra
- Searches products on each website
- Takes screenshots automatically
- Generates HTML test reports
- Handles popups and dynamic content

## Project Structure

ecommerce_testing_suite/
- main.py
- config.py
- test_base.py
- test_runner.py
- test_amazon.py
- test_flipkart.py
- test_bestbuy.py
- test_target.py
- test_walmart.py
- test_ebay.py
- test_myntra.py
- screenshot_manager.py
- report_generator.py
- webdriver_factory.py
- utils.py
- screenshots/
- test_reports/

## Installation

1. Install Python 3.8 or higher

2. Install required packages:

   pip install selenium webdriver-manager pillow

3. Make sure Google Chrome is installed

## How to Run

   python main.py

## Console Output

Running tests for: Amazon
[PASS] Amazon - Search Products: Found 24 products
[PASS] Flipkart - Navigation Menu: Successfully hovered menu
[PASS] Best Buy - Product Details: Search successful
[PASS] Target - Add to Cart: Found products
[PASS] Walmart - Price Comparison: Results loaded
[PASS] eBay - Infinite Scroll: Scrolled successfully
[PASS] Myntra - Filter Combinations: Search successful

TEST EXECUTION COMPLETED
Report: test_reports/test_report.html
Screenshots: screenshots/

## Test Results

PASS - Test passed
WARNING - Minor issue, test completed
FAIL - Test failed, check screenshot

## Configuration

Edit config.py to change:

HEADLESS_MODE = False      (Run without browser window)
RANDOM_DELAY_MIN = 2.0     (Minimum delay between actions)
RANDOM_DELAY_MAX = 4.0     (Maximum delay between actions)

## Common Issues

WebDriver error: Update Chrome and run pip install --upgrade webdriver-manager

Permission denied: Run terminal as Administrator

Time not defined: Add import time to the test file

## Adding a New Website

1. Create test_newsite.py
2. Extend BaseTest class
3. Add URL to config.py
4. Import in test_runner.py

## Requirements

- Python 3.8+
- Google Chrome
- selenium
- webdriver-manager
- pillow

## License

MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

