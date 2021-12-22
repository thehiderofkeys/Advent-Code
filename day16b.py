def ingest() -> list[int]:
    line = input()
    str_template = '0{}b'.format(len(line)*4)
    bits_str = format(int(line, 16), str_template)
    return [int(digit) for digit in bits_str]


def main(bits_list: list[int]):
    result = packet(bits_list)
    print(result)


def get_n(bits_list: list[int], n: int) -> str:
    output = "".join(str(i) for i in bits_list[:n])
    del bits_list[:n]
    return output


def packet(bits_list: list[int]) -> int:
    version = int(get_n(bits_list, 3), 2)
    type_id = int(get_n(bits_list, 3), 2)
    #print("Version: {}, Type: {}".format(version, type_id), end="")

    if type_id == 4:
        value = ""
        while True:
            cont = bits_list.pop(0)
            value += get_n(bits_list, 4)
            if not cont:
                break
        value = int(value, 2)
        #print(", Value: {}".format(value))
        return value
    len_type = bits_list.pop(0)
    results = []
    if len_type == 0:
        length = int(get_n(bits_list, 15), 2)
        #print(", Length Type: {}, Length {}".format(len_type, length))
        sublist = bits_list[:length]
        del bits_list[:length]
        while len(sublist) > 0:
            results.append(packet(sublist))
    if len_type == 1:
        length = int(get_n(bits_list, 11), 2)
        #print(", Length Type: {}, Length {}".format(len_type, length))
        for _ in range(length):
            results.append(packet(bits_list))
    if type_id == 0:
        return sum(results)
    if type_id == 1:
        product = 1
        for result in results:
            product *= result
        return product
    if type_id == 2:
        return min(results)
    if type_id == 3:
        return max(results)
    if type_id == 5:
        return int(results[0] > results[1])
    if type_id == 6:
        return int(results[0] < results[1])
    if type_id == 7:
        return int(results[0] == results[1])


if __name__ == "__main__":
    main(ingest())
