import requests
from bs4 import BeautifulSoup
import pandas as pd


class goodreadsquoteScraper:
    """
    Class which extracts data by scraping https://www.goodreads.com/quotes and returns into a dataframe
    """

    def __init__(self, base_url="https://www.goodreads.com/quotes"):
        self.base_url = base_url

    def get_page_content(self, url):
        """
        Fetching content of website using requests.get()

        Args:
        url - url of webpage

        Returns:
        text - response.text has the response of url
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(
                    f"Failed to retrieve content. Status code: {response.status_code}"
                )
                return None
        except Exception as e:
            print(f"An error occurred while fetching content: {e}")
            return None

    def scrape_quotes(self, num_pages=1):
        """
        parsing the contents of website using beautifulsoup and appending it into a quotes lists

        Args:
        num_pages - number of pages scraped

        Returns:
        quotes - quotes scraped from website which is a list
        """
        quotes = []

        for page_num in range(1, num_pages + 1):
            page_url = f"{self.base_url}?page={page_num}"

            page_content = self.get_page_content(page_url)
            if page_content is None:
                break

            soup = BeautifulSoup(page_content, "html.parser")
            quote_elements = soup.find_all("div", class_="quoteDetails")

            for quote_element in quote_elements:
                quote_text = quote_element.find(
                    "div", class_="quoteText"
                ).text.strip()  # stores the quotes
                quote_author = quote_element.find(
                    "span", class_="authorOrTitle"
                ).text.strip()  # Stores the name of authors

                quotes.append({"quote": quote_text, "author": quote_author})

        return quotes

    def create_dataframe(self, quotes):
        """
        converts the quotes lists into a dataframe and returns it

        Args:
        quotes - scraped quotes from website

        Return:
        df - data in quotes list is converted into this dataframe
        """
        goodreads_scraper = goodreadsquoteScraper()
        quotes = goodreads_scraper.scrape_quotes(num_pages=100)
        if quotes:
            df = pd.DataFrame(quotes)
            print(df)
        else:
            print("Failed to scrape quotes.")
