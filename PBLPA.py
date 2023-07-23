from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
from operator import itemgetter
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
import logging

# Let's set up some basic logging
logging.basicConfig(level=logging.INFO)

class LotteryScraper:
    def __init__(self, url, top_n=10):
        self.url = url
        self.top_n = top_n
        self.service = Service(ChromeDriverManager().install())
        self.options = Options()
        self.options.headless = True  # We're running this headless - no GUI for us!

    def request_data(self):
        # Nothing too crazy here, just setting up our webdriver
        driver = None
        try:
            driver = webdriver.Chrome(service=self.service, options=self.options)
            driver.get(self.url)
            html = driver.page_source
        except Exception as err:
            # If something goes wrong, we want to know about it
            logging.error(f"Ouch, hit a snag: {err}")
            return None
        finally:
            # Always be sure to close that driver
            if driver is not None:
                driver.quit()
        return html

    def parse_html(self, html):
        # BeautifulSoup does a great job making HTML navigable
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('div', {'class': 'winning_numbers'})
        if table is None:
            # If there's no table, there's not much for us to do
            logging.warning('Bummer, no table found in the web page.')
            return []
        table_data = []

        # Loop through each row in the table, snagging the data
        for row in table.find_all('li'):
            cols = [col.get_text() for col in row.find_all('span')]
            table_data.append(cols)

        return table_data

    def prepare_data(self, table_data):
        # We've got the data, now let's shape it for analysis
        df = pd.DataFrame(table_data, columns=['Draw Date', 'Winning Numbers'])
        df['Draw Date'] = pd.to_datetime(df['Draw Date'])
        df['Winning Numbers'] = df['Winning Numbers'].apply(lambda x: list(map(int, x.split())))
        return df['Winning Numbers'].tolist()

    @staticmethod
    def convert_to_int(x):
        # This is a pretty straightforward conversion, but there's always a chance of ValueError
        try:
            return list(map(int, x.split()))
        except ValueError:
            logging.error("Had an issue turning these strings into integers.")
            return []

    def calculate_probabilities(self, frequencies):
        # Divide each frequency by the total to get probability
        total = sum(frequencies.values())
        probabilities = {k: v / total for k, v in frequencies.items()}
        return probabilities

    def visualize_probabilities(self, probabilities_sorted):
        # Now for the fun part - let's see a visual of our data
        numbers = [str(num) for num, _ in probabilities_sorted[:self.top_n]]
        probabilities = [prob for _, prob in probabilities_sorted[:self.top_n]]

        plt.bar(numbers, probabilities)
        plt.xlabel('Number')
        plt.ylabel('Probability')
        plt.title(f'Top {self.top_n} Numbers by Probability')
        plt.show()

    def scrape(self):
        # Let's bring all the steps together
        html = self.request_data()
        if html is not None:
            table_data = self.parse_html(html)
            lottery_data = self.prepare_data(table_data)

            # Let's map out the frequencies with ProcessPoolExecutor - super efficient!
            with ProcessPoolExecutor() as executor:
                frequencies = Counter(executor.map(lambda draw: tuple(draw), lottery_data))

            # Now we'll calculate probabilities
            probabilities = self.calculate_probabilities(frequencies)

            # Let's get those probabilities sorted
            probabilities_sorted = sorted(probabilities.items(), key=itemgetter(1), reverse=True)

            # And finally, we'll visualize the top N probabilities
            self.visualize_probabilities(probabilities_sorted)

if __name__ == "__main__":
    # The Powerball URL is our target
    url = 'https://www.powerball.com/winning-numbers'  
    scraper = LotteryScraper(url, top_n=15)
    scraper.scrape()
