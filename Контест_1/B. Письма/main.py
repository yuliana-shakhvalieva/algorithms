def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    k, l = 0, 0
    for i in range(n):
        for j in range(l, m):
            if b[j] - k <= a[i]:
                l += 1
                print(i + 1, b[j] - k)
            else:
                k += a[i]
                break


if __name__ == "__main__":
    main()
