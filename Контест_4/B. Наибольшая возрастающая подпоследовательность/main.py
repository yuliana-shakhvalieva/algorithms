def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    arr_len = [1] * n
    prev = [-1] * n
    ans = []

    for i in range(n):
        for j in range(i):
            if sequence[j] < sequence[i] and arr_len[j] + 1 > arr_len[i]:
                arr_len[i] = arr_len[j] + 1
                prev[i] = j

    pos = 0
    length = arr_len[0]
    for i in range(n):
        if arr_len[i] > length:
            pos = i
            length = arr_len[i]

    while pos != -1:
        ans.append(sequence[pos])
        pos = prev[pos]

    print(len(ans))
    print(' '.join([str(ans[i]) for i in range(len(ans) - 1, -1, -1)]))


if __name__ == "__main__":
    main()
