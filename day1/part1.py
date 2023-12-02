def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()

    total = 0
    for line in lines:
        line = line.strip()

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
