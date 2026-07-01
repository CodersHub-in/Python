import csv
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

# Replace 'https://example.com' with the website you want to scrape
url = 'https://www.codershubinc.com/sponsors'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# Initialize variables for the loading bar
headlines = soup.find_all('h2')
headlines += soup.find_all('h3')
headlines += soup.find_all('p')
headlines_list = []

# Loop through the headlines and extract the text
for headline in tqdm(headlines, desc="Scraping Headlines"):
    headlines_list.append(headline.text.strip())
    time.sleep(1)

# Create a CSV file and write the headlines to it
with open('headlines.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Headline']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for headline in headlines_list:
        writer.writerow({'Headline': headline})

print("\nHeadlines saved to headlines.csv.")
