'''
Part 3: GU Analysis

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

import pandas as pd
import numpy as np
import json
import requests

d = requests.get('https://api.godsunchained.com/proto/purity')
n = requests.get('https://api.godsunchained.com/proto')
cardDist = d.json()
cardNames = n.json()


cardDist_df = pd.DataFrame(cardDist)#columns = col_names)
cardNames_df = pd.DataFrame(cardNames)


'''
Here we use the cardNames dataframe to output the id's of the cards
'''
dist_id = []
for val in cardNames_df.id:
	dist_id.append(val)

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
			info_list.append(int(cardDist_df[str(id)][i]))

	data.append(info_list)
	info_list = []

card_df = pd.DataFrame(data)
col_names = ['Name', 'Rarity', 'Normal','Shadow','Gold','Diamond']
card_df.columns = col_names

legendaries = 0
rares = 0
epics = 0
commons = 0

leg_dict = {}
epics_dict = {}
sum_shine_epics = 0
sum_shine_leg = 0

#Show how many of each card exist
for index, row in card_df.iterrows():
    #print(row['Rarity'])

    if row['Rarity'] == 'Common' or row['Rarity'] =='common':
        commons += row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

    elif row['Rarity'] == 'Rare' or row['Rarity'] =='rare':
        rares += row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

    elif row['Rarity'] == 'Epic' or row['Rarity'] =='epic':
        sum_shine_epics = row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

        epics_dict[row['Name']] = sum_shine_epics
        epics += sum_shine_epics

    elif row['Rarity'] == 'Legendary' or row['Rarity'] =='legendary':
        sum_shine_leg = row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

        leg_dict[row['Name']] = sum_shine_leg
        legendaries += sum_shine_leg

amount = [commons, rares, epics, legendaries]

norm_amount = [commons*100/sum(amount), rares*100/sum(amount), epics*100/sum(amount), legendaries*100/sum(amount)]
