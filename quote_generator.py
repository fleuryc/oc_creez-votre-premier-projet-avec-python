import random
import json


def read_values_from_json(file):
    # load data
    with open(file) as f:
        return json.load(f)


characters = read_values_from_json('data/characters.json')
quotes = read_values_from_json('data/quotes.json')


def get_random_item(list):
    # pick a random item from list
    return list[random.randint(0, len(list)-1)]


while input("Type 'Enter' for a new quote, or 'B' to quit.\n") != "B":
    print(
        '{character} says : "{quote}"\n'.format(
            character=get_random_item(characters).capitalize(),
            quote=get_random_item(quotes)))

print("Bye !")
