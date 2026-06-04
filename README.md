
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

```
ecommerce_testing_suite/
├── main.py                 # Run this file
├── config.py               # Settings
├── test_base.py            # Base test class
├── test_runner.py          # Runs all tests
├── test_amazon.py          # Amazon tests
├── test_flipkart.py        # Flipkart tests
├── test_bestbuy.py         # Best Buy tests
├── test_target.py          # Target tests
├── test_walmart.py         # Walmart tests
├── test_ebay.py            # eBay tests
├── test_myntra.py          # Myntra tests
├── screenshot_manager.py   # Takes screenshots
├── report_generator.py     # Creates HTML reports
├── webdriver_factory.py    # Sets up browser
├── utils.py                # Helper functions
├── screenshots/            # Screenshots saved here
└── test_reports/           # HTML reports saved here
```

## Installation

1. Install Python 3.8 or higher

2. Install required packages:
```bash
pip install selenium webdriver-manager pillow
```

3. Make sure Google Chrome is installed

## How to Run

```bash
python main.py
```

## What You'll See

Console output:
```
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
```

## Test Results

| Status | Meaning |
|--------|---------|
| PASS | Test passed |
| WARNING | Minor issue, test completed |
| FAIL | Test failed, check screenshot |

## Configuration

Edit `config.py` to change:

```python
HEADLESS_MODE = False      # Run without browser window
RANDOM_DELAY_MIN = 2.0     # Minimum delay between actions
RANDOM_DELAY_MAX = 4.0     # Maximum delay between actions
```

## Common Issues

**WebDriver error**: Update Chrome and run `pip install --upgrade webdriver-manager`

**Permission denied**: Run terminal as Administrator

**Time not defined**: Add `import time` to the test file

## Adding a New Website

1. Create `test_newsite.py`
2. Extend `BaseTest` class
3. Add URL to `config.py`
4. Import in `test_runner.py`

## Requirements

- Python 3.8+
- Google Chrome
- selenium
- webdriver-manager
- pillow

## License

MIT License
```

This is short, clean, and will display perfectly on GitHub. Just copy and paste this entire text into your `README.md` file.




