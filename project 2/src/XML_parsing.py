import requests
from bs4 import BeautifulSoup
import pandas as pd

class sitemapParser:
    def __init__(self, website_url):
        self.website_url = website_url
        self.sitemaps = []

    def fetch_robots_txt(self):
        try:
            robots_url = f"{website_url}/robots.txt"
            response = requests.get(robots_url)
            if response.status_code == 200:
                return response.text
            else:
                raise Exception("Failed to fetch robots.txt")
        except Exception as e:
            print(f"Error fetching robots.txt: {e}")
            return None

    def parse_robots_txt(self, robots_txt):
        if not robots_txt:
            return

        lines = robots_txt.split('\n')
        for line in lines:
            if line.strip().startswith('Sitemap:'):
                parts = line.strip().split(' ')
                if len(parts) == 2:
                    self.sitemaps.append(parts[1])

    def parse_sitemaps_to_dataframe(self):
        if not self.sitemaps:
            print("No sitemaps found in robots.txt")
            return None

        sitemap_data = []
        for sitemap_xmls in self.sitemaps:
            try:
                response = requests.get(sitemap_xmls)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'xml')
                    xmls = [loc.text for loc in soup.find_all('loc')]
                    for urls in xmls:
                        responses = requests.get(urls)
                        soups = BeautifulSoup(responses.text, 'xml')
                        urls = [url.text for url in soups.find_all('loc')]
                        sitemap_data.extend(urls)
                else:
                    print(f"Failed to fetch sitemap: {sitemap_xmls}")
            except Exception as e:
                print(f"Error parsing sitemap: {e}")

        if sitemap_data:
            df = pd.DataFrame({'URL': sitemap_data})
            return df
        else:
            return None

    def run(self):
        robots_txt = self.fetch_robots_txt()
        self.parse_robots_txt(robots_txt)
        dataframe = self.parse_sitemaps_to_dataframe()
        return dataframe

website_url = "https://www.fandom.com" 
sitemap_parser = sitemapParser(website_url)
df = sitemap_parser.run()

if df is not None:
    print(df)