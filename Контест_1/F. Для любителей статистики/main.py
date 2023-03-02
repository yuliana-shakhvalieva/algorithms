def main():
    n = int(input())
    count_people = list(map(int, input().split()))
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    pair_arr = []
    for i in range(n):
        pair_arr.append([count_people[i], i + 1])
    pair_arr.sort()

    ans = []
    for query in queries:
        l = -1
        r = n
        while l + 1 != r:
            m = (l+r)//2
            if pair_arr[m][0] == query[2] and query[0] <= pair_arr[m][1] <= query[1]:
                ans.append(1)
                break
            elif pair_arr[m][0] > query[2] or pair_arr[m][0] == query[2] and pair_arr[m][1] > query[1]:
                r = m
            else:
                l = m
        else:
            ans.append(0)

    print(''.join(str(x) for x in ans))


if __name__ == "__main__":
    main()

