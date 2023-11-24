import requests
from bs4 import BeautifulSoup
import pandas as pd


class sitemapParser:
    """
    Class contains code which extracts data after parsing sitemaps of https://www.fandom.com from robots.txt file and
    returns as a dataframe
    """

    def __init__(self, website_url):
        self.website_url = website_url
        self.sitemaps = []

    def fetch_robots_txt(self):
        """
        This function fetches the robots.txt file

        Args:
        self - contains the url of the website

        Return:
        response.text - returns the response of the url
        """
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
        """
        Function fetches the sitemap from the robots.txt file

        Args:
        robots_txt - which is the robots.txt of the website

        Return:
        none
        """
        if not robots_txt:
            return

        lines = robots_txt.split("\n")
        for line in lines:
            if line.strip().startswith(
                "Sitemap:"
            ):  # Extracts the line containing sitemaps
                parts = line.strip().split(" ")
                if len(parts) == 2:
                    self.sitemaps.append(parts[1])  # Appending to a sitemaps list

    def parse_sitemaps_to_dataframe(self):
        """
        Extracting data from sitemaps to a dataframe

        Args:
        self - contains all the sitemaps from robots.txt

        Return:
        df - dataframe containing data's of sitemap
        """
        if not self.sitemaps:
            print("No sitemaps found in robots.txt")
            return None

        sitemap_data = []
        for sitemap_xmls in self.sitemaps:
            try:
                response = requests.get(sitemap_xmls)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "xml")
                    xmls = [
                        loc.text for loc in soup.find_all("loc")
                    ]  # data is extracted from the loc tag from xml
                    for urls in xmls:
                        responses = requests.get(urls)
                        soups = BeautifulSoup(responses.text, "xml")
                        urls = [url.text for url in soups.find_all("loc")]
                        sitemap_data.extend(urls)
                else:
                    print(f"Failed to fetch sitemap: {sitemap_xmls}")
            except Exception as e:
                print(f"Error parsing sitemap: {e}")

        if sitemap_data:
            df = pd.DataFrame({"URL": sitemap_data})
            return df
        else:
            return None

    def run(self):
        """
        Function which returns the dataframe when the package is imported
        """
        robots_txt = self.fetch_robots_txt()
        self.parse_robots_txt(robots_txt)
        dataframe = self.parse_sitemaps_to_dataframe()
        return dataframe


website_url = "https://www.fandom.com"  # Website URL
sitemap_parser = sitemapParser(website_url)
df = sitemap_parser.run()

if df is not None:
    print(df)
