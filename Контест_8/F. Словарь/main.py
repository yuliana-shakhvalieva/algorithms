class Node:
    def __init__(self):
        self.term = -1
        self.go = dict()


def add(s, root, idx):
    cur = root
    for c in s:
        if c not in cur.go.keys():
            cur.go[c] = Node()
        cur = cur.go[c]
    cur.term = idx


def main():
    text = input()
    m = int(input())
    words = [input() for _ in range(m)]

    root = Node()
    for idx, word in enumerate(words):
        add(word, root, idx)

    ans = ['No' for _ in range(m)]
    for i in range(len(text)):
        cur = root
        for j in range(i, len(text)):
            letter = text[j]
            if letter not in cur.go.keys():
                break
            cur = cur.go[letter]
            if cur.term != -1:
                ans[cur.term] = 'Yes'

    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
