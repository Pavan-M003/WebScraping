from selenium import webdriver
import pandas as pd

# setting up target and path of a webdriver
website = "https://www.indiatoday.in/" # Website link
path = "./chrome-headless-shell.exe"   # Webdriver path

driver = webdriver.Chrome()
driver.get(website)


titles = []
subtitles =[]
links = []


containers = driver.find_elements(by="xpath", value='//div[@class="B1S3_content__wrap__9mSB6"]')

# using loop iterate through all the news
for container in containers:
    title = container.find_element(by="xpath", value='./h2/a').text
    subtitle = container.find_element(by="xpath", value='.//p').text
    link = container.find_element(by="xpath", value='./h2/a').get_attribute("href")

#     append the extracted data in variables
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Exporting Data to a CSV file
my_dict = {"title": titles,
           "subtitle": subtitles,
           "link": links
           }

headlines = pd.DataFrame(my_dict)
headlines.to_csv("headline.csv")

driver.quit()