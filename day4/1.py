f = open("input.txt", "r")
cards = f.read().split("\n")
f.close()

total = 0
for card in cards:
    card_name, card_data = card.split(":")
    winning_numbers, owned_numbers = card_data.split(" | ")
    winning_numbers = winning_numbers.split()
    owned_numbers = owned_numbers.split()
    i = 0
    for number in owned_numbers:
        if number in winning_numbers:
            if i < 1:
                i = 1
            else:
                i = i * 2
    total += i
    print(card_name, i)
print(f"Total: {total}")
