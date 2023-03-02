operation = {
    '+': lambda b, a: a + b,
    '-': lambda b, a: a - b,
    '*': lambda b, a: a * b
}


def main():
    list_input = list(map(str, input().split()))
    stack = []
    for value in list_input:
        try:
            stack.append(int(value))
        except ValueError:
            stack.append(operation.get(value)(stack.pop(), stack.pop()))
    print(stack[0])


if __name__ == "__main__":
    main()
