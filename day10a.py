def main():
    line = input()
    syntax_stack = []
    closing = { "(":")", "[":"]", "{":"}", "<":">" }
    penalty = { ")":3, "]":57, "}":1197, ">":25137 }
    score = 0
    while line:
        corrupted = False
        for char in line:
            if char in ["(","[","{","<"]:
                syntax_stack.append(char)
            else:
                expect = closing[syntax_stack.pop()]
                if char != expect and not corrupted:
                    print("Expected {}, but found {} instead".format(expect, char))
                    corrupted = True
                    score += penalty[char]
        line = input()
    print(score)
    


if __name__ == "__main__":
    main()