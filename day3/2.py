f = open("input.txt", "r")
lines = f.read().split("\n")
f.close()

total = 0
for i, row in enumerate(lines):
    for j, col in enumerate(row):
        if col == "*":
            known_positions = []
            numbers = []
            for r in [i - 1, i, i + 1]:
                for c in [j - 1, j, j + 1]:
                    if r < 0 or r > len(lines) or c < 0 or c > len(row):
                        continue

                    char = lines[r][c]

                    if char.isdigit():
                        found = False
                        tc = c
                        while tc > 0 and not found:
                            tc -= 1
                            if not lines[r][tc].isdigit():
                                found = True
                                tc += 1

                        if (found or tc == 0) and (r, tc) not in known_positions:
                            known_positions.append((r, tc))
                            number = ""
                            while tc < len(row) and lines[r][tc].isdigit():
                                if lines[r][tc].isdigit():
                                    number += str(lines[r][tc])
                                tc += 1
                            numbers.append(number)

            if len(numbers) > 1:
                total += int(numbers[0]) * int(numbers[1])
print("Total:", total)
