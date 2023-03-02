def find_minimum(n, matrix, L):
    size = n - L + 1
    for i in range(n):
        for j in range(size):
            matrix[i][j] = min(matrix[i][j:j+L])

    for j in range(n):
        for i in range(size):
            min_clmn = matrix[i][j]
            for k in range(i + 1, i + L):
                min_clmn = min(min_clmn, matrix[k][j])
            matrix[i][j] = min_clmn

    return [matrix[i][0:size] for i in range(size)]


def main():
    n, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = find_minimum(n, matrix, L)

    for i in range(len(ans)):
        for j in range(len(ans[0])):
            print(ans[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
