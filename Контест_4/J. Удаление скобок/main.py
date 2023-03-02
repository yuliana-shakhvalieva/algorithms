s = input()
n = len(s)
dp = [[0 for _ in range(n)] for _ in range(n)]
pos = [[0 for _ in range(n)] for _ in range(n)]
res = ''


def ans(left, right):
    global s, res, pos, dp

    if dp[left][right] == right - left + 1:
        return

    if dp[left][right] == 0:
        res += s[left:right + 1]
        return

    if pos[left][right] == -10:
        res += s[left]
        ans(left + 1, right - 1)
        res += s[right]
        return

    ans(left, pos[left][right])
    ans(pos[left][right] + 1, right)


def main():
    if n <= 0:
        print('')
        return

    for i in range(n):
        for j in range(n):
            if i > j:
                dp[i][j] = 0
                continue
            if i == j:
                dp[i][j] = 1

    for right in range(n):
        for left in range(right, -1, -1):
            if left == right:
                dp[left][right] = 1
            else:
                min = 100000
                mink = -10
                if s[left] == '(' and s[right] == ')' or s[left] == '[' and s[right] == ']' or s[left] == '{' and s[
                    right] == '}':
                    min = dp[left + 1][right - 1]
                for k in range(left, right):
                    if dp[left][k] + dp[k + 1][right] < min:
                        min = dp[left][k] + dp[k + 1][right]
                        mink = k
                dp[left][right] = min
                pos[left][right] = mink

    ans(0, n - 1)
    print(len(res))


if __name__ == '__main__':
    main()
