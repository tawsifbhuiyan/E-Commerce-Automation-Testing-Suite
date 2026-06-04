"""
Utility functions for common operations
"""
import re
import random
from typing import List, Dict

class TestUtils:
    """Utility functions for test automation"""
    
    @staticmethod
    def extract_price(text: str) -> float:
        """Extract price from text"""
        match = re.search(r'\$?(\d+(?:\.\d{2})?)', text)
        if match:
            return float(match.group(1))
        return 0.0
    
    @staticmethod
    def generate_unique_email() -> str:
        """Generate unique email for testing"""
        import time
        return f"test_user_{int(time.time())}_{random.randint(1000,9999)}@example.com"
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean text by removing extra spaces and newlines"""
        return ' '.join(text.split()).strip()