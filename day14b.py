from typing import Counter


def ingest() -> tuple[list, dict]:
    template = list(input())
    input()
    rules = dict()
    line = input()
    while line:
        match, insert = line.split(" -> ")
        rules[match] = insert
        line = input()
    return template, rules


def main(template: list, rules: dict):
    freq = Counter(template)
    for first, second in zip(template, template[1:]):
        iter_freq(first, second, rules, freq)
    print(freq)
    most_common = max(freq, key=freq.get)
    least_common = min(freq, key=freq.get)
    print("Most common {}, {}".format(most_common, freq[most_common]))
    print("Least common {}, {}".format(least_common, freq[least_common]))


def iter_freq(first: str, second: str, rules: dict, freq: dict, depth: int = 40):
    new_char = rules[first+second]
    if new_char not in freq:
        freq[new_char] = 0
    freq[new_char] += 1
    depth -= 1
    if depth > 0:
        iter_freq(first, new_char, rules, freq, depth)
        iter_freq(new_char, second, rules, freq, depth)


if __name__ == "__main__":
    template, rules = ingest()
    main(template, rules)
