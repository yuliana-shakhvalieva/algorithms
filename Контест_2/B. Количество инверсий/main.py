import itertools


def nextRand24(a, b, m):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield (cur >> 8) % m


def merge(left, right):
    len_left = len(left)
    len_right = len(right)
    result = [0] * (len_left + len_right)
    pA = pB = pC = count = 0

    while pA != len_left and pB != len_right:

        if left[pA] <= right[pB]:
            result[pC] = left[pA]
            pC += 1
            pA += 1
        else:
            result[pC] = right[pB]
            pC += 1
            pB += 1
            count += len_left - pA

    while pA != len_left:
        result[pC] = left[pA]
        pC += 1
        pA += 1

    while pB != len_right:
        result[pC] = right[pB]
        pC += 1
        pB += 1

    return result, count


def merge_sort(array):
    if len(array) == 1:
        return array, 0

    m = len(array) // 2
    result_left, count_left = merge_sort(array[:m])
    result_right, count_right = merge_sort(array[m:])
    result, count_result = merge(result_left, result_right)

    return result, count_left + count_right + count_result


def main():
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    array = list(itertools.islice(nextRand24(a, b, m), n))
    print(merge_sort(array)[1])


if __name__ == "__main__":
    main()
