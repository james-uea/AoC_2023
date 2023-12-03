check_pos = [
    [0, 1],
    [0, -1],
    [1, 0],
    [1, -1],
    [1, 1],
    [-1, 0],
    [-1, 1],
    [-1, -1],
]


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    plot2d = []

    for line in lines:
        line = line.strip()
        plot = []
        for char in line:
            plot.append(char)
        plot2d.append(plot)

    numbers = []
    r = 0

    for row in plot2d:
        c = 0
        verified = False
        number = ""
        for col in row:
            if col.isdigit():
                number += str(col)
                for pos in check_pos:
                    nr = pos[0]
                    nc = pos[1]
                    check_row = r + nr
                    check_col = c + nc
                    if (
                        check_row != -1
                        and check_col != -1
                        and check_row < len(plot2d)
                        and check_col < len(row)
                    ):
                        check = plot2d[check_row][check_col]
                        if not check.isdigit() and check != ".":
                            verified = True
            else:
                if number != "":
                    if verified:
                        numbers.append(number)
                        verified = False
                    number = ""
            c += 1
        r += 1
        if number != "":
            if verified:
                numbers.append(number)
            number = ""

    total = 0
    print(numbers)
    for number in numbers:
        total += int(number)
    print(total)


if __name__ == "__main__":
    main()
