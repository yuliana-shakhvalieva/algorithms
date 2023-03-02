def main():
    n, w = map(int, input().split())
    v_array = list(map(int, input().split()))
    v_array.sort(reverse=True)
    sum_array = []
    for v in v_array:
        while v <= w:
            w -= v
            sum_array.append(v)

    print(len(sum_array))
    print(' '.join(str(x) for x in sum_array))


if __name__ == "__main__":
    main()
