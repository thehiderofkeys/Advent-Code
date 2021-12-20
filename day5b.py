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
        xs = list(max(range(line[0], line[2], + 1), range(line[0], line[2], -1), key=len)) + [line[2]]
        ys = list(max(range(line[1], line[3], + 1), range(line[1], line[3], -1), key=len)) + [line[3]]
        if len(xs) == 1:
            xs = xs * len(ys)
        if len(ys) == 1:
            ys = ys * len(xs)
        for x, y in zip(xs,ys):
            check_coord(x, y)
    print(vents['intersections'])
    for y in range(10):
        line = ''
        for x in range(10):
            key = "{},{}".format(x, y)
            line += str(vents[key]) if key in vents else '.'
        print(line)
            

if __name__ == "__main__":
    input_values = ingest()
    main(input_values)