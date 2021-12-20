import statistics
def ingest() -> list[int]: 
    output = [int(number) for number in input().split(',')]
    return output

def main(crabs:list[int]):
    middle = int(statistics.median(crabs))
    fuel = sum([abs(pos - middle) for pos in crabs])
    print(middle)
    print(fuel)


if __name__ == "__main__":
    input_values = ingest()
    main(input_values)