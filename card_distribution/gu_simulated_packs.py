'''
Part 2: Pack Simulation

This code is used to simulate an unbiased pulling of cards given base rarities:
Legendary = 0.5%
Epic = 4%
Rare = 23%
Common = 72.5%
'''

import random
import matplotlib.pyplot as plt

'''
Here I construct a list of a thousand elements with the distribution equivalent
to the base rarity on the God's Unchained website
'''
pos = ['Legendary'] * 5 + ['Epic'] * 40 + ['Rare'] * 230 + ['Common']*725

simulated_space = []

'''
Here we uniformly pick a sample from the array "pos". I choose 750,000 samples,
since this is approximatley the same amount of cards that were revealed at the
time of project
'''

for i in range(0,750000):
    simulated_space.append(random.choice(pos))

l = 0
e = 0
r = 0
c = 0

'''
Count the amount of each rarity
'''
for pull in simulated_space:
    if pull == 'Legendary':
        l += 1
    elif pull == 'Epic':
        e += 1
    elif pull == 'Rare':
        r += 1
    elif pull == 'Common':
        c += 1

amount = [c,r,e,l]
print(amount[0]/sum(amount),amount[1]/sum(amount),amount[2]/sum(amount),amount[3]/sum(amount))

'''
This section plots the distribution of cards
'''

'''
barlist = plt.bar(['Common', 'Rare', 'Epic', 'Legendary'], amount, align='center', alpha=0.5)
barlist[0].set_color('grey')
barlist[1].set_color('blue')
barlist[2].set_color('purple')
barlist[3].set_color('gold')
plt.ylabel('Amount of Cards Generated')
plt.title('Gods Unchained: Simulated Distribution')
plt.show()
'''
