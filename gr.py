class Graph:
    def __init__(self):
        self.v = {}

used = {}
match = {}

def dfs(gr, v, q):
    global used
    global match

    if used[v]:
        return False
    q.append(v)
    used[v] = True

    if match[v] is not None:
        u = match[v]
        if used[u]:
            for to in gr.v[v]:
                if (match[to] is None):
                    match[to] = v
                    match[v] = to
                    q.append(to)
                    return True
                elif dfs(gr, to, q):
                    match[v] = to
                    match[to] = v
                    return True
        else:
            if dfs(gr, u, q):
                match[v] = None
                return True
    else:
        for to in gr.v[v]:
            if match[to] is None:
                match[v] = to
                match[to] = v
                q.append(to)
                return True
            elif dfs(gr, to, q):
                match[v] = to
                match[to] = v
                return True

    q.pop()
    return False

def main(gr):
    global used
    global match
    for v in gr.v:
        match[v] = None

    for v in gr.v:
        if match[v] is not None:
            continue
        for u in gr.v[v]:
            if match[u] is None:
                match[u] = v
                match[v] = u
                break

    print('curr gr:')
    print_gr(gr)
    print('________________')
    for v in gr.v:
        for u in gr.v:
            used[u] = False
        q = []
        if match[v] is not None:
            continue
        if dfs(gr, v, q):
            print('dfs from ', v, 'and q is')
            print(q)
            print('curr gr:')
            print_gr(gr)
            print('________________')

def print_gr(gr):
    for v in gr.v:
        if (match[v] is not None):
            print(v, match[v])

gr = Graph()
gr.v = {'x1' : ['y1','y2'], 'x2' : ['y3'], 'x3' : ['y3'], \
        'y1' : ['x1'], 'y2' : ['x1'], 'y3' : ['x2', 'x3'] }

gr.v = {'A' : ['g', 'h'], \
        'B' : ['a', 'c', 'f', 'h', 'j'], \
        'C' : ['g'], \
        'D' : ['a', 'g', 'h', 'i'], \
        'E' : ['d', 'g'], \
        'F' : ['d', 'f', 'h'], \
        'G' : ['d'], \
        'H' : ['b', 'j'], \
        'I' : ['a', 'c', 'e', 'h'], \
        'J' : ['d', 'e'] \
       }

for v in list(gr.v):
    for to in list(gr.v[v]):
        if to not in gr.v:
            gr.v[to] = []
        gr.v[to].append(v)

main(gr)
