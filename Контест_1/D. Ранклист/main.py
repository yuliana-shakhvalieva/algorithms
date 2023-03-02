def main():
    n, k = map(int, input().split())
    result_list = [list(map(int, input().split())) for _ in range(n)]
    result_list.sort(reverse=True, key=lambda x: (x[0], -x[1]))
    print(result_list.count(result_list[k-1]))


if __name__ == "__main__":
    main()
