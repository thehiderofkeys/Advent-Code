def ingest() -> list[(str,int)]: 
    output = []
    try:
        while True:
            pair = input().split(' ')
            direction = pair[0]
            magnitude = int(pair[1])
            output.append((direction, magnitude))
    except IndexError:
        return output

def main(input_array:list[(str,int)]):
    depth = 0
    distance = 0
    aim = 0
    for direction, magnitude in input_array:
        if direction == "forward":
            distance += magnitude
            depth += aim * magnitude
        if direction == "down":
            aim += magnitude
        if direction == "up":
            aim -= magnitude
    print("depth: {}".format(depth))
    print("distance: {}".format(distance))
    print(depth * distance)

if __name__ == "__main__":
    input_values = ingest()
    main(input_values)