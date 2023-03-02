import itertools
from random import randint


def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8


def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen)
        d = next(gen)
        yield (c << 8) ^ d


def find_statistic(array, l, r, q):
    if l + 1 >= r:
        return

    p = array[l + randint(0, len(array)) % (r - l)]
    i_1 = i_2 = i_3 = l
    while i_3 < r:
        if array[i_3] < p:
            array[i_3], array[i_2] = array[i_2], array[i_3]
            array[i_2], array[i_1] = array[i_1], array[i_2]
            i_1 += 1
            i_2 += 1
        elif array[i_3] == p:
            array[i_3], array[i_2] = array[i_2], array[i_3]
            i_2 += 1
        i_3 += 1

    if i_1 - l >= q + 1:
        find_statistic(array, l, i_1, q)
    elif i_2 - l >= q + 1:
        return p
    elif i_3 - l >= q + 1:
        find_statistic(array, i_2, r, q - i_2 + l)
    return array[q]


def main():
    n, q = map(int, input().split())
    a, b = map(int, input().split())
    array = list(itertools.islice(nextRand32(a, b), n))
    q -= 1
    print(find_statistic(array, 0, len(array), q))


if __name__ == "__main__":
    main()
