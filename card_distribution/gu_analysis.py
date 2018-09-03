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
import matplotlib.pyplot as plt

'''
Data Collected August 29, 2018 @ ~3pm
'''
#Ask in the medium post how to more efficiently do this if I have access to the json

'''
df1 = pd.read_table("gu1.txt", delim_whitespace=True)
df2 = pd.read_table("gu2.txt", delim_whitespace=True)
df3 = pd.read_table("gu3.txt", delim_whitespace=True)
df4 = pd.read_table("gu4.txt", delim_whitespace=True)
df5 = pd.read_table("gu5.txt", delim_whitespace=True)
df6 = pd.read_table("gu6.txt", delim_whitespace=True)
df7 = pd.read_table("gu7.txt", delim_whitespace=True)
df8 = pd.read_table("gu8.txt", delim_whitespace=True)
df9 = pd.read_table("gu9.txt", delim_whitespace=True)
df10 = pd.read_table("gu10.txt", delim_whitespace=True)
df11 = pd.read_table("gu11.txt", delim_whitespace=True)
df12 = pd.read_table("gu12.txt", delim_whitespace=True)

card_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12])
'''
card_df = pd.read_table("/guAll.txt", delim_whitespace=True)

legendaries = 0
rares = 0
epics = 0
commons = 0

'''
I store specific names in a dictionary for convience.
I know exactly what entry I'm looking at since it is the name of the card
'''
leg_dict = {}
epics_dict = {}

'''
This "for loop" goes through each row of data
and extracts values to calculate the amount a specified card
'''
#Show how many of each card exist
for index, row in card_df.iterrows():
    if row['Rarity'] == 'Common':
        commons = commons + row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

    elif row['Rarity'] == 'Rare':
        rares = rares + row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

    elif row['Rarity'] == 'Epic':
        sum_shine_epics = row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

        epics_dict[row['Name']] = sum_shine_epics
        epics += sum_shine_epics

    elif row['Rarity'] == 'Legendary':
        sum_shine_leg = row['Normal'] + row['Shadow'] + row['Gold'] + row['Diamond']

        leg_dict[row['Name']] = sum_shine_leg
        legendaries += sum_shine_leg
'''
Store the sums in a list to move around more easily
'''
amount = [commons, rares, epics, legendaries]

'''
Normalizing the array,
this is equivalent to showing the percentage each group is of the whole
'''
norm_amount = [commons*100/sum(amount), rares*100/sum(amount), epics*100/sum(amount), legendaries*100/sum(amount)]
#print(norm_amount)
#print('Leg',len(leg_dict), 'Epics', len(epics_dict))

'''
Uncomment this line to save a list to a csv file.
This makes it easy to share data.
#np.savetxt("file_name.csv", norm_amount, delimiter=",", fmt='%s')
'''

'''
This section plots the data that is in the dictionaries
'''
'''
#This shows copies of each legendary exist
plt.bar(range(len(leg_dict)), leg_dict.values(), align='center')
plt.xticks(range(len(leg_dict)), list(leg_dict.keys()), rotation='vertical')
plt.show()
'''
#This plots the distribute of the different rarities
barlist = plt.bar(['Common', 'Rare', 'Epic', 'Legendary'], amount, align='center', alpha=0.5)
barlist[0].set_color('grey')
barlist[1].set_color('blue')
barlist[2].set_color('purple')
barlist[3].set_color('gold')
plt.ylabel('Amount of Cards Found')
plt.title('Gods Unchained: Card Rarity Distribution')
plt.show()
