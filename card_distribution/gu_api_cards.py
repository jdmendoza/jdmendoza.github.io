'''
Part 1: The Better Way

This python script is used to take a txt file with Gods Unchained Data in the following format:
-----gu1.txt----------
Name Rarity Normal Shadow Gold Diamond
Levitate Common 3475 184 31 3
Spellbound Common 3495 178 41 10
...
----------------------
Once the data is imported, we can manipulate the dataframe (Pandas data structure)
to look at trends and such
'''
import json
import requests
import pandas as pd


'''
Here we use the requests package to access the Gods Unchained API.
'''
d = requests.get('https://api.godsunchained.com/proto/purity')
n = requests.get('https://api.godsunchained.com/proto')
cardDist = d.json()
cardNames = n.json()

'''
We can directly import the json into dataframes.
No ugly html need. How cool is that!
'''
cardDist_df = pd.DataFrame(cardDist)#columns = col_names)
cardNames_df = pd.DataFrame(cardNames)


'''
Here we use the cardNames dataframe to output the id's of the cards
'''
dist_id = []
for val in cardNames_df.id:
	dist_id.append(val)

'''
We traverse through all the id, pull the relevant data and store in a nested list.
It is important to note that there are issues with a few entries,
I used if statements to ignore them
'''
info_list = []
data = []
shine = ['plain', 'shadow', 'gold', 'diamond']

for id in dist_id:
	if id == 379: #| id == 380 | id == 381): #erroneous cards
		print('id=379 ignored')

	elif id == 378:
		print('id=378 ignored')

	else:
		row = dist_id.index(id)
		info_list.append(cardNames_df['name'][row])
		info_list.append(cardNames_df['rarity'][row])

		for i in shine:
			info_list.append(cardDist_df[str(id)][i])

	data.append(info_list)
	info_list = []

'''
Here we take the nested list and store it in a dataframe.
We then put all the data into a text file for the next script in the pipeline
'''

card_df = pd.DataFrame(data)
col_names = ['Name', 'Rarity', 'Normal','Shadow','Gold','Diamond']
card_df.columns = col_names

card_df.to_csv(r'guAll.txt', index=None, sep=' ', mode='a')
