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

    return z


def main():
    word = input()
    text = input()
    z = calcZ(word + '$' + text)[len(word) + 1::]
    z_1 = calcZ(word[::-1] + '$' + text[::-1])[len(word) + 1::]
    z_rev = z_1[::-1]

    ans = []
    for i in range(len(z) - len(word) + 1):
        if z[i] + z_rev[i + len(word) - 1] >= len(word) - 1:
            ans.append(i + 1)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
