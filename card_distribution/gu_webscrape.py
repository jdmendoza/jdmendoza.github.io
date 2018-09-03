"""
Part 1: Using Web-Scraping

This part of the code is used to scrape data from the Gods Unchained webpage
This script outputs a text file with one page equivalent to of card data
"""
#Include the instructions to isntall webdriver
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time



'''
Using selenium to open chrome and go to the webpage, this is required becuase
the page needs to be rendered. Just looking at the html of the page returns
javascript and no data on the cards.
'''
browser = webdriver.Chrome()
url = "https://godsunchained.com/genesis-set"
url = "https://medium.com/@jdannym93/relative-value-of-cards-in-gods-unchained-b875a1cee7e0"
browser.get(url)

'''
We need to pause before reading the data, since we must manually change to the
to the next page (1 to 12 for the genesis set)
'''
time.sleep(10)

innerHTML = browser.execute_script("return document.body.innerHTML")
browser.quit()

'''
Once we have the massive innerHTML data, we need to search for the relevant data,
we can use BeautifulSoup + functions to parse the html and make it sligtly easier to traverse.
'''
parsed_html = BeautifulSoup(innerHTML, features="lxml")
names = parsed_html.find_all('div', class_=("noselect name")) #Prints the card name
rarities = parsed_html.findAll("div", class_=("backlight"))
shinies = parsed_html.find_all('p') #Contains only availible


'''
Preparing the dataframe with column names
'''
col_names = ['Name', 'Rarity', 'Normal','Shadow','Gold','Diamond']
card_df = pd.DataFrame(columns = col_names)
info_list = []

'''
Here we prepare the the list so we have the table in an intuitive form
and to be ready for some analysis!
'''
for card in range(0,25):
    info_list.append(names[card].text)
    info_list.append(rarities[0+card]['class'][1])

    x = 1 + card*4
    y = 5 + card*4

    for i in shinies[x:y]:
        info_list.append(int(i.text))
    card_df.loc[len(card_df)] = info_list
    info_list = []

print(card_df)

'''
Saves the dataframe to a text file for the next step in the pipeline
'''
card_df.to_csv(r'gu1.txt', index=None, sep=' ', mode='a')
