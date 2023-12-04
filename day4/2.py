# This is a very slow method lol, but oh well...

import os

f = open("input.txt", "r")
cards = f.read().split("\n")
f.close()

global total
total = 0


def process_card(id):
    global total

    card = cards[id]
    card_name, card_data = card.split(":")
    try:
        card_id = int(card_name.split("Card")[1].strip(" "))
    except Exception as e:
        print(e, id, card_name)
        os._exit(1)

    winning_numbers, owned_numbers = card_data.split(" | ")
    winning_numbers = winning_numbers.split()
    owned_numbers = owned_numbers.split()

    final_numbers = []
    for number in owned_numbers:
        if number in winning_numbers:
            final_numbers.append(number)

    for i in range(len(final_numbers)):
        new_card = card_id + i
        process_card(new_card)

    total += 1


new_cards = []
for id, card in enumerate(cards):
    process_card(id)

print(f"Total: {total}")
