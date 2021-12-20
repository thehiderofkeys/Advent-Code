import statistics
def ingest() -> list[int]: 
    output = [int(number) for number in input().split(',')]
    return output

def main(crabs:list[int]):
    mean  = statistics.mean(crabs)
    min_fuel = None
    ideal_pos = None
    for i in range(int(mean) - 1 , int(mean) + 2):
        fuel = sum([pow(pos - i, 2) + abs(pos - i) for pos in crabs]) /2
        if min_fuel is None or fuel < min_fuel:
            min_fuel = fuel
            ideal_pos = i
    print(ideal_pos)
    print(min_fuel)


if __name__ == "__main__":
    input_values = ingest()
    main(input_values)