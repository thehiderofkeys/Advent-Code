def ingest() -> list[int]:
    line = input()
    str_template = '0{}b'.format(len(line)*4)
    bits_str = format(int(line, 16), str_template)
    return [int(digit) for digit in bits_str]


def main(bits_list: list[int]):
    versions = []
    packet(bits_list, versions)
    print(sum(versions))


def get_n(bits_list: list[int], n: int) -> str:
    output = "".join(str(i) for i in bits_list[:n])
    del bits_list[:n]
    return output


def packet(bits_list: list[int], versions):
    version = int(get_n(bits_list, 3), 2)
    type_id = int(get_n(bits_list, 3), 2)
    versions.append(version)
    #print("Version: {}, Type: {}".format(version, type_id), end="")

    if type_id == 4:
        value = ""
        while True:
            cont = bits_list.pop(0)
            value += get_n(bits_list, 4)
            if not cont:
                break
        #print(", Value: {}".format(int(value, 2)))
        return
    len_type = bits_list.pop(0)
    if len_type == 0:
        length = int(get_n(bits_list, 15), 2)
        #print(", Length Type: {}, Length {}".format(len_type, length))
        sublist = bits_list[:length]
        del bits_list[:length]
        while len(sublist) > 0:
            packet(sublist, versions)
    if len_type == 1:
        length = int(get_n(bits_list, 11), 2)
        #print(", Length Type: {}, Length {}".format(len_type, length))
        for _ in range(length):
            packet(bits_list, versions)


if __name__ == "__main__":
    main(ingest())
