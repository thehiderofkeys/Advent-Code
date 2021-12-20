import statistics

def main():
    line = input()
    closing = { "(":")", "[":"]", "{":"}", "<":">" }
    penalty = { ")":1, "]":2, "}":3, ">":4 }
    score = []
    while line:
        line_score = 0
        syntax_stack = []
        corrupted = False
        for char in line:
            if char in ["(","[","{","<"]:
                syntax_stack.append(closing[char])
            else:
                if char != syntax_stack.pop() and not corrupted:
                    corrupted = True
        if not corrupted:
            for char in reversed(syntax_stack):
                line_score *= 5
                line_score += penalty[char]
            score.append(line_score)
        line = input()
    print(statistics.median(score))
    


if __name__ == "__main__":
    main()