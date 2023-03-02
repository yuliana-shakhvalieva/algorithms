def push_back(left_stack, x):
    if not left_stack:
        left_stack.append([x, x])
    else:
        prev = len(left_stack) - 1
        left_stack.append([x, min(int(x), left_stack[prev][1])])


def pop_front(left_stack, right_stack):
    if not right_stack:
        x = left_stack.pop()[0]
        right_stack.append([x, x])
        len_left = len(left_stack)
        for i in range(len_left, 0, -1):
            x = left_stack.pop()[0]
            right_stack.append([x, min(x, right_stack[len_left-i][1])])
    right_stack.pop()


def main():
    q = int(input())
    left_stack, right_stack = [], []

    for i in range(q):
        value = input().split()
        if value[0] == '+':
            push_back(left_stack, int(value[1]))
        elif value[0] == '-':
            pop_front(left_stack, right_stack)

        len_left, len_right = len(left_stack), len(right_stack)
        if len_left != 0 and len_right == 0:
            print(left_stack[len_left - 1][1])
        elif len_left == 0 and len_right != 0:
            print(right_stack[len_right - 1][1])
        elif len_left != 0 and len_right != 0:
            print(min(left_stack[len_left - 1][1],
                  right_stack[len_right - 1][1]))
        elif len_left == 0 and len_right == 0:
            print(-1)


if __name__ == "__main__":
    main()
