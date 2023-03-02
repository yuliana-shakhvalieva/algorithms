def main():
    m = int(input())
    l = r = None
    segments = []
    while l != 0 or r != 0:
        l, r = map(int, input().split())
        if m > l != r > 0:
            segments.append([l, r, l])
    if len(segments) == 0:
        print('No solution')
        exit(0)
    segments.sort(key=lambda x: (x[0], -x[1]))

    ans_stack = []
    for i in range(0, len(segments)):
        curr_segment = segments[i]

        while len(ans_stack) > 0:
            if (curr_segment[0] <= ans_stack[-1][2] or curr_segment[0] <= 0) and curr_segment[1] > ans_stack[-1][1]:
                ans_stack.pop()
            elif curr_segment[0] <= ans_stack[-1][1] < curr_segment[1]:
                curr_segment[2] = ans_stack[-1][1]
                ans_stack.append(curr_segment)
                break
            elif curr_segment[1] <= ans_stack[-1][1]:
                break
            else:
                print('No solution')
                exit(0)
        else:
            if curr_segment[0] <= 0:
                ans_stack.append(curr_segment)
            else:
                print('No solution')
                exit(0)
        if ans_stack[-1][1] >= m:
            break

    if ans_stack[-1][1] < m:
        print('No solution')
    else:
        print(len(ans_stack))
        for segment in ans_stack:
            print(segment[0], segment[1])


if __name__ == '__main__':
    main()
