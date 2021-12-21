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
    pair_freq = dict()
    freq = Counter(template)
    for first, second in zip(template, template[1:]):
        node = first + second
        pair_freq[node] = 1 if node not in pair_freq else pair_freq[node] + 1

    for _ in range(40):
        next_freq = dict()
        for node in pair_freq:
            n = pair_freq[node]
            char = rules[node]
            freq[char] = n if char not in freq else freq[char] + n
            left, right = tree[node]
            next_freq[left] = n if left not in next_freq else next_freq[left] + n
            next_freq[right] = n if right not in next_freq else next_freq[right] + n
        pair_freq = next_freq
    most_common = max(freq, key=freq.get)
    least_common = min(freq, key=freq.get)
    print("Most common {}, {}".format(most_common, freq[most_common]))
    print("Least common {}, {}".format(least_common, freq[least_common]))


if __name__ == "__main__":
    template, rules, tree = ingest()
    main(template, rules, tree)
