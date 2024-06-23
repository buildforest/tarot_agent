import random
import pandas as pd

data = pd.read_json('static/tarot-images.json', orient='records')
cards = pd.json_normalize(data['cards'])

cards['img_file'] = cards.apply(lambda row: row['img'][0] + str(row['img'][1:]), axis=1)

def draw_cards():
    selected_cards = cards.sample(3)
    return selected_cards
