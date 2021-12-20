def main():
    last = int(input())
    sum = 0
    try:
        while(True):
            curr = int(input())
            if (curr > last):
                sum += 1
            last = curr
    except ValueError:
        print(sum)


if __name__ == "__main__":
    main()
