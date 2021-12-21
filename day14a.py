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
    for _ in range(10):
        i = 0
        while i < len(template) - 1:
            pair = "".join(template[i:i+2])
            if pair in rules:
                template.insert(i + 1, rules[pair])
                i += 1
            i += 1
    freq = Counter(template)
    most_common = max(freq, key=freq.get)
    least_common = min(freq, key=freq.get)
    print("Most common {}, {}".format(most_common, freq[most_common]))
    print("Least common {}, {}".format(least_common, freq[least_common]))


if __name__ == "__main__":
    template, rules = ingest()
    main(template, rules)
