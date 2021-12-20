def main():
    tally = 0
    while True:
        code = input()
        if not code:
            break
        output_digits = code.split("|")[1].split()
        for digit in output_digits:
            if len(digit) in [2, 3, 4, 7]:
                tally += 1

    print(tally)

if __name__ == "__main__":
    main()