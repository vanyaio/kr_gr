class Graph:
    def __init__(self):
        self.v = {}
        self.l = set()
        self.r = set()

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

    c_s = contr_set(gr)
    print("contr set is ", c_s)

def contr_set(gr):
    global match

    newgr = {}
    for v in gr.v:
        newgr[v] = []

    for l in gr.l:
        for r in gr.v[l]:
            if match[l] is not None and match[l] == r:
                newgr[r].append(l)
            else:
                newgr[l].append(r)
    used = {}
    for u in gr.v:
        used[u] = False

    for l in gr.l:
        if match[l] is None:
            q = []
            dfs_contr_set(l, newgr, used, q)
            print('contr set: start dfs from', l)
            print('added vertexes ', q)
            print('*********')

    lp = set()
    rp = set()
    lm = set()
    rm = set()
    for v in used:
        if used[v] and v in gr.l:
            lp.add(v)
        if used[v] and v in gr.r:
            rp.add(v)
        if (not used[v]) and v in gr.l:
            lm.add(v)
        if (not used[v]) and v in gr.r:
            rm.add(v)

    print('lm is ', lm)
    print('rp is ', rp)
    return lm.union(rp)


def dfs_contr_set(v, newgr, used, q):
    if used[v]:
        return False
    used[v] = True
    q.append(v)

    for u in newgr[v]:
        dfs_contr_set(u, newgr, used, q)

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

gr.l = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
gr.r = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

#  gr.v = {'x1' : ['y3'], \
        #  'x2' : ['y2', 'y5'], \
        #  'x3' : ['y1', 'y4'], \
        #  'x4' : ['y1', 'y4'], \
        #  'x5' : ['y2', 'y3'], \
       #  }


for v in list(gr.v):
    for to in list(gr.v[v]):
        if to not in gr.v:
            gr.v[to] = []
        gr.v[to].append(v)

main(gr)
