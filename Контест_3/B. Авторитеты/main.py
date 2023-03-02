import heapq


def main():
    n, a0 = map(int, input().split())
    positives = []
    negatives = []
    for i in range(n):
        a, b = map(int, input().split())
        if b >= 0:
            positives.append((a, b, i + 1))
        else:
            negatives.append((a, b, i + 1))

    positives.sort(key=lambda x: x[0])
    negatives.sort(key=lambda x: x[1], reverse=True)
    negatives.sort(key=lambda x: x[1] + x[0], reverse=True)

    ans = []
    for pos in positives:
        if a0 < pos[0]:
            break
        a0 += pos[1]
        ans.append(pos[2])

    h = []
    i = 0
    while i != len(negatives):
        neg = negatives[i]
        if a0 < neg[0] and len(h) != 0 and neg[1] > h[0][0]:
            old_neg = heapq.heappushpop(h, (neg[1], neg[0], neg[2]))
            a0 -= old_neg[0]
            a0 += neg[1]
            ans.remove(old_neg[2])
            ans.append(neg[2])
            negatives[i] = (old_neg[1], old_neg[0], old_neg[2])
            i -= 1
        elif a0 >= neg[0]:
            a0 += neg[1]
            ans.append(neg[2])
            heapq.heappush(h, (neg[1], neg[0], neg[2]))
        i += 1

    print(len(ans))
    print(' '.join([str(a) for a in ans]))


if __name__ == '__main__':
    main()
