import requests
from bs4 import BeautifulSoup
import pandas as pd

class DataMiner:
    def __init__(self, url):
        self.url = url
    
    # Fetch the content of the web page
    def fetch_page(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch the page. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error during fetching page: {e}")
        return None
    
    # Parse the content and extract relevant data
    def parse_page(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Extracting all <h2> tags and their text content
        data = []
        for tag in soup.find_all('h2'):
            data.append(tag.text.strip())

        return data
    
    # Store the extracted data in a CSV file
    def save_to_csv(self, data, filename='output.csv'):
        df = pd.DataFrame(data, columns=['Extracted Data'])
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    
    # Full process: Fetch, Parse, and Save
    def scrape_and_save(self):
        html_content = self.fetch_page()
        if html_content:
            extracted_data = self.parse_page(html_content)
            self.save_to_csv(extracted_data)

# Example usage
url = 'https://example.com'  # Replace with your target website
miner = DataMiner(url)
miner.scrape_and_save()
