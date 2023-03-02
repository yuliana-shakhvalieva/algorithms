def main():
    n = int(input())
    gnomes_a = list(map(float, input().split()))
    gnomes_b = list(map(float, input().split()))
    gnomes = [[gnomes_a[i], gnomes_b[i]] for i in range(n)]

    for i in range(n):
        gnomes[i].append(i+1)
    gnomes.sort(reverse=True, key=lambda x: x[0] + x[1])

    sleep = gnomes[0][0] + gnomes[0][1]
    curr = gnomes[0][0]
    for i in range(1, len(gnomes)):
        if curr + gnomes[i][0] + gnomes[i][1] <= sleep:
            sleep = curr + gnomes[i][0] + gnomes[i][1]
        curr += gnomes[i][0]

    if sleep > curr:
        print(' '.join(str(gnomes[i][2]) for i in range(len(gnomes))))
    else:
        print('-1')


if __name__ == "__main__":
    main()
