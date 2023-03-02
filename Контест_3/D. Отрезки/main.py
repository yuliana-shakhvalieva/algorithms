def main():
    n = int(input())
    segments = [list(map(int, input().split())) for _ in range(n)]
    segments.sort(key=lambda x: (x[1], x[0]))
    count = 1
    k = 0
    for i in range(1, n):
        if segments[k][1] <= segments[i][0]:
            count += 1
            k = i
    print(count)


if __name__ == "__main__":
    main()
