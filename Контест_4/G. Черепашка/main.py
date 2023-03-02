def main():
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if i - 1 == -1:
                ans[i][j] = ans[i][j - 1] + matrix[i][j]
            elif j - 1 == -1:
                ans[i][j] = ans[i - 1][j] + matrix[i][j]
            else:
                ans[i][j] = min(ans[i - 1][j], ans[i][j - 1]) + matrix[i][j]

    print(ans[n-1][m-1])


if __name__ == "__main__":
    main()
