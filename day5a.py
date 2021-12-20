def ingest() -> list[list[int]]: 
    output = []
    while True:
        line_str = input()
        if not line_str:
            break
        coords = line_str.replace('->', ',').split(',')
        line = [int(coord) for coord in coords]
        output.append(line)
    return output

def main(input_array:list[list[int]]):
    vents = {'intersections':0}
    def check_coord(x, y):
        key = "{},{}".format(x, y)
        if key in vents:
            if vents[key] == 1:
                vents['intersections'] += 1
            vents[key] += 1
        else:
            vents[key] = 1
    for line in input_array:
        if line[0] == line[2]:
            x = line[0]
            for y in range(min(line[1], line[3]), max(line[1], line[3]) + 1):
                check_coord(x, y)
        if line[1] == line[3]:
            y = line[1]
            for x in range(min(line[0], line[2]), max(line[0], line[2]) + 1):
                check_coord(x, y)
    print(vents['intersections'])

if __name__ == "__main__":
    input_values = ingest()
    main(input_values)