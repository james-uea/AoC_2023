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


def is_legal(data):
    return (
        data["red"] <= MAX_RED
        and data["green"] <= MAX_GREEN
        and data["blue"] <= MAX_BLUE
    )


def main():
    f = open("input.txt", "r")
    lines = f.readlines()
    f.close()
    total = 0
    for line in lines:
        line = line.strip().replace(" ", "")
        game_id, content = line.split(":")
        throws = content.split(";")
        all_throws_legal = True
        for throw in throws:
            cubes = get_cube_count(throw)
            if not is_legal(cubes):
                all_throws_legal = False
        if all_throws_legal:
            total += int(game_id.split("Game")[1])
    print(total)


if __name__ == "__main__":
    main()
