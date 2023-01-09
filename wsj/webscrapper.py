import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv = Service('/Users/s/Desktop/chrome driver/chromedriver')

driver = webdriver.Chrome(service=serv)
driver.get('https://www.wsj.com/news/business?mod=nav_top_section')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs='WSJTheme--headline--7VCzo7Ay'):
    name = a.find('h3')
    if name not in results:
        results.append(name.text)

df = pd.DataFrame({'Name': results})
df.to_csv('wsj.csv', index=False, encoding='utf-8')