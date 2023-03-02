def check(m, start_len, N, K):
    ans = 0
    for i in range(N):
        ans += start_len[i] // m
    if ans >= K:
        return True
    else:
        return False


def main():
    N, K = map(int, input().split())
    start_len = [int(input()) for _ in range(N)]

    l = 1
    r = 10000001
    while l + 1 < r:
        m = int((l + r) / 2)
        if check(m, start_len, N, K):
            l = m
        else:
            r = m
    if sum(start_len) >= l*K:
        print(int(l))
    else:
        print(0)


if __name__ == "__main__":
    main()
