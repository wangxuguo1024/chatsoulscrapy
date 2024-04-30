import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
sourceurl = "https://www.zhihu.com/column/c_1272930684131704832"
# Set up the Selenium driver
driver = webdriver.Chrome()  # Replace with your preferred browser

# Send a GET request to the webpage
response = requests.get(sourceurl)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Use Selenium to scroll down and load more data
driver.get(response.url)
time.sleep(10)
while driver.find_element(By.NAME,)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Find all the article links and titles on the page
article_links = []
article_titles = []
for item in soup.find_all('div', {'class': 'RichTextContainer'}):
    for link in item.find_all('a'):
        article_links.append(link.get('href'))
    title = item.find('h1').text.strip()
    article_titles.append(title)

# Print the scraped links and titles
print("Article Links:")
for link in article_links:
    print(link)
print("\nArticle Titles:")
for title in article_titles:
    print(title)

# Clean up
driver.quit()
