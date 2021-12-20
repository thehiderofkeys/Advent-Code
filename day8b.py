def main():
    tally = 0
    while True:
        code = input()
        if not code:
            break
        input_digits = code.split("|")[0].split()
        decoder = get_encoding(input_digits)
        output_digits = code.split("|")[1].split()
        output = int(''.join([str(decoder[''.join(sorted(digit))]) for digit in output_digits]))
        print(output)
        tally += output

    print(tally)

def get_encoding(input_digits: list[str]) -> dict:
    string_to_num = {}
    num_to_set = {}
    for digit in input_digits:
        if len(digit) == 2:
            string_to_num[''.join(sorted(digit))] = 1
            num_to_set[1] = set(digit)
            continue
        if len(digit) == 3:
            string_to_num[''.join(sorted(digit))] = 7
            num_to_set[7] = set(digit)
            continue
        if len(digit) == 4:
            string_to_num[''.join(sorted(digit))] = 4
            num_to_set[4] = set(digit)
            continue
        if len(digit) == 7:
            string_to_num[''.join(sorted(digit))] = 8
            num_to_set[8] = set(digit)
            continue
    for digit in input_digits:
        if len(digit) == 5:
            digit_set = set(digit)
            num = 0
            if len(digit_set.intersection(num_to_set[1])) == 2:
                num = 3
            elif len(digit_set.intersection(num_to_set[4])) == 2:
                num = 2
            else:
                num = 5
            string_to_num[''.join(sorted(digit))] = num
            num_to_set[num] = digit
            continue
        if len(digit) == 6:
            digit_set = set(digit)
            num = 0
            if len(digit_set.intersection(num_to_set[1])) == 1:
                num = 6
            elif len(digit_set.intersection(num_to_set[4])) == 4:
                num = 9
            else:
                num = 0
            string_to_num[''.join(sorted(digit))] = num
            num_to_set[num] = digit
            continue
    return string_to_num

    

    
            
if __name__ == "__main__":
    main()