"""
Configuration settings for the automation suite
"""
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class TestConfig:
    """Central configuration for all tests"""
    # Browser settings
    HEADLESS_MODE: bool = False
    IMPLICIT_WAIT: int = 10
    EXPLICIT_WAIT: int = 15
    
    # Test settings
    RANDOM_DELAY_MIN: float = 2.0
    RANDOM_DELAY_MAX: float = 4.0
    MAX_RETRIES: int = 3
    
    # URLs
    AMAZON_URL: str = "https://www.amazon.com"
    FLIPKART_URL: str = "https://www.flipkart.com"
    BESTBUY_URL: str = "https://www.bestbuy.com"
    TARGET_URL: str = "https://www.target.com"
    WALMART_URL: str = "https://www.walmart.com"
    EBAY_URL: str = "https://www.ebay.com"
    MYNTRA_URL: str = "https://www.myntra.com"
    
    # Search terms - Using default_factory instead of direct dict
    SEARCH_TERMS: Dict[str, List[str]] = field(default_factory=lambda: {
        "amazon": ["laptop backpack", "wireless mouse"],
        "bestbuy": ["wireless mouse", "gaming keyboard"],
        "target": ["water bottle", "coffee maker"],
        "walmart": ["headphones", "smartwatch", "power bank"],
        "ebay": ["vintage watches", "collectible coins"],
        "myntra": ["t-shirts", "jeans"]
    })
    
    # Report settings
    REPORT_DIR: str = "test_reports"
    SCREENSHOT_DIR: str = "screenshots"
    
    def create_directories(self):
        """Create necessary directories"""
        import os
        for directory in [self.REPORT_DIR, self.SCREENSHOT_DIR]:
            if not os.path.exists(directory):
                os.makedirs(directory)