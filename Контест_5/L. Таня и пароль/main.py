from string import ascii_lowercase, ascii_uppercase, digits


def euler(length, n, edges):
    adj = [[] for _ in range(length)]

    deg = [0] * length
    rdeg = [0] * length

    for a, b in edges:
        deg[a] += 1
        rdeg[b] += 1
        adj[a].append(b)

    s = t = u = -1
    for i in range(length):
        if deg[i] == rdeg[i] == 0:
            continue

        df = deg[i] - rdeg[i]

        if not -1 <= df <= 1:
            return None

        if df == 1:
            if s != -1:
                return None
            s = i
        elif df == -1:
            if t != -1:
                return None
            t = i
        else:
            u = i

    v0 = (s if s != -1 else u)

    result = []
    st = [v0]
    *it, = map(iter, adj)
    while st:
        v = st[-1]
        w = next(it[v], -1)
        if w == -1:
            result.append(v)
            st.pop()
            continue

        st.append(w)

    result.reverse()

    if len(result) != n + 1:
        return None

    return result


def main():
    n = int(input())

    abc = ascii_lowercase + ascii_uppercase + digits
    len_abc = len(abc)

    edges = []
    for i in range(n):
        el_1, el_2, el_3 = map(abc.index, input())
        edges.append((len_abc * el_1 + el_2, len_abc * el_2 + el_3))

    result = euler(len_abc * len_abc, n, edges)

    if result is None:
        print("NO")

    else:
        print("YES")

        ans = []
        for el in result[:n]:
            ans.append(abc[el // len_abc])

        last_el = result[n]
        ans.append(abc[last_el // len_abc])
        ans.append(abc[last_el % len_abc])

        print(*ans, sep='')


if __name__ == "__main__":
    main()
