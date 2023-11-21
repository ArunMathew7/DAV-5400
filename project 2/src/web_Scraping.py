import requests
from bs4 import BeautifulSoup
import pandas as pd

class goodreadsquoteScraper:
    def __init__(self, base_url="https://www.goodreads.com/quotes"):
        self.base_url = base_url

    def get_page_content(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to retrieve content. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching content: {e}")
            return None

    def scrape_quotes(self, num_pages=1):
        quotes = []

        for page_num in range(1, num_pages + 1):
            page_url = f"{self.base_url}?page={page_num}"

            page_content = self.get_page_content(page_url)
            if page_content is None:
                break

            soup = BeautifulSoup(page_content, 'html.parser')
            quote_elements = soup.find_all('div', class_='quoteDetails')

            for quote_element in quote_elements:
                quote_text = quote_element.find('div', class_='quoteText').text.strip()
                quote_author = quote_element.find('span', class_='authorOrTitle').text.strip()

                quotes.append({"quote": quote_text, "author": quote_author})

        return quotes

    def create_dataframe(self, quotes):
        goodreads_scraper = goodreadsquoteScraper()
        quotes = goodreads_scraper.scrape_quotes(num_pages=100) 
        if quotes:
            df = pd.DataFrame(quotes)
            print(df)
        else:
            print("Failed to scrape quotes.")
