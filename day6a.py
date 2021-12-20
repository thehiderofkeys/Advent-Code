def ingest() -> list[int]: 
    output = [int(number) for number in input().split(',')]
    return output

def main(fishes:list[int]):
    for _ in range(80):
        new_fish = fishes.count(0)
        fishes = [6 if fish == 0 else fish -1 for fish in fishes]
        fishes += [8] * new_fish   
    print(len(fishes))

if __name__ == "__main__":
    input_values = ingest()
    main(input_values)