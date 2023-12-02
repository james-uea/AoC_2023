MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_cube_count(throw):
    # Get the given red green and blue cubes from a throw
    data = {"red": 0, "green": 0, "blue": 0}
    cubes = throw.split(",")
    for cube in cubes:
        for colour in data.keys():
            if colour in cube:
                data[colour] += int(cube.split(colour)[0])
    return data


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    total = 0
    for line in lines:
        line = line.strip().replace(" ", "")
        game_id, content = line.split(":")
        throws = content.split(";")

        min_red = 0
        min_green = 0
        min_blue = 0

        for throw in throws:
            cubes = get_cube_count(throw)
            if cubes["red"] > min_red:
                min_red = cubes["red"]
            if cubes["green"] > min_green:
                min_green = cubes["green"]
            if cubes["blue"] > min_blue:
                min_blue = cubes["blue"]

        print(min_red, min_green, min_blue)
        total += min_red * min_green * min_blue

    print(total)


if __name__ == "__main__":
    main()
