#prints the ten most common unique words from a text file.

from collections import Counter
from pathlib import Path

# filename = Path('resources/pru.txt').read_text()
# print(filename) 

filename = 'resources/pru.txt'
def count_unique_words(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = text.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(10)
        for word, count in most_common:
            print(f"{word}: {count}")

count_unique_words(filename)    

## Nobel prize 
def load_nobel_prizes(filename='resources/prize.json') -> dict:
    try:
        import json
        with open(filename, 'r') as file:
            data = json.load(file)

            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")

    return {}

#define a class to represent Nobel Prize data 
class NobelPrize:
    def __init__(self, year: str, category: str, laureates: list[dict]):
        self.year = year
        self.category = category
        self.laureates = laureates  

def filter_nobel_prizes(nobel_data: dict, **argv) -> list[dict]:
    year = argv.get('year', None)
    category = argv.get('category', None)
    filteredPrizes = [ i for i in nobel_data["prizes"] \
                      if ((i["year"] == year or year == None) and \
                          (i["category"] == category or category == None)) ]
    return filteredPrizes

def filter_nobel_prizesObjects(nobel_data: dict, **argv) -> list[NobelPrize]:
    year = argv.get('year', None)
    category = argv.get('category', None)
    filteredPrizes = [ i for i in nobel_data["prizes"] \
                      if ((i["year"] == year or year == None) and \
                          (i["category"] == category or category == None)) ]
    return [ NobelPrize(i["year"], i["category"], i["laureates"]) for i in filteredPrizes  ]

import json

nobel_prizes = load_nobel_prizes()
print(type(nobel_prizes))
# nobel_prizes = filter_nobel_prizes(nobel_prizes,category="literature")
# print(json.dumps(nobel_prizes, indent=2)) 
nobel_prizes = filter_nobel_prizesObjects(nobel_prizes,year="2020")
print(type(nobel_prizes[0]))
for i in nobel_prizes:
    print(f"{i.year} - {i.category} ")  
    for j in i.laureates:
        print(f"   {j['id']} - {j['firstname']} {j.get('surname',' - ')}")     
