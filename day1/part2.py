import re

conversions = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# def replace_words(line):
#     # Very scuffy implementation to prevent "eightwo" from becoming "eigh2" and so on...
#     temp_line = ""
#     did_swap = True

#     while did_swap:
#         did_swap = False
#         redo = False

#         for i in range(len(line)):
#             char = line[i]
#             temp_line += char
#             for word in conversions.keys():
#                 if word in temp_line:
#                     temp_line = temp_line.replace(word, str(conversions[word]))
#                     line = temp_line + line[i + 1 :]
#                     temp_line = ""
#                     did_swap = True
#                     redo = True
#             if redo:
#                 break

#     return line


def replace_words(line):
    occurrences = re.findall(
        r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line
    )

    for i in range(len(occurrences)):
        entry = occurrences[i]
        if entry in conversions:
            occurrences[i] = str(conversions[entry])

    line = "".join(occurrences)
    return line


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    total = 0
    for line in lines:
        line = line.strip()

        line = replace_words(line)

        first = -1
        last = -1
        for char in line:
            if char.isdigit():
                if first == -1:
                    first = char
                last = char
        print(first + last, line)
        total += int(first + last)
    print(total)


if __name__ == "__main__":
    main()
