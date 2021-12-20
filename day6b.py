def ingest() -> list[int]:
    fish_per_weekday = [0 for _ in range(7)]
    for day in input().split(','):
        fish_per_weekday[int(day)] += 1
    return fish_per_weekday


def main(fish_per_weekday: list[int]):
    nursery = [0 for _ in range(7)]
    for day in range(256):
        nursery[(day + 2) % 7] = fish_per_weekday[day % 7]
        fish_per_weekday[day % 7] += nursery[day % 7]
        nursery[day % 7] = 0
    print(sum(fish_per_weekday) + sum(nursery))


if __name__ == "__main__":
    input_values = ingest()
    main(input_values)
