import pandas as pd
import random 
import os

random.seed(42)

silhouettes = [
    "A-line","Ball Gown","Mermaid","Sheath",
    "Fit and Flare","Empire","Shift","Fitted"
]

fabrics = [
    "Chiffon","Satin","Lace","Velvet",
    "Jersey","Tulle","Organza","Crepe"
]

necklines = [
    "V-neck", "Sweetheart", "Square",
    "Off-shoulder", "One-shoulder",
    "Illusion", "Halter", "Boat", "Strapless"
]

sleeves = [
    "Sleeveless", "Long Sleeves", "Short Sleeves",
    "Cap Sleeves", "Puff Sleeves", "Three-quarter Sleeves"
]

lengths = [
    "Mini", "Knee", "Midi", "Floor", "Tea"
]

embellishments = [
    "Sequin", "Beaded", "Embroidery",
    "Pleated", "Ruffles", "Feather Trim",
    "Ruched", "No Embellishment"
]

colors = [
    "Black", "White", "Red", "Blue",
    "Navy", "Sage", "Dusty Blue",
    "Emerald", "Pink", "Royal Blue"
]

categories = [
    "Wedding", "Bridesmaid", "Prom",
    "Evening", "Cocktail", "Formal", "Party"
]

templates = [
    "{length} length {fabric} {category} dress with {embellishment} details, {neckline} neckline and {sleeve} featuring a {silhouette} silhouette in {color}.", 

    "{fabric} {category} gown in {color}with{neckline} neckline,{sleeve},{embellishment} accents and {length} length {silhouette} design.",

    "{color} {fabric} {category} dress featuring a {silhouette} silhouette,{neckline} neckline,sleeve, and {embellishment} work with {length} length.",

    "{silhouette} {category} dress crafted from {fabric} with {neckline} neckline,{sleeve},{embellishment}embellishment and {color}color."

]

rows = []

for _ in range(500):
    silhouette = random.choice(silhouettes)
    fabric = random.choice(fabrics)
    neckline = random.choice(necklines)
    sleeve = random.choice(sleeves)
    length = random.choice(lengths)
    embellishment = random.choice(embellishments)
    color = random.choice(colors)
    category = random.choice(categories)

    description = random.choice(templates).format(
        silhouette = silhouette,
        fabric=fabric,
        neckline=neckline,
        sleeve=sleeve,
        length=length,
        embellishment=embellishment,
        color=color,
        category=category
    )

    rows.append({
        "description": description,
        "silhouette": silhouette,
        "fabric": fabric,
        "neckline":neckline,
        "sleeve":sleeve,
        "length":length,
        "embellishment":embellishment,
        "color":color,
        "category":category
        }
    )

df = pd.DataFrame(rows)
os.makedirs("dataset",exist_ok=True)
df.to_csv("dataset/train.csv",index=False)

print(df.head())
print(f"\nDataset created with {len(df)} samples")