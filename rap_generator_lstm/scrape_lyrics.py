import requests
from bs4 import BeautifulSoup
import re
import operator

from keras.preprocessing.text import Tokenizer

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

astro_urls = ["https://www.letssingit.com/travis-scott-lyrics-stargazing-58n9ght",
    "https://www.letssingit.com/travis-scott-lyrics-carousel-j64h43v",
    "https://www.letssingit.com/travis-scott-feat.-drake-lyrics-sicko-mode-nmkdl3r",
    "https://www.letssingit.com/travis-scott-lyrics-r.i.p.-screw-j5dpw9t",
    "https://www.letssingit.com/travis-scott-lyrics-stop-trying-to-be-god-dhjtnr4",
    "https://www.letssingit.com/travis-scott-lyrics-no-bystanders-rpdq45w",
    "https://www.letssingit.com/travis-scott-lyrics-skeletons-tztqhfw",
    "https://www.letssingit.com/travis-scott-feat.-the-weeknd-lyrics-wake-up-2dqcwsn",
    "https://www.letssingit.com/travis-scott-lyrics-5%25-tint-zt32q37",
    "https://www.letssingit.com/travis-scott-lyrics-nc-17-clhrtx4",
    "https://www.letssingit.com/travis-scott-lyrics-astrothunder-qjvqdws",
    "https://www.letssingit.com/travis-scott-lyrics-yosemite-plftzbs",
    "https://www.letssingit.com/travis-scott-lyrics-can-t-say-xfn84bp",
    "https://www.letssingit.com/travis-scott-lyrics-who-what-85j74fs",
    "https://www.letssingit.com/travis-scott-lyrics-butterfly-effect-cfhkw16",
    "https://www.letssingit.com/travis-scott-lyrics-houstonfornication-32rc1sf",
    "https://www.letssingit.com/travis-scott-lyrics-coffee-bean-7sxhckv"]


birds_urls = ["https://www.letssingit.com/travis-scott-feat.-andr%C3%A9-3000-lyrics-the-ends-fnw6k2t",
            "https://www.letssingit.com/travis-scott-lyrics-way-back-3rlm11f",
            "https://www.letssingit.com/travis-scott-lyrics-coordinate-9xsd1jl",
            "https://www.letssingit.com/travis-scott-lyrics-through-the-late-night-63l2nk3",
            "https://www.letssingit.com/travis-scott-lyrics-beibs-in-the-trap-3qnnw39",
            "https://www.letssingit.com/travis-scott-lyrics-sdp-interlude-gmfjjx5",
            "https://www.letssingit.com/travis-scott-lyrics-sweet-sweet-83d5pwq",
            "https://www.letssingit.com/travis-scott-lyrics-outside-ds2msgn",
            "https://www.letssingit.com/travis-scott-feat.-kendrick-lamar-lyrics-goosebumps-nms576m",
            "https://www.letssingit.com/travis-scott-lyrics-first-take-n7lzf4k",
            "https://www.letssingit.com/young-thug-and-travis-scott-feat.-quavo-lyrics-pick-up-the-phone-wt6lz3l",
            "https://www.letssingit.com/travis-scott-lyrics-lose-3hnlxsm",
            "https://www.letssingit.com/travis-scott-lyrics-guidance-shw9xzd",
            "https://www.letssingit.com/travis-scott-feat.-the-weeknd-lyrics-wonderful-p24czz1"]

rodeo_urls = ["https://www.letssingit.com/travis-scott-lyrics-pornography-s7bq9pg",
            "https://www.letssingit.com/travis-scott-feat.-quavo-lyrics-oh-my-dis-side-6bklb5w",
            "https://www.letssingit.com/travis-scott-feat.-2-chainz-and-future-lyrics-3500-dc48ckt",
            "https://www.letssingit.com/travis-scott-feat.-juicy-j-lyrics-wasted-kc4szqs",
            "https://www.letssingit.com/travis-scott-lyrics-90210-kr554fw",
            "https://www.letssingit.com/travis-scott-feat.-the-weeknd-lyrics-pray-4-love-nd26c1j",
            "https://www.letssingit.com/travis-scott-feat.-chief-keef-and-swae-lee-lyrics-night-call-5hbmb14",
            "https://www.letssingit.com/travis-scott-feat.-kanye-west-lyrics-piss-on-your-grave-7v65m1k",
            "https://www.letssingit.com/travis-scott-lyrics-antidote-lh1wqq4",
            "https://www.letssingit.com/travis-scott-lyrics-impossible-vx2zssj",
            "https://www.letssingit.com/travis-scott-feat.-justin-bieber-and-young-thug-lyrics-maria-i-m-drunk-bm5qj2d",
            "https://www.letssingit.com/travis-scott-feat.-toro-y-moi-lyrics-flying-high-s6q8mbb",
            "https://www.letssingit.com/travis-scott-lyrics-i-can-tell-vdchrdf",
            "https://www.letssingit.com/travis-scott-lyrics-apple-pie-h8j6r7p",
            "https://www.letssingit.com/travis-scott-feat.-schoolboy-q-lyrics-ok-alright-l1cvn39",
            "https://www.letssingit.com/travis-scott-lyrics-never-catch-me-drkb3vp"]


urls = []
urls.extend(astro_urls)
urls.extend(birds_urls)
urls.extend(rodeo_urls)

def clean_text(text):
        clean = re.sub(r"[\[].*?[\]]", "", text)
        clean = clean.replace('\n',' ')
        clean = re.sub('[(,!?){}<>]', '', clean)
        return(clean.lower())

def lyrics_string(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, features="html5lib")
    div = soup.find('div', {'id':'lyrics'})
    list_lyrics = div.text.split("\n")
    cleaned_lyrics = []
    for item in list_lyrics:
        cleaned_lyrics.append(clean_text(item))
    return(list(filter(None, cleaned_lyrics)))


lyrics_list = []
for url in urls:
        lyrics_list.extend(lyrics_string(url))

with open('lyrics.txt', 'w') as file_handler:
    for item in lyrics_list:
        file_handler.write("{}\n".format(item))
