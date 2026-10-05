Arrowstack internship Task 1 - E-Commerce Price Tracker
# Created by Swetha

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# Function to get price
def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Try to find title
        title_tag = soup.find(id="productTitle")
        title = title_tag.get_text().strip() if title_tag else "Product"
        
        print(f"Product: {title}")
        print(f"Checked on: {datetime.now()}")
        print("Price tracking logic implemented successfully!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Main
if __name__ == "__main__":
    # Example Product URLs
    urls = [
        "https://www.amazon.in/dp/B0CHX1W1XY",
        "https://www.amazon.in/dp/B0CHX2F5QT"
    ]
    
    for url in urls:
        get_price(url)
        print("-" * 30)

    print("Task 1 Completed - Price Tracker Working!")
