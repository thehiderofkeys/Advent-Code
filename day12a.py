def ingest() -> dict:
    line = input()
    tree = {}
    while line:
        a,b = line.split("-")
        if a != "end" and b != "start":
            if a not in tree:
                tree[a] = []
            tree[a].append(b)
        if a != "start" and b != "end": 
            if b not in tree:
                tree[b] = []
            tree[b].append(a)
        line = input()
    return tree

def recur_dfs(cur_node:str, cur_path:list[str], tree:dict, output:list[int]):
    if cur_node.islower() and cur_node in cur_path:
        return
    if cur_node == "end":
        output[0] += 1
        return
    for next_node in tree[cur_node]:
        recur_dfs(next_node, cur_path + [cur_node], tree, output)

def main(tree:dict):
    output = [0]
    recur_dfs("start", [], tree, output)
    print(output[0])

if __name__ == "__main__":
    main(ingest())