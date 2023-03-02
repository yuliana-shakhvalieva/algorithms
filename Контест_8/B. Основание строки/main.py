def calcZ(s):
    n = len(s)

    z = [0 for _ in range(n)]
    z[0] = n
    left, right = 0, 0

    for i in range(1, n):
        k = 0
        if i <= right:
            k = min(z[i - left], right - i + 1)
        while i + k != n and s[k] == s[i + k]:
            k += 1
        z[i] = k

        if i + z[i] - 1 > right:
            left = i
            right = i + z[i] - 1

        if z[i] == n - i:
            return i

    return n


def main():
    print(calcZ(input()))


if __name__ == "__main__":
    main()
