def ingest() -> list[int]:
    output = []
    try:
        while(True):
            output.append(int(input()))
    except ValueError:
        return output


def main(input_array: list[int]):
    last = sum(input_array[0:3])
    total = 0
    for i in range(1, len(input_array) - 2):
        curr = sum(input_array[i:i+3])
        if(curr > last):
            total += 1
        last = curr
    print(total)


if __name__ == "__main__":
    input_values = ingest()
    main(input_values)
