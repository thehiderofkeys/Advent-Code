from typing import Counter


def ingest() -> tuple[list, dict]:
    template = list(input())
    input()
    rules, tree = dict(), dict()
    line = input()
    while line:
        match, insert = line.split(" -> ")
        rules[match] = insert
        tree[match] = (match[0] + insert, insert + match[1])
        line = input()
    return template, rules, tree


def main(template: list, rules: dict, tree: dict):
    freq = Counter(template)
    for first, second in zip(template, template[1:]):
        iter_freq(first + second, rules, tree, freq)
    print(freq)
    most_common = max(freq, key=freq.get)
    least_common = min(freq, key=freq.get)
    print("Most common {}, {}".format(most_common, freq[most_common]))
    print("Least common {}, {}".format(least_common, freq[least_common]))


def iter_freq(node: str, rules: dict, tree: dict, freq: dict, depth: int = 10):
    new_char = rules[node]
    if new_char not in freq:
        freq[new_char] = 0
    freq[new_char] += 1
    depth -= 1
    if depth > 0:
        left, right = tree[node]
        iter_freq(left, rules, tree, freq, depth)
        iter_freq(right, rules, tree, freq, depth)


if __name__ == "__main__":
    template, rules, tree = ingest()
    main(template, rules, tree)
